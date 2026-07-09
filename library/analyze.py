"""analyze.py — thin orchestrator: raw take -> analysis.json (draft).

Pipeline (timestamps from the proxy transfer 1:1 to the raw file):
    1. proxy       (Tier 0)  720p working copy in derived/{slug}/
    2. scene map   (Tier 0)  ffmpeg scene filter + long-shot subdivision
    3. frames      (Tier 0)  one midpoint JPEG per shot for labeling
    4. labels      (Tier 2)  Twelve Labs Pegasus per shot, IF key present
                   (Tier 1)  otherwise shots stay unlabeled and the
                             fatbeats-content-analyze skill has the agent Read the
                             frames and fill in labels itself

Output: releases/{slug}/analysis.json with shots[] labeled or not, and
an EMPTY sequences[] — grouping shots into never-cut sequences is the
semantic pass the agent always does (see plugin/skills/fatbeats-content-analyze).

Usage (from repo root):
    python3 -m library.analyze --release wiz-khalifa-cabin-fever-trilogy [--take 1] [--no-tl]
"""

import datetime as dt
import json
import sys
from pathlib import Path

from library import twelvelabs_client
from library.env_config import REPO_ROOT
from library.ffprobe import probe_duration_seconds
from library.frame_sample import sample_shot_frames
from library.media_paths import derived_dir, find_raw_file
from library.proxy import ensure_proxy
from library.scene_detect import (
    detect_scene_changes,
    shot_intervals,
    split_long_intervals,
)


def load_release(slug: str) -> dict:
    release_path = REPO_ROOT / "releases" / slug / "release.json"
    if not release_path.exists():
        raise FileNotFoundError(
            f"{release_path} missing — run `python3 -m library.ingest --all` first"
        )
    return json.loads(release_path.read_text())


def analyze_take(slug: str, take: int = 1, use_twelve_labs: bool = True) -> Path:
    release = load_release(slug)
    take_record = next(
        (f for f in release["raw_files"] if f["take"] == take), None
    )
    if take_record is None:
        raise ValueError(f"take {take} not found in {slug}/release.json")

    raw_path = find_raw_file(take_record["file"], slug)
    shot_dir = derived_dir(slug)

    print(f"[1/4] proxy for {raw_path.name}")
    proxy_path = ensure_proxy(raw_path, shot_dir / f"proxy-take{take}.mp4")
    duration = probe_duration_seconds(proxy_path)

    print("[2/4] scene map")
    changes = detect_scene_changes(proxy_path)
    intervals = split_long_intervals(shot_intervals(changes, duration))
    print(f"      {len(intervals)} shots over {duration:.1f}s")

    print("[3/4] midpoint frames")
    frames = sample_shot_frames(
        proxy_path, intervals, shot_dir / f"frames-take{take}"
    )

    tier = "0"
    shots: list[dict] = []
    labeled = False
    if use_twelve_labs and twelvelabs_client.is_available():
        print("[4/4] Twelve Labs labels (Tier 2)")
        video_id = twelvelabs_client.get_or_upload_video(proxy_path)
        for index, (start, end) in enumerate(intervals):
            label = twelvelabs_client.describe_shot(video_id, start, end)
            shots.append(
                {
                    "shot": index,
                    "start": start,
                    "end": end,
                    "frame": frames[index]["frame"],
                    **label,
                }
            )
            print(f"      shot {index:>2} {start:>7.2f}-{end:<7.2f} {label['sequence_type']:<16} {label['key_action']}")
        tier, labeled = "2", True
    else:
        print("[4/4] no Twelve Labs key (or --no-tl) — Tier 1: agent labels the frames")
        for index, (start, end) in enumerate(intervals):
            shots.append(
                {
                    "shot": index,
                    "start": start,
                    "end": end,
                    "frame": frames[index]["frame"],
                    "visual": None,
                    "key_action": None,
                    "sequence_type": None,
                    "motion_state": None,
                }
            )
        tier = "1"

    analysis = {
        "release": slug,
        "take": take,
        "source": take_record["file"],
        "duration_seconds": round(duration, 3),
        "analyzed": dt.datetime.now().isoformat(timespec="seconds"),
        "tier": tier,
        "shots_labeled": labeled,
        "shots": shots,
        # The agent's semantic pass fills this (fatbeats-content-analyze skill):
        # contiguous shots forming one event share a sequence with a
        # hard never-cut-inside boundary.
        "sequences": [],
    }
    # Take 1 keeps the historical name so single-take releases (and every
    # consumer that reads analysis.json) are untouched; further takes get
    # sibling files instead of overwriting take 1's analysis.
    name = "analysis.json" if take == 1 else f"analysis-take{take}.json"
    out_path = REPO_ROOT / "releases" / slug / name
    out_path.write_text(json.dumps(analysis, indent=2) + "\n")
    print(f"\nwrote {out_path.relative_to(REPO_ROOT)} (tier {tier})")
    return out_path


def main() -> int:
    args = sys.argv[1:]
    if "--release" not in args:
        print(__doc__)
        return 2
    slug = args[args.index("--release") + 1]
    take = int(args[args.index("--take") + 1]) if "--take" in args else 1
    use_tl = "--no-tl" not in args
    analyze_take(slug, take, use_tl)
    return 0


if __name__ == "__main__":
    sys.exit(main())
