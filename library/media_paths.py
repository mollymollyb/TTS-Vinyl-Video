"""media_paths.py — the ONLY place media byte paths are resolved.

The media root lives OUTSIDE git (locally or on Google Drive) and is
found via media.config.json (per-machine, gitignored). Lifecycle:

    {mediaRoot}/raw/       originals — never modified, never deleted
    {mediaRoot}/derived/{slug}/   regenerable: proxies, frames, shots
    {mediaRoot}/work/{slug}/{YYYY-MM-DD}/   throwaway draft renders
    {mediaRoot}/finals/{slug}/    approved deliverables

Raw files may sit flat in raw/ (matching Molly's Drive folder) or in
raw/{slug}/ subfolders; find_raw_file() checks both.

Usage:
    from library.media_paths import work_dir
    out = work_dir("wiz-khalifa-cabin-fever-trilogy") / "v1.mp4"
"""

import datetime as dt
import json
from pathlib import Path

from library.env_config import REPO_ROOT

CONFIG_PATH = REPO_ROOT / "media.config.json"


class MediaConfigError(RuntimeError):
    """media.config.json missing or the configured root is unreachable."""


def media_root() -> Path:
    """Resolve the media root, failing with copy-pasteable fix steps."""
    if not CONFIG_PATH.exists():
        raise MediaConfigError(
            "media.config.json not found. Fix:\n"
            "  cp media.config.example.json media.config.json\n"
            "  then set mediaRoot to your machine's absolute media path."
        )
    root = Path(json.loads(CONFIG_PATH.read_text())["mediaRoot"]).expanduser()
    if not root.is_dir():
        raise MediaConfigError(
            f"mediaRoot does not exist: {root}\n"
            "Edit media.config.json (is Google Drive synced on this machine?)."
        )
    return root


def raw_dir() -> Path:
    return media_root() / "raw"


def derived_dir(slug: str) -> Path:
    path = media_root() / "derived" / slug
    path.mkdir(parents=True, exist_ok=True)
    return path


def work_dir(slug: str, date: str | None = None) -> Path:
    date = date or dt.date.today().isoformat()
    path = media_root() / "work" / slug / date
    path.mkdir(parents=True, exist_ok=True)
    return path


def finals_dir(slug: str) -> Path:
    path = media_root() / "finals" / slug
    path.mkdir(parents=True, exist_ok=True)
    return path


def find_raw_file(filename: str, slug: str | None = None) -> Path:
    """Locate a raw file by name — raw/{slug}/ first, then flat raw/."""
    candidates = []
    if slug:
        candidates.append(raw_dir() / slug / filename)
    candidates.append(raw_dir() / filename)
    for candidate in candidates:
        if candidate.exists():
            return candidate
    raise FileNotFoundError(
        f"Raw file '{filename}' not found under {raw_dir()} "
        f"(checked {[str(c) for c in candidates]})"
    )


def list_raw_files() -> list[Path]:
    """All raw video files (flat or one level of slug subfolders)."""
    root = raw_dir()
    if not root.is_dir():
        return []
    videos: list[Path] = []
    for pattern in ("*.MOV", "*.mov", "*.mp4", "*.MP4"):
        videos.extend(root.glob(pattern))
        videos.extend(root.glob(f"*/{pattern}"))
    return sorted(set(videos))
