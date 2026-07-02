"""env_config.py — the ONE .env loader + typed secret accessors.

Every key is OPTIONAL by design (see CLAUDE.md "Capability tiers").
Callers must treat a None return as "run the keyless fallback", never
as an error.

Usage:
    from library.env_config import get_twelve_labs_key
    key = get_twelve_labs_key()   # str | None
"""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

_loaded = False


def load_env() -> None:
    """Load REPO_ROOT/.env into os.environ once. Real env vars win on
    conflict so CI / shell overrides behave as expected."""
    global _loaded
    if _loaded:
        return
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        for raw_line in env_path.read_text().splitlines():
            line = raw_line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and not os.environ.get(key):
                os.environ[key] = value
    _loaded = True


def _get_optional(name: str) -> str | None:
    load_env()
    value = os.environ.get(name, "").strip()
    return value or None


def get_twelve_labs_key() -> str | None:
    """Tier 2 unlock: programmatic shot labeling via Twelve Labs."""
    return _get_optional("TWELVE_LABS_API_KEY")


def get_tribe_key() -> str | None:
    """Tier 3 unlock: tribe-viral engagement tiebreaker (optional)."""
    return _get_optional("SWIFT_LABS_TRIBE_API_KEY")
