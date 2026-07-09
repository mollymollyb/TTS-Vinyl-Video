---
name: fatbeats-content-edit
description: Generate 2-3 edit variants (EDLs) for an analyzed release and render them as drafts. Use when the user says "edit this release", "make the cuts", "generate variants", or after fatbeats-content-analyze completes. Requires releases/{slug}/analysis.json with sequences filled in.
---

# Fatbeats-content edit

Read FIRST, every time: `knowledge/editing-rules.md`,
`knowledge/release-types.md`, and the release's `analysis.json`.

## 1. Design 2-3 EDLs

Each variant is `releases/{slug}/edits/v{N}.edl.json`:

```json
{"release": "{slug}", "source": "Exact Raw File.MOV", "version": 1,
 "notes": "structure rationale",
 "segments": [{"start": 41.2, "end": 48.9, "why": "seq-03 vinyl-pull disc 2"}]}
```

Constraints (the hard rules, mechanically checkable):
- Segment boundaries only at sequence boundaries (±0.25s), inside
  dead-space, or fully containing a sequence — never inside one.
- No dead-space content in any segment.
- Release-type structure honored (all discs of a 2x/3xLP; gatefold opens
  fully). Target length per `knowledge/release-types.md`.
- End on a completed motion or held product frame.
- Variants must differ structurally (different opener / arc / pacing),
  e.g. v1 chronological, v2 variant-reveal-first, v3 fastest-paced.
- Every segment has a `why` naming its sequence id.

Energy (the "Motion & pacing grammar" in editing-rules.md, in order):
1. Shape rhythm with shot lengths — back half faster than front half.
2. Optionally add `"motion": {"type": "punch_in"|"pull_back", "amount": 1.05-1.12}`
   to CAMERA-STILL holds only (2-3 per cut, max), motivated by a detail.
   Never on segments whose `why` names a pull/pan/slide sequence.
3. Optionally add `"speed": 1.15-1.5` to procedural stretches; money
   shots stay 1.0. Validation caps both fields and fails loudly.

## 2. Validate + render

For each variant:
`.venv/bin/python -m library.edl_render releases/{slug}/edits/v{N}.edl.json`
— validation runs inside the renderer and fails loudly; fix the EDL, not
the validator. Renders land in the media `work/{slug}/{date}/` folder.

## 3. Close out

Status → `editing`, then hand every render to `fatbeats-content-review`. Update the
release README + board + dashboard in the same turn. EDLs are committed;
renders are never committed.
