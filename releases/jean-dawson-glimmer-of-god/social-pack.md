# Social pack — Jean Dawson, Glimmer Of God (2026-07-05)

10 post-ready vertical videos (1080x1920 target; v1-v3 render at raw
4K portrait). Paths are media-plane (`media/work/jean-dawson-glimmer-of-god/`),
never in git. Suggested caption lines below; the release-level caption +
listing copy lives in `caption.md`. All drafts — Molly picks and posts.

## The pack

| # | ID | File | Len | What it is | Cost (USD) |
|---|----|------|-----|-----------|-----------|
| 1 | v1 | `2026-07-05/v1.mp4` | 25.4s | REAL full story: cover -> chrome gatefold -> pull -> held disc | 0.00 |
| 2 | v2 | `2026-07-05/v2.mp4` | 19.9s | REAL variant-first: disc cold open -> cover -> gatefold -> tracklist | 0.00 |
| 3 | v3 | `2026-07-05/v3.mp4` | 13.8s | REAL disc fancam (take 3): macro entry -> opal-flare tilt | 0.00 |
| 4 | G1 | `genmedia/G1.mp4` | 15.0s | GEN chrome portal: gatefold ripples -> molten tunnel -> disc -> ON WAX card | 2.62 |
| 5 | G2 | `genmedia/G2_final.mp4` | 15.0s | GEN angel drop: disc floats into dusk sky, light wings, needle drop -> OUT NOW card (silent gen + mmaudio foley) | 2.64 |
| 6 | G3 | `genmedia/G3.mp4` | 15.0s | GEN stoop pour: chrome drips into mirror puddle, disc rises -> LINK IN BIO card | 2.62 |
| 7 | X1 | `genmedia/X1_hook_cover_v2.mp4` | 21.9s | COMPOSITE: AI breathing-cover hook (captioned) -> full v2 real edit | 0.35 |
| 8 | X2 | `genmedia/X2_hook_disc_v3.mp4` | 15.9s | COMPOSITE: AI opal-shimmer hook -> full v3 fancam | 0.35 |
| 9 | X3 | `genmedia/X3_supercut.mp4` | 11.2s | COMPOSITE: 9-beat gen x real supercut -> generated LINK IN BIO card | 5.59* |
| 10 | X4 | `genmedia/X4_g1_tightcut.mp4` | 10.3s | COMPOSITE: G1 select cut w/ captions -> generated ON WAX card | 2.62* |

\* Composite costs are ATTRIBUTED lineage (the generations they reuse).
X3 reuses G1+G3+H2 and X4 reuses G1 — those dollars appear once in
actual spend even though three pack items lean on them.

## Suggested caption lines (voice: Molly, collector-to-collector)

1. v1 — "full package tour. the gatefold goes crazy"
2. v2 — "the wax matches the album title"
3. v3 — "just the marble wax catching sun"
4. G1 — "what living inside the gatefold feels like"
5. G2 — "this record believes in something"
6. G3 — "the artwork leaked onto the stoop"
7. X1 — "wait for the real thing"
8. X2 — "the shimmer is not an effect"
9. X3 — "glimmer of god in 15 seconds"
10. X4 — "POV: you fell into the gatefold"

## Actual fal spend (all estimated unless noted)

| Item | What | USD |
|---|---|---|
| G1 | seedance i2v 4k/15s | 2.62 |
| G2 | seedance i2v 4k/15s — FAILED audio moderation (billed) | 2.62 |
| G2B | seedance i2v 4k/15s silent rerun | 2.62 |
| G3 | seedance i2v 4k/15s | 2.62 |
| H1 | seedance i2v 720p/5s hook | 0.35 |
| H2 | seedance i2v 720p/5s hook | 0.35 |
| G2F | mmaudio foley x2 runs (8s default, then 15s) | 0.02 (exact) |
| **Total** | | **11.20** |

First slate (5 jobs to the root `bytedance/seedance-2.0` alias) no-op'd
at $0 — see genmedia-experiments.md technique notes. Seedance costs are
ESTIMATES from the Wiz benchmark (fal prices in opaque compute-seconds;
this API key can't read the usage API) — reconcile against the fal
dashboard before quoting real numbers. Twelve Labs analysis indexing
(3 proxies, ~110s video) is outside fal and untracked here.

Budget note: the ~$10 gate was set for the slate estimate ($8.56); the
$2.62 overage is entirely the G2 moderation failure.

## Human decisions open

- Confirm release type (1xLP gatefold) and the VARIANT NAME — footage
  shows marbled white/cream, retail standard is hot pink. Caption
  ships only after that's confirmed.
- Pick winners + post order (suggestion: X1 or v2 first, X3 as the
  fast-follow, G1 when the post cadence needs a spike).
- G2's wings moment is gorgeous but the turntable room at 10-12s reads
  slightly AI-dreamy — call if that's a feature or a cut.
