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

MIN_SEGMENT_SECONDS = 0.5
BOUNDARY_TOLERANCE = 0.25  # seconds of slack when comparing to sequence edges


class EdlValidationError(Exception):
    """The EDL violates the action space (bad segment, out of range...)."""


def load_edl(edl_path: Path) -> dict:
    return json.loads(Path(edl_path).read_text())


def save_edl(edl: dict, edl_path: Path) -> None:
    edl_path.parent.mkdir(parents=True, exist_ok=True)
    edl_path.write_text(json.dumps(edl, indent=2) + "\n")


def validate_edl(edl: dict, source_duration: float) -> float:
    """Hard-fail on any malformed segment. Returns output duration."""
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
        total += end - start
    if total > source_duration:
        raise EdlValidationError(
            f"output {total:.1f}s exceeds source {source_duration:.1f}s"
        )
    return round(total, 3)


def internal_cut_timestamps(edl: dict) -> list[float]:
    """Output-timeline positions of every internal cut (for review)."""
    cuts: list[float] = []
    elapsed = 0.0
    for segment in edl["segments"][:-1]:
        elapsed += float(segment["end"]) - float(segment["start"])
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
