# Wiz Khalifa — Cabin Fever Trilogy

- **Status:** review (v1–v3 rendered and self-review PASSED — awaiting Molly's pick)
- **Release type:** 3xLP box set (footage-confirmed: CF1/CF2/CF3 sleeves
  + red translucent variant vinyl; Molly confirms commercial details)

## Raw takes

- take 1: `Wiz Khalifa - Cabin Fever Trilogy.MOV` — 81.6s, 3840x2160 @ 29.97fps, 444.2MB

## Analysis

- 14 shots; sequence map **rev 2**: 23 sequences (6 atomic never-cut
  events, 6 dead-space). Tier 2 (Twelve Labs) + agent dense-probe pass
  (~80 frames reviewed at 0.5–1s spacing over the showcase regions).
- Key beats: FAN 1 at 35.0–37.2s · FAN 2 at 39.4–40.8s · CF2/CF3 sleeve
  swaps 42.4–49.0s · red vinyl pull 53.2–59.8s · red + fan showcase
  65.2–69.3s · slide-out closer 75.6–80.6s.
- Rev 2 exists because Sidney caught organizing-hands stretches inside
  the rev-1 "fan-out" — see `knowledge/decisions/2026-07-02-...md`.

## Edit variants (rev 3 EDLs on the rev-2 map + approved motion pass)

| Variant | Length | Structure |
|---|---|---|
| v1 | 24.5s | chronological: cover (punch-in) → tracklists → FAN 1 → swap run (1.15x) → red pull finale (1.0x) |
| v2 | 21.2s | variant-first: red pull opener (1.15x) → cover (punch-in) → FAN 2 (pull-back) → red+fan showcase (punch-in) → slide-out closer |
| v3 | 16.2s | fastest: cover flash (punch-in) → back flip → FAN 1 hold → CF3 claw swap → red pull (1.15x) |

Renders: media `work/wiz-khalifa-cabin-fever-trilogy/2026-07-02/`. The
`v2-motion` demo file was folded into v2 after Sidney approved the
toolkit (see `knowledge/decisions/2026-07-02-motion-toolkit-approved.md`).

## Generative experiments (2026-07-03 → 07-05, four rounds)

36 AI artifacts via genmedia/fal: round 1 shots/restyles/composites,
round 2 full 4K/15s scripted videos + the X4 supercut, round 3
context-loaded videos driven by `knowledge/artists/wiz-khalifa.md`,
round 4 the favorites finished — V1B continuation chain, X5 (V1+V1B
24.5s two-parter), X6 (V3 11.9s select cut). Ledger with prompts +
verdict slots: `genmedia-experiments.md`; spend records:
`genmedia.json`; outputs in media
`work/wiz-khalifa-cabin-fever-trilogy/genmedia/`. Sidney so far:
**V1 and V3 are the favorites** → both now have finished cuts.
The whole playbook is promoted to reusable skills: `vinyl-genmedia`,
`vinyl-gen-video`, `vinyl-gen-composite`, `vinyl-artist-context`.

## Review log

| Date | Variant | Verdict | Notes |
|---|---|---|---|
| 2026-07-02 | v1–v3 r1 | integrity PASS, visual FAIL | first frame half-framed; v1/v3 endings past reveal peak |
| 2026-07-02 | v1–v3 r2 | starts fixed, endings still weak | endings landed on sleeve shuffle |
| 2026-07-02 | v1–v3 r3 | visual PASS on rev-1 map | Sidney then flagged organizing-hands inside the fan-out |
| 2026-07-02 | map rev 2 + EDL rev 3 | re-analyzed + recut | dip 37.2–39.4 excised; red+fan showcase added to v2 |
| 2026-07-02 | v1–v3 r4 | PASS | all cuts land on motion-complete frames; v2 closer trimmed to 80.6; 0 violations |
| 2026-07-02 | v2-motion demo | approved | Sidney: "the effect was cool" — toolkit graduates to grammar |
| 2026-07-02 | v1–v3 r5 (motion pass) | **PASS** | punch/pull framings clean, sped cuts land per speed-aware math, portrait verified, 0 violations |

## Decisions

(awaiting Molly's pick — capture via vinyl-learn)
