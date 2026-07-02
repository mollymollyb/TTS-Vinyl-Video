"""edl_render.py — render an EDL into an mp4. Tier 0, pure ffmpeg.

Vendored from auto-edit/score.py's render_concat() (Sidney Swift, 2026):
re-encode each segment individually (no keyframe-alignment problems at
arbitrary cut points), then concat-demux with stream copy. Quality is
raised vs the lab version (crf 20 veryfast, not ultrafast) because these
renders are deliverables, not scoring fodder.

Usage (from repo root):
    python3 -m library.edl_render releases/<slug>/edits/v1.edl.json
    -> renders to {mediaRoot}/work/{slug}/{today}/v1.mp4 from the RAW file
"""

import subprocess
import sys
import tempfile
from pathlib import Path

from library.edl import load_edl, validate_edl
from library.ffprobe import probe_duration_seconds
from library.media_paths import find_raw_file, work_dir


def render_edl(source_path: Path, edl: dict, out_path: Path) -> Path:
    """Cut edl['segments'] from source_path, concat in order -> out_path."""
    validate_edl(edl, probe_duration_seconds(source_path))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="vinyl_render_") as tmp:
        tmp_dir = Path(tmp)
        segment_paths: list[Path] = []
        for index, segment in enumerate(edl["segments"]):
            segment_path = tmp_dir / f"seg_{index:03d}.mp4"
            subprocess.run(
                [
                    "ffmpeg", "-y", "-loglevel", "error",
                    "-ss", str(segment["start"]),
                    "-to", str(segment["end"]),
                    "-i", str(source_path),
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-c:a", "aac", "-b:a", "160k",
                    str(segment_path),
                ],
                check=True,
            )
            segment_paths.append(segment_path)

        concat_list = tmp_dir / "concat.txt"
        concat_list.write_text(
            "\n".join(f"file '{p.as_posix()}'" for p in segment_paths)
        )
        subprocess.run(
            [
                "ffmpeg", "-y", "-loglevel", "error",
                "-f", "concat", "-safe", "0",
                "-i", str(concat_list),
                "-c", "copy",
                str(out_path),
            ],
            check=True,
        )
    return out_path


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 -m library.edl_render <path/to/vN.edl.json> [out.mp4]")
        return 2
    edl_path = Path(sys.argv[1])
    edl = load_edl(edl_path)
    source = find_raw_file(edl["source"], edl.get("release"))
    if len(sys.argv) > 2:
        out_path = Path(sys.argv[2])
    else:
        out_path = work_dir(edl["release"]) / f"{edl_path.stem.replace('.edl', '')}.mp4"
    rendered = render_edl(source, edl, out_path)
    print(f"rendered: {rendered}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
