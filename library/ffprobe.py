"""ffprobe.py — video metadata via ffprobe. Pure local, zero keys (Tier 0).

Replaces the two duplicated probe_duration copies that lived in
sidney/labs/auto-edit's score.py and analyze_render.py.

Usage:
    from library.ffprobe import probe_video_metadata
    meta = probe_video_metadata(Path("clip.MOV"))
    # {"duration_seconds": 162.4, "fps": 60.0, "width": 2160, ...}
"""

import json
import subprocess
from pathlib import Path


def probe_duration_seconds(video_path: Path) -> float:
    """Duration in seconds — the source of truth for EDL validation."""
    output = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1",
            str(video_path),
        ],
        text=True,
    ).strip()
    return float(output)


def probe_video_metadata(video_path: Path) -> dict:
    """Duration, fps, resolution, and size for release records."""
    output = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate",
            "-show_entries", "format=duration,size",
            "-of", "json",
            str(video_path),
        ],
        text=True,
    )
    parsed = json.loads(output)
    stream = (parsed.get("streams") or [{}])[0]
    fmt = parsed.get("format") or {}

    numerator, _, denominator = str(stream.get("r_frame_rate", "0/1")).partition("/")
    fps = float(numerator) / float(denominator or 1) if float(denominator or 1) else 0.0

    return {
        "duration_seconds": round(float(fmt.get("duration", 0.0)), 3),
        "fps": round(fps, 2),
        "width": stream.get("width"),
        "height": stream.get("height"),
        "size_mb": round(int(fmt.get("size", 0)) / (1024 * 1024), 1),
    }
