"""ingest.py — register raw footage as release records. Tier 0.

Scans {mediaRoot}/raw/, groups files into releases (multiple takes like
"... 1.MOV" / "... 2.MOV" collapse into one release), probes each file
with ffprobe, and writes releases/{slug}/release.json + README.md into
GIT (tiny text). Raw files are never moved or modified.

Usage (from repo root):
    python3 -m library.ingest --all
    python3 -m library.ingest --file "Wiz Khalifa - Cabin Fever Trilogy.MOV"
"""

import datetime as dt
import json
import re
import sys
from pathlib import Path

from library.env_config import REPO_ROOT
from library.ffprobe import probe_video_metadata
from library.media_paths import list_raw_files

RELEASES_DIR = REPO_ROOT / "releases"

# Known filename typos -> canonical spelling, so takes group correctly.
TITLE_ALIASES = {
    "blacc hollywod": "blacc hollywood",
}

# Weak hints only; every guess ships as "draft - confirm with Molly".
TYPE_HINTS = {
    "trilogy": "3xLP",
    "live": "2xLP",
}


def parse_raw_filename(filename: str) -> dict:
    """'Wiz Khalifa - Blacc Hollywod 2.MOV' ->
    {artist: 'Wiz Khalifa', title: 'Blacc Hollywood', take: 2}"""
    stem = Path(filename).stem.strip()
    artist, _, rest = stem.partition(" - ")
    if not rest:  # no ' - ' separator: treat whole stem as title
        artist, rest = "Unknown", stem
    take = 1
    match = re.search(r"\s+(\d+)$", rest)
    if match:
        take = int(match.group(1))
        rest = rest[: match.start()].strip()
    title_key = rest.lower()
    title = TITLE_ALIASES.get(title_key, title_key).title()
    return {"artist": artist.strip(), "title": title, "take": take}


def slugify(artist: str, title: str) -> str:
    combined = f"{artist} {title}".lower()
    return re.sub(r"[^a-z0-9]+", "-", combined).strip("-")


def guess_release_type(title: str) -> str:
    for hint, release_type in TYPE_HINTS.items():
        if hint in title.lower():
            return release_type
    return "unknown"


def group_releases(raw_files: list[Path]) -> dict[str, dict]:
    """Group raw files by (artist, title) into release records."""
    releases: dict[str, dict] = {}
    for raw_path in raw_files:
        parsed = parse_raw_filename(raw_path.name)
        slug = slugify(parsed["artist"], parsed["title"])
        record = releases.setdefault(
            slug,
            {
                "slug": slug,
                "artist": parsed["artist"],
                "title": parsed["title"],
                "release_type": guess_release_type(parsed["title"]),
                "release_type_confirmed": False,
                "status": "raw",
                "created": dt.date.today().isoformat(),
                "raw_files": [],
            },
        )
        metadata = probe_video_metadata(raw_path)
        record["raw_files"].append(
            {"file": raw_path.name, "take": parsed["take"], **metadata}
        )
    for record in releases.values():
        record["raw_files"].sort(key=lambda f: f["take"])
    return releases


def write_release(record: dict) -> Path:
    """Write release.json + a README dashboard stub. Preserves fields a
    human/agent already confirmed (type, status) on re-ingest."""
    release_dir = RELEASES_DIR / record["slug"]
    release_dir.mkdir(parents=True, exist_ok=True)
    release_path = release_dir / "release.json"

    if release_path.exists():
        existing = json.loads(release_path.read_text())
        for keep in ("release_type", "release_type_confirmed", "status", "created"):
            if keep in existing:
                record[keep] = existing[keep]

    release_path.write_text(json.dumps(record, indent=2) + "\n")

    takes = "\n".join(
        f"- take {f['take']}: `{f['file']}` — {f['duration_seconds']}s, "
        f"{f['width']}x{f['height']} @ {f['fps']}fps, {f['size_mb']}MB"
        for f in record["raw_files"]
    )
    (release_dir / "README.md").write_text(
        f"# {record['artist']} — {record['title']}\n\n"
        f"- **Status:** {record['status']}\n"
        f"- **Release type:** {record['release_type']}"
        f"{'' if record['release_type_confirmed'] else ' (draft — confirm)'}\n\n"
        f"## Raw takes\n\n{takes}\n\n"
        "## Files\n\n"
        "- `release.json` — machine record\n"
        "- `analysis.json` — shots + sequences (after fatbeats-content-analyze)\n"
        "- `edits/vN.edl.json` — edit recipes (after fatbeats-content-edit)\n"
        "- `caption.md` — caption + product description (after fatbeats-content-caption)\n"
    )
    return release_path


def main() -> int:
    args = sys.argv[1:]
    raw_files = list_raw_files()
    if "--file" in args:
        wanted = args[args.index("--file") + 1]
        raw_files = [f for f in raw_files if f.name == wanted]
    if not raw_files:
        print("No raw files found to ingest.", file=sys.stderr)
        return 1
    releases = group_releases(raw_files)
    for slug, record in sorted(releases.items()):
        path = write_release(record)
        print(f"{slug}: {len(record['raw_files'])} take(s) -> {path.relative_to(REPO_ROOT)}")
    print(f"\n{len(releases)} release(s) registered.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
