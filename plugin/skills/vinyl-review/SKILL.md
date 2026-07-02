---
name: vinyl-review
description: Self-review a rendered edit before any human sees it — the system watching its own output. Use after vinyl-edit renders a draft, or when the user says "review this cut", "check the edit", "did it cut mid-sequence". Catches mid-sequence cuts, dead space, and bad endings, then drives re-edits.
---

# Vinyl review — the watch-itself loop

For each rendered variant (EDL + its mp4 in the media `work/` folder):

## 1. Mechanical integrity (must pass before anything else)

Run from the repo root:

```bash
.venv/bin/python - <<'EOF'
import json
from library.edl import load_edl, check_sequence_integrity, internal_cut_timestamps
edl = load_edl("releases/{slug}/edits/v1.edl.json")
analysis = json.loads(open("releases/{slug}/analysis.json").read())
print("violations:", check_sequence_integrity(edl, analysis) or "NONE")
print("internal cuts at:", internal_cut_timestamps(edl))
EOF
```

Any violation = fail. Go back to the EDL, move the boundary to the
sequence edge (or drop the segment), re-render, re-review.

## 2. Visual boundary check (your eyes on the actual render)

Extract before/after frames around every internal cut of the RENDER with
`library.frame_sample.sample_cut_context` (output them into the release's
derived `review/` folder), then Read each pair and judge:
- Does the outgoing frame complete its motion (`completing`/`static`)?
- Does the incoming frame start something new (not mid-blur)?
- Extract the final 3 frames of the render: does it END on a held
  product or completed motion (hard rule 5)?

## 3. Energy pass — "can I make this better?" (after integrity passes)

Correct is the floor; this cut also has to feel alive on a feed. Compute
per-segment OUTPUT durations (`library.edl.segment_output_seconds`) and
interrogate the cut against the Motion & pacing grammar
(`knowledge/editing-rules.md`):

- Rhythm: is the back half of the cut faster than the front half? Any
  two adjacent segments nearly equal length (flat rhythm)?
- Static holds: any camera-still segment >2.5s with no digital motion?
  Candidate for a `motion` field — or for trimming.
- Drag: any procedural stretch that would survive `speed: 1.25` without
  losing meaning?
- Restraint: more than 3 motion/speed touches per ~20s? Remove the
  least-motivated one. Motion on a physical camera move? Remove it.

Each finding = a concrete EDL tweak (field-level, not new cuts), then
re-render and re-check the tweaked boundaries visually. Energy tweaks
must never violate a hard rule — sequences still win over beats.

## 4. Verdict + close out

- **Pass:** note it in the release README (variant, date, checks passed).
- **Fail:** write WHY (which cut, which rule), fix the EDL, re-render,
  repeat. Max 3 rounds per variant, then discard the variant and say so.
- A variant that passes review is the ONLY thing Molly ever sees.
- Optional Tier 3 (only if asked and key present): rank passing variants
  by engagement — never use it to justify a rule violation.
