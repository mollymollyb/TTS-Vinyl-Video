"""scene_detect.py — visual change detection via ffmpeg. Tier 0, no network.

Adapted from sidney/labs/auto-edit/analyze_render.py (Sidney Swift, 2026):
ffmpeg's scene filter finds frame-accurate visual cuts far more reliably
than asking a vision model to localize them.

Vinyl raw footage is mostly ONE continuous handheld take, so hard cuts
are rare; split_long_intervals() subdivides long stretches into fixed
windows so labeling still has usable granularity. Those synthetic
boundaries are analysis granularity, NOT candidate cut points — cut
decisions belong to sequences (see library/edl.py).

Usage:
    changes = detect_scene_changes(proxy_path)
    intervals = shot_intervals(changes, duration)
    intervals = split_long_intervals(intervals, max_len=6.0)
"""

import re
import subprocess
from pathlib import Path

# 0.25 (vs auto-edit's 0.3) because handheld vinyl footage transitions
# smoothly; slightly more sensitive catches product-to-product moves.
SCENE_THRESHOLD = 0.25
MIN_SHOT_GAP_SECONDS = 0.5


def detect_scene_changes(
    video_path: Path, threshold: float = SCENE_THRESHOLD
) -> list[float]:
    """ffmpeg scene filter -> sorted, deduped cut timestamps (seconds)."""
    command = [
        "ffmpeg", "-i", str(video_path),
        "-filter:v", f"select='gt(scene,{threshold})',showinfo",
        "-f", "null", "-",
    ]
    result = subprocess.run(command, capture_output=True, text=True)
    timestamps: list[float] = []
    for line in result.stderr.splitlines():
        match = re.search(r"pts_time:([0-9.]+)", line)
        if match:
            timestamps.append(float(match.group(1)))
    if not timestamps or timestamps[0] > 0.05:
        timestamps.insert(0, 0.0)
    deduped: list[float] = []
    for timestamp in sorted(timestamps):
        if not deduped or timestamp - deduped[-1] >= MIN_SHOT_GAP_SECONDS:
            deduped.append(timestamp)
    return deduped


def shot_intervals(
    changes: list[float], duration: float
) -> list[tuple[float, float]]:
    """Cut timestamps -> contiguous (start, end) intervals covering [0, duration]."""
    intervals: list[tuple[float, float]] = []
    for index, start in enumerate(changes):
        end = changes[index + 1] if index + 1 < len(changes) else duration
        if end - start > 0.01:
            intervals.append((round(start, 3), round(end, 3)))
    return intervals


def split_long_intervals(
    intervals: list[tuple[float, float]], max_len: float = 6.0
) -> list[tuple[float, float]]:
    """Subdivide intervals longer than max_len into equal-ish windows."""
    result: list[tuple[float, float]] = []
    for start, end in intervals:
        length = end - start
        if length <= max_len:
            result.append((start, end))
            continue
        pieces = int(length // max_len) + (1 if length % max_len > 0.5 else 0)
        pieces = max(pieces, 1)
        step = length / pieces
        for i in range(pieces):
            piece_start = round(start + i * step, 3)
            piece_end = round(end if i == pieces - 1 else start + (i + 1) * step, 3)
            result.append((piece_start, piece_end))
    return result
