"""frame_sample.py — extract still frames for shot labeling. Tier 0.

Produces small JPEGs under derived/{slug}/frames/ that either Twelve
Labs supplements (Tier 2) or the agent Reads and labels itself (Tier 1
— the keyless fallback). Also used by fatbeats-content-review to inspect the
frames around each cut in a rendered draft.

Usage:
    frames = sample_shot_frames(proxy, intervals, frames_dir)
    # frames_dir/shot003_t42.10.jpg ... (one mid-shot frame per interval)
"""

import subprocess
from pathlib import Path

FRAME_WIDTH = 480
JPEG_QUALITY = "4"  # ffmpeg qscale; 2 best - 31 worst


def extract_frame_at(
    video_path: Path, timestamp: float, out_path: Path, width: int = FRAME_WIDTH
) -> Path:
    """Grab one frame at `timestamp` seconds into out_path (JPEG)."""
    out_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-ss", f"{timestamp:.3f}",
            "-i", str(video_path),
            "-frames:v", "1",
            "-vf", f"scale={width}:-2",
            "-q:v", JPEG_QUALITY,
            str(out_path),
        ],
        check=True,
    )
    return out_path


def sample_shot_frames(
    video_path: Path,
    intervals: list[tuple[float, float]],
    frames_dir: Path,
    width: int = FRAME_WIDTH,
) -> list[dict]:
    """One representative (midpoint) frame per shot interval.

    Returns [{"shot": i, "timestamp": t, "frame": "<abs path>"}] so
    analysis.json can point the agent straight at each image.
    """
    samples: list[dict] = []
    for index, (start, end) in enumerate(intervals):
        midpoint = round((start + end) / 2, 2)
        frame_path = frames_dir / f"shot{index:03d}_t{midpoint:.2f}.jpg"
        if not frame_path.exists():
            extract_frame_at(video_path, midpoint, frame_path, width)
        samples.append(
            {"shot": index, "timestamp": midpoint, "frame": str(frame_path)}
        )
    return samples


def sample_cut_context(
    video_path: Path,
    cut_timestamps: list[float],
    frames_dir: Path,
    offset: float = 0.3,
) -> list[dict]:
    """Frames just before/after each internal cut — fatbeats-content-review's evidence
    for 'did this cut land mid-motion?'."""
    samples: list[dict] = []
    for index, cut in enumerate(cut_timestamps):
        pair = {}
        for side, timestamp in (("before", cut - offset), ("after", cut + offset)):
            frame_path = frames_dir / f"cut{index:02d}_{side}_t{max(timestamp, 0):.2f}.jpg"
            if not frame_path.exists():
                extract_frame_at(video_path, max(timestamp, 0.0), frame_path)
            pair[side] = str(frame_path)
        samples.append({"cut": index, "timestamp": cut, **pair})
    return samples
