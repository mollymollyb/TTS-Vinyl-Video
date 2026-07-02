"""proxy.py — low-res working copies of raw footage. Tier 0.

Raw vinyl footage is 4K (~400MB per 2-3 min). Scene detection, frame
sampling, and Twelve Labs uploads all run dramatically faster on a 720p
proxy, and timestamps are identical to the raw file, so every analysis
result transfers 1:1. Final renders always cut from the RAW file.

Usage:
    from library.proxy import ensure_proxy
    proxy = ensure_proxy(raw_path, derived_dir(slug) / "proxy-take1.mp4")
"""

import subprocess
from pathlib import Path

PROXY_WIDTH = 720


def ensure_proxy(source_path: Path, proxy_path: Path, width: int = PROXY_WIDTH) -> Path:
    """Create (or reuse) a downscaled H.264 proxy of source_path."""
    if proxy_path.exists() and proxy_path.stat().st_size > 0:
        return proxy_path
    proxy_path.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            "ffmpeg", "-y", "-loglevel", "error",
            "-i", str(source_path),
            # -2 keeps height divisible by 2 for any aspect ratio
            "-vf", f"scale={width}:-2",
            "-c:v", "libx264", "-preset", "veryfast", "-crf", "26",
            "-c:a", "aac", "-b:a", "96k",
            str(proxy_path),
        ],
        check=True,
    )
    return proxy_path
