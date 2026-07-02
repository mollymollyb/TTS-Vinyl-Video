"""edl.py — Edit Decision List schema, validation, and integrity checks.

An EDL is the tiny, git-committable recipe for one edit: which raw
file, which time slices, in what order. Renders are regenerable from
raw + EDL, so drafts never need to be stored.

Schema (releases/{slug}/edits/vN.edl.json):
    {
      "release": "wiz-khalifa-cabin-fever-trilogy",
      "source": "Wiz Khalifa - Cabin Fever Trilogy.MOV",
      "version": 1,
      "notes": "why these cuts",
      "segments": [{"start": 12.4, "end": 19.1, "why": "vinyl 1 pull"}]
    }

Segments may optionally carry the motion toolkit (see
knowledge/editing-rules.md "Motion & pacing grammar" for WHEN, and
library/motion_filters.py for HOW):
      {"start": 1.5, "end": 5.0, "why": "cover hold",
       "motion": {"type": "punch_in", "amount": 1.10},
       "speed": 1.25}

Segment validation is adapted from auto-edit/score.py. One deliberate
divergence: auto-edit forced output duration to within +/-20% of the
source (a re-arrangement experiment); vinyl edits COMPRESS 2-3 min of
raw into 15-45s, so here the bound is simply output <= source.

check_sequence_integrity() is the heart of vinyl-review: no cut may
land strictly inside a labeled sequence — the exact failure Molly kept
seeing ("it cuts in the middle of the vinyl pull").
"""

import json
from pathlib import Path

from library.motion_filters import (
    MOTION_AMOUNT_MAX,
    MOTION_AMOUNT_MIN,
    MOTION_TYPES,
    SPEED_MAX,
    SPEED_MIN,
)

MIN_SEGMENT_SECONDS = 0.5
BOUNDARY_TOLERANCE = 0.25  # seconds of slack when comparing to sequence edges


class EdlValidationError(Exception):
    """The EDL violates the action space (bad segment, out of range...)."""


def load_edl(edl_path: Path) -> dict:
    return json.loads(Path(edl_path).read_text())


def save_edl(edl: dict, edl_path: Path) -> None:
    edl_path.parent.mkdir(parents=True, exist_ok=True)
    edl_path.write_text(json.dumps(edl, indent=2) + "\n")


def _validate_segment_motion(index: int, segment: dict) -> float:
    """Check optional motion/speed fields; return the segment's speed."""
    motion = segment.get("motion")
    if motion is not None:
        if motion.get("type") not in MOTION_TYPES:
            raise EdlValidationError(
                f"segment {index}: motion type must be one of {MOTION_TYPES}"
            )
        try:
            amount = float(motion["amount"])
        except (KeyError, TypeError, ValueError) as err:
            raise EdlValidationError(f"segment {index}: bad motion amount ({err})")
        if not MOTION_AMOUNT_MIN <= amount <= MOTION_AMOUNT_MAX:
            raise EdlValidationError(
                f"segment {index}: motion amount {amount} outside "
                f"[{MOTION_AMOUNT_MIN}, {MOTION_AMOUNT_MAX}] — subtle or nothing"
            )
    try:
        speed = float(segment.get("speed", 1.0))
    except (TypeError, ValueError) as err:
        raise EdlValidationError(f"segment {index}: bad speed ({err})")
    if not SPEED_MIN <= speed <= SPEED_MAX:
        raise EdlValidationError(
            f"segment {index}: speed {speed} outside [{SPEED_MIN}, {SPEED_MAX}]"
        )
    return speed


def segment_output_seconds(segment: dict) -> float:
    """A segment's on-screen duration (source slice divided by speed)."""
    span = float(segment["end"]) - float(segment["start"])
    return span / float(segment.get("speed", 1.0))


def validate_edl(edl: dict, source_duration: float) -> float:
    """Hard-fail on any malformed segment. Returns OUTPUT duration."""
    segments = edl.get("segments")
    if not isinstance(segments, list) or not segments:
        raise EdlValidationError("EDL 'segments' must be a non-empty list")
    total = 0.0
    for index, segment in enumerate(segments):
        try:
            start, end = float(segment["start"]), float(segment["end"])
        except (KeyError, TypeError, ValueError) as err:
            raise EdlValidationError(f"segment {index}: bad start/end ({err})")
        if end <= start:
            raise EdlValidationError(f"segment {index}: end {end} <= start {start}")
        if end - start < MIN_SEGMENT_SECONDS:
            raise EdlValidationError(
                f"segment {index}: {end - start:.2f}s < {MIN_SEGMENT_SECONDS}s minimum"
            )
        if start < 0 or end > source_duration + 0.01:
            raise EdlValidationError(
                f"segment {index}: [{start}, {end}] outside source [0, {source_duration:.2f}]"
            )
        _validate_segment_motion(index, segment)
        total += segment_output_seconds(segment)
    if total > source_duration:
        raise EdlValidationError(
            f"output {total:.1f}s exceeds source {source_duration:.1f}s"
        )
    return round(total, 3)


def internal_cut_timestamps(edl: dict) -> list[float]:
    """Output-timeline positions of every internal cut (for review).

    Speed-aware: a 1.25x segment occupies less of the output timeline
    than its source slice, and review frames must land on real cuts.
    """
    cuts: list[float] = []
    elapsed = 0.0
    for segment in edl["segments"][:-1]:
        elapsed += segment_output_seconds(segment)
        cuts.append(round(elapsed, 3))
    return cuts


def check_sequence_integrity(edl: dict, analysis: dict) -> list[str]:
    """Return violations where a segment boundary cuts INSIDE a sequence.

    Sequences come from analysis.json:
        {"sequences": [{"id": "seq-03", "type": "vinyl-pull",
                        "start": 41.2, "end": 48.9, "atomic": true, ...}]}
    A boundary is legal if it sits within BOUNDARY_TOLERANCE of the
    sequence's edge, fully outside it, inside dead-space, or inside a
    non-atomic sequence (static holds are trimmable; actions are not).
    Segments that fully CONTAIN a sequence are of course fine.
    """
    violations: list[str] = []
    sequences = [
        sequence for sequence in analysis.get("sequences", [])
        if sequence.get("type") != "dead-space"
        and sequence.get("atomic", True)
    ]
    for index, segment in enumerate(edl["segments"]):
        for boundary_name, boundary in (
            ("start", float(segment["start"])),
            ("end", float(segment["end"])),
        ):
            for sequence in sequences:
                inside_start = sequence["start"] + BOUNDARY_TOLERANCE
                inside_end = sequence["end"] - BOUNDARY_TOLERANCE
                if inside_start < boundary < inside_end:
                    violations.append(
                        f"segment {index} {boundary_name}={boundary:.2f}s cuts inside "
                        f"{sequence['id']} ({sequence['type']} "
                        f"{sequence['start']:.2f}-{sequence['end']:.2f}s)"
                    )
    return violations
