# Improvements ledger (vinyl-reflect)

Dated entries: friction observed → change made → how we'll know it worked.

## 2026-07-02 — system born

- Vendored auto-edit's proven pieces (scene detection, Twelve Labs shot
  labeling, EDL concat rendering) into single-purpose `library/` modules;
  fixed the SDK drift (`ResponseFormat` → `SyncResponseFormat`, native
  `start_time`/`end_time` scoping on analyze calls).
- Inverted the auto-edit optimization philosophy: sequence integrity is
  the hard constraint, engagement is Tier 3 tiebreak only — because the
  spike proved engagement-maximizing edits go incoherent.
