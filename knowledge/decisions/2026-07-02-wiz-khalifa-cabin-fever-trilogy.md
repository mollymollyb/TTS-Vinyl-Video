# 2026-07-02 — Cabin Fever Trilogy: organizing hands are not a showcase

## Decision

Sidney reviewed the first rendered variants and flagged that the edits
included stretches where "the hand moves over to the side and then
organizes the three looks" — the system wasn't picking the perfect
shots. Sequence map rebuilt (rev 2) from a dense 0.5-1.0s frame probe
over 34-50s and 59.5-77s; all three EDLs recut on the new map.

## Why

Two compounding causes:

1. ffmpeg scene detection under-segments continuous handheld footage,
   so 6s analysis windows spanned showcase + organizing + showcase.
2. Twelve Labs labels at that granularity averaged the window into
   "unboxing", hiding a 2.2s organizing dip (37.2-39.4s) where the box
   tilts away and leaves frame, plus a long shuffle (69.3-75.6s).

Dense probing also FOUND better material: a strong red-vinyl + sleeve-fan
showcase at 65.2-69.3s (label readable) that rev-1 had skipped, now the
fourth beat of v2.

## Rule?

Yes — two durable changes made the same day:

- `knowledge/editing-rules.md` hard rule 3 extended: organizing hands =
  dead space even mid-showcase.
- `fatbeats-content-analyze` skill now requires a dense (~1s) frame probe across
  every sequence intended for use in an edit before the map is saved.
