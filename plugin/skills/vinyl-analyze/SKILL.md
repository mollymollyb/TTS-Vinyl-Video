---
name: vinyl-analyze
description: Turn one raw take into a labeled shot and sequence map (analysis.json). Use after ingest, when the user says "analyze this footage", "map the shots", or before any editing on a release that lacks analysis.json. Works with or without a Twelve Labs key.
---

# Vinyl analyze — machine pass, then YOUR semantic pass

## 1. Machine pass

Run `.venv/bin/python -m library.analyze --release {slug} [--take N]`.
It builds a 720p proxy, scene-maps it, extracts one midpoint frame per
shot, and — if `TWELVE_LABS_API_KEY` is set (Tier 2) — labels every shot
(visual, key_action, sequence_type, motion_state).

**Tier 1 fallback (no key):** shots come back unlabeled. Read each
frame image listed in `shots[].frame` yourself and fill in the same four
fields directly in `analysis.json`. Use the `sequence_type` vocabulary
from `library/twelvelabs_client.py` (SEQUENCE_TYPES). If a shot is
ambiguous from its midpoint frame, extract extra frames with
`library.frame_sample.extract_frame_at` before guessing.

## 2. Sequence pass (always yours — this is the never-cut map)

Group contiguous shots into **sequences**: one complete event each
(a vinyl pull start-to-finish, a gatefold open, one pan across the
tracklist). Write them into `analysis.json` as:

```json
{"id": "seq-03", "type": "vinyl-pull", "start": 41.2, "end": 48.9,
 "shots": [7, 8], "note": "pulls disc 2, holds it up"}
```

Rules:
- Every second of the take belongs to exactly one sequence; label
  non-showcase stretches `dead-space` (those ARE cuttable).
- Boundaries sit where motion completes, not where the scene detector
  fired — trust `motion_state`: a `mid-motion` shot NEVER ends a sequence.
- Spot-check 2-3 boundary frames with `extract_frame_at` before saving.
- Count the vinyl-pull sequences; if it contradicts `release_type`
  (e.g. 3 pulls but type says 1xLP), flag it in your report and in the
  release README.

## 3. Close out

Set release status to `analyzed` and update the release `README.md`,
`releases/_board.md`, and `artifacts/dashboard.html` in the same turn.
