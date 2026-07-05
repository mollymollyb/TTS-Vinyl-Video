# Genmedia experiments — Jean Dawson, Glimmer of God

Ledger of AI generations for this release. Machine twin:
`genmedia.json` (same IDs). Outputs: `media/work/jean-dawson-glimmer-of-god/genmedia/`.

Seeds extracted from the 3 raw takes (NYC stoop shoot, milky-white
marble disc, black cover w/ red wordmark, liquid-chrome gatefold):
`media/derived/jean-dawson-glimmer-of-god/gen-seeds/` — cover,
gatefold, tracklist, disc_hold, disc_macro, disc_opal.

## Batch G — social-pack slate (2026-07-05)

Context threads used: chrome/liquid-metal gatefold motif (album's own
artwork), dark-fairytale register + angel-wing back-cover motif
(`knowledge/artists/jean-dawson.md`). All audio prompts instrumental
(moderation guardrail). All via `bytedance/seedance-2.0/image-to-video`.

| ID | Model | Settings | Seed | Concept | Est. cost | My read | Verdict |
|---|---|---|---|---|---|---|---|
| G1 | seedance-2.0/i2v | 4k 15s 9:16 | seed_gatefold | chrome spread ripples -> camera dives into molten-silver tunnel -> drains to spinning marble disc -> GLIMMER OF GOD / ON WAX card | ~$2.62 | STRONG. Chrome melt is hypnotic, tunnel dive lands, end card clean and on-copy. Best of slate | |
| G2 | seedance-2.0/i2v | 4k 15s 9:16 | seed_disc_hold | disc floats out of hand -> dusk fairytale sky -> light wings unfurl -> dives to turntable, needle drop -> OUT NOW ON VINYL card | ~$2.62 | FAILED audio moderation after full inference (billed). Visuals never delivered | kill |
| G2B | seedance-2.0/i2v | 4k 15s 9:16, silent | seed_disc_hold | same prompt, --generate_audio false | ~$2.62 | Wings sequence is genuinely beautiful; dusk sky + city read cinematic. Turntable room (10-12s) is a touch AI-dreamy. Needle-drop macro solid; card clean | |
| G2F | mmaudio-v2 | 15s foley | G2B | night wind + wing whoosh + needle drop, negative: all vocals | $0.02 | Foley sells it; passed moderation. NOTE: default duration=8 truncated first run | |
| G3 | seedance-2.0/i2v | 4k 15s 9:16 | seed_cover | cover floats, gatefold blows open -> chrome drips into mirror puddle on stoop -> disc rises from puddle -> LINK IN BIO card | ~$2.62 | Mercury drip + mirror puddle = scroll-stopper. Disc rising reads clean. Cover art stays on-model (real seed). End card slightly pink-shifted but legible | |
| H1 | seedance-2.0/i2v | 720p 5s 9:16 | seed_cover | cinemagraph: cover breathes, red lettering glints (composite hook fodder) | ~$0.35 | Subtle, exactly what a hook needs — real footage energy with a wrongness that stops the thumb | |
| H2 | seedance-2.0/i2v | 720p 5s 9:16 | seed_disc_opal | cinemagraph macro: opal sheen sweeps marble disc (composite hook fodder) | ~$0.35 | Opal sweep is lush; grooves sparkle without going glitter-fake | |

Slate estimate: ~$8.56 (under the ~$10 gate); actuals landed $11.20
because G2's moderation failure billed a full 4K run. Composites X1-X4
built from these — see `social-pack.md` for the full deliverable table.

## Technique notes (this release)

- **Root alias trap (cost us ~25 min, $0):** first slate went to
  `bytedance/seedance-2.0` (no sub-path). Queue accepted it, status
  said COMPLETED, but the app 404'd internally — json_output was
  `{"detail": "Path / not found"}`, no video ever existed, and every
  result route 404'd. Platform API
  (`/v1/models/requests/by-endpoint?...&expand=payloads`) confirmed
  the no-op. Resubmitted everything to the explicit
  `/image-to-video` sub-endpoint. Rule now lives in vinyl-genmedia.
- Do not POST to queue result URLs — it enqueues a NEW (empty) job.
  One stray POST auto-completed as a validation reject ($0).
