"""doctor.py — deterministic, READ-ONLY workspace health check.

The mechanical fast path behind the fatbeats-content-doctor skill: checks that need
no judgment live here so they ship with the build and never get
reinvented. Writes operations/health.md and prints the same report.
Exit code 0 = healthy (score >= 80), 1 = needs attention.

Usage (from repo root):
    .venv/bin/python operations/doctor.py
"""

import datetime as dt
import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from library.genmedia_ledger import load_ledger, validate_ledger  # noqa: E402
from library.media_paths import MediaConfigError, media_root  # noqa: E402

MEDIA_EXTENSIONS = (".mov", ".mp4", ".m4v", ".avi")
SEVERITY_COST = {"high": 10, "med": 5, "low": 2}

findings: list[tuple[str, str]] = []  # (severity, message)


def finding(severity: str, message: str) -> None:
    findings.append((severity, message))


def check_environment() -> None:
    for tool in ("ffmpeg", "ffprobe"):
        if not shutil.which(tool):
            finding("high", f"{tool} not on PATH (brew install ffmpeg)")
    if not (REPO_ROOT / ".venv").is_dir():
        finding("med", ".venv missing — python3 -m venv .venv && .venv/bin/pip install -r requirements.txt")


def check_media_config() -> None:
    try:
        root = media_root()
    except MediaConfigError as err:
        finding("high", f"media config: {str(err).splitlines()[0]}")
        return
    for sub in ("raw", "derived", "work", "finals"):
        if not (root / sub).is_dir():
            finding("med", f"media root missing {sub}/ ({root / sub})")


def check_git_hygiene() -> None:
    tracked = subprocess.check_output(
        ["git", "ls-files"], cwd=REPO_ROOT, text=True
    ).splitlines()
    for path in tracked:
        if path.lower().endswith(MEDIA_EXTENSIONS):
            finding("high", f"MEDIA FILE TRACKED BY GIT: {path}")
        if path in (".env", "media.config.json", ".tl_cache.json"):
            finding("high", f"per-machine/secret file tracked by git: {path}")


def load_releases() -> list[dict]:
    releases = []
    releases_dir = REPO_ROOT / "releases"
    if not releases_dir.is_dir():
        finding("high", "releases/ directory missing")
        return releases
    for release_dir in sorted(releases_dir.iterdir()):
        if not release_dir.is_dir() or release_dir.name.startswith("_"):
            continue
        record_path = release_dir / "release.json"
        if not record_path.exists():
            finding("med", f"{release_dir.name}: missing release.json")
            continue
        record = json.loads(record_path.read_text())
        record["_dir"] = release_dir
        releases.append(record)
        if not (release_dir / "README.md").exists():
            finding("low", f"{release_dir.name}: missing README.md dashboard")
    return releases


def check_release_consistency(releases: list[dict]) -> None:
    """Status must match artifacts on disk — the never-stale contract."""
    order = ["raw", "analyzed", "editing", "review", "final"]
    for record in releases:
        slug, status, release_dir = record["slug"], record.get("status", "raw"), record["_dir"]
        if status not in order:
            finding("med", f"{slug}: unknown status '{status}'")
            continue
        rank = order.index(status)
        analysis_path = release_dir / "analysis.json"
        if rank >= 1:
            if not analysis_path.exists():
                finding("med", f"{slug}: status {status} but no analysis.json")
            elif not json.loads(analysis_path.read_text()).get("sequences"):
                finding("med", f"{slug}: analysis.json has no sequences (semantic pass not done)")
        if rank >= 2 and not list((release_dir / "edits").glob("v*.edl.json")):
            finding("med", f"{slug}: status {status} but no EDLs in edits/")
        if rank >= 4:
            try:
                if not any((media_root() / "finals" / slug).glob("*")):
                    finding("med", f"{slug}: status final but finals/{slug}/ is empty")
            except MediaConfigError:
                pass
        if record.get("release_type") == "unknown" and rank >= 2:
            finding("low", f"{slug}: editing without a release type — confirm with Molly")


def check_genmedia_ledgers() -> None:
    for ledger_path in sorted((REPO_ROOT / "releases").glob("*/genmedia.json")):
        slug = ledger_path.parent.name
        for problem in validate_ledger(load_ledger(slug)):
            finding("med", f"{slug}: genmedia.json — {problem}")


def check_boards(releases: list[dict]) -> None:
    for artifact in ("releases/_board.md", "artifacts/dashboard.html"):
        path = REPO_ROOT / artifact
        if not path.exists():
            finding("med", f"{artifact} missing")
            continue
        content = path.read_text()
        for record in releases:
            if record["slug"] not in content:
                finding("low", f"{artifact} does not mention {record['slug']} (stale)")


def check_routines() -> None:
    index = REPO_ROOT / "routines" / "README.md"
    if not index.exists():
        finding("med", "routines/README.md index missing")
        return
    if "armed: yes" not in index.read_text():
        finding("low", "no routine is schedule-armed — janitor only runs on demand")


def check_plugin() -> None:
    names = set()
    for manifest in (
        REPO_ROOT / "plugin/.claude-plugin/plugin.json",
        REPO_ROOT / "plugin/.codex-plugin/plugin.json",
    ):
        if not manifest.exists():
            finding("med", f"{manifest.relative_to(REPO_ROOT)} missing")
            continue
        try:
            names.add(json.loads(manifest.read_text())["name"])
        except (json.JSONDecodeError, KeyError):
            finding("med", f"{manifest.relative_to(REPO_ROOT)} invalid")
    if len(names) > 1:
        finding("med", f"plugin manifests disagree on name: {names}")
    skills_dir = REPO_ROOT / "plugin" / "skills"
    for skill_dir in sorted(skills_dir.iterdir()) if skills_dir.is_dir() else []:
        if skill_dir.is_dir() and not (skill_dir / "SKILL.md").exists():
            finding("med", f"plugin/skills/{skill_dir.name}/ has no SKILL.md")


def main() -> int:
    check_environment()
    check_media_config()
    check_git_hygiene()
    releases = load_releases()
    check_release_consistency(releases)
    check_genmedia_ledgers()
    check_boards(releases)
    check_routines()
    check_plugin()

    score = max(0, 100 - sum(SEVERITY_COST[severity] for severity, _ in findings))
    lines = [
        "# Workspace health",
        "",
        f"- **Score:** {score}/100",
        f"- **Run:** {dt.datetime.now().isoformat(timespec='seconds')} (operations/doctor.py — mechanical checks)",
        f"- **Releases:** {len(releases)}",
        "",
    ]
    if findings:
        lines.append("| severity | finding |")
        lines.append("|---|---|")
        for severity, message in sorted(findings, key=lambda f: SEVERITY_COST[f[0]], reverse=True):
            lines.append(f"| {severity} | {message} |")
    else:
        lines.append("No mechanical findings. Clean bill of health.")
    report = "\n".join(lines) + "\n"
    (REPO_ROOT / "operations" / "health.md").write_text(report)
    print(report)
    return 0 if score >= 80 else 1


if __name__ == "__main__":
    sys.exit(main())
