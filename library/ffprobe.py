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
    """Duration, fps, DISPLAY resolution, and size for release records.

    iPhone MOVs store landscape frames plus a rotation=±90 flag; ffmpeg
    auto-rotates whenever it filters/re-encodes. Reporting the stored
    dimensions therefore lies to every consumer (zoompan sizing, release
    records), so width/height are swapped here when the flag says
    portrait. (Caught 2026-07-02: motion demo rendered stretched
    landscape segments.)
    """
    output = subprocess.check_output(
        [
            "ffprobe", "-v", "error",
            "-select_streams", "v:0",
            "-show_entries", "stream=width,height,r_frame_rate",
            "-show_entries", "stream_side_data=rotation",
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

    rotation = 0
    for side_data in stream.get("side_data_list", []):
        if "rotation" in side_data:
            rotation = int(side_data["rotation"])
    width, height = stream.get("width"), stream.get("height")
    if rotation % 180 != 0:
        width, height = height, width

    return {
        "duration_seconds": round(float(fmt.get("duration", 0.0)), 3),
        "fps": round(fps, 2),
        "width": width,
        "height": height,
        "size_mb": round(int(fmt.get("size", 0)) / (1024 * 1024), 1),
    }
