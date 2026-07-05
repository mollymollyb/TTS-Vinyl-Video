# Improvements ledger (vinyl-reflect)

Dated entries: friction observed → change made → how we'll know it worked.

## 2026-07-05 — generative wing promoted to skills

- Friction: three days of fal.ai experimentation (batches A–F, V, X on
  Cabin Fever) lived only in one release's `genmedia-experiments.md` —
  unusable for the Mac Miller / Jeezy / Jean Dawson releases without
  re-derivation.
- Change: promoted the proven patterns into four modular skills —
  `vinyl-genmedia` (mechanics + ledger), `vinyl-gen-video` (scripted
  15s generations, chaining), `vinyl-gen-composite` (AI+real cutting
  recipes), `vinyl-artist-context` (recent-arc research files). CLAUDE.md
  routes gen work through them.
- Provenance (per vinyl-skillify's 2+ rule): every recipe ran ≥2 real
  times (two-step pipeline F1–F3; scripted videos V1–V7; composites
  X1–X6; context files/threads wiz ×3 uses).
- We'll know it worked when the next release's gen batch starts from
  the skills and its first batch quality matches Cabin Fever round 3.

## 2026-07-02 — system born

- Vendored auto-edit's proven pieces (scene detection, Twelve Labs shot
  labeling, EDL concat rendering) into single-purpose `library/` modules;
  fixed the SDK drift (`ResponseFormat` → `SyncResponseFormat`, native
  `start_time`/`end_time` scoping on analyze calls).
- Inverted the auto-edit optimization philosophy: sequence integrity is
  the hard constraint, engagement is Tier 3 tiebreak only — because the
  spike proved engagement-maximizing edits go incoherent.
