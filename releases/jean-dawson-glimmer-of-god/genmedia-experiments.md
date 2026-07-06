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

## Batch J — "MORE and BETTER" round (2026-07-05, after Sidney's mid verdict)

Feedback driving this round: pack was "mid", only 2 full videos, rest
too quick — edit like a gen-z: grab attention, hold attention, memes.

| ID | Model | Settings | Seed | Concept | Est. cost | My read | Verdict |
|---|---|---|---|---|---|---|---|
| J1 | seedance-2.0/i2v | 4k 15s | seed_g1_lastframe | PT.2 chain: G1's card burns, disc splits open like doors -> chrome record-cathedral flythrough -> stage-size turntable needle drop -> COP THE VINYL | ~$2.62 | Cathedral is jaw-dropping — pillars are stacks of records, altar turntable lands. Chain seam reads as a beat. Best generation on this release | |
| J2 | seedance-2.0/i2v | 4k 15s | seed_disc_macro | brainrot: disc pops into dozens raining down the stoop, bus splashes through, tower stack -> OK ONE IS ENOUGH | ~$2.62 | Genuinely funny. Multiplication reads clean, bus beat lands, tower wobble sells it. Comedy audio (pops/clinks) PASSED moderation | |
| J3 | seedance-2.0/i2v | 4k 15s | seed_tracklist | calligraphy lifts off sleeve, spells DARLIN/BLACK SUGAR/HOUSTON in 3D, wing-beat spark blast, tracklist rewrites -> 15 TRACKS NO SKIPS | ~$2.62 | FAILED audio moderation ("shimmering chimes"). 2nd celestial-audio fail — pattern confirmed | kill |
| J3B | seedance-2.0/i2v | 4k 15s silent | seed_tracklist | same, --generate_audio false | ~$2.62 | Letters lift and spell the real track names legibly; wing beat + spark rain deliver; card clean | |
| J3F | mmaudio-v2 | 15s foley | J3B | bells/whoosh/spark rain/pen scratch | $0.02 | Passed. J3_final.mp4 is the deliverable | |

## Batch N — divine meme stills (nano-banana-2/edit, ~$0.05 ea)

All six landed on-model and genuinely funny-beautiful: N1 renaissance
angel statue holding the disc (halo god-rays), N2 disc as full moon
over the same street, N3 cover on a Times Square billboard w/ crowd,
N4 cherub sitting on the chrome gatefold in a museum, N5 disc in a
fresco cloudscape w/ doves, N6 cover as stained glass casting light.
Divine register = the album's own theme; memes stay brand-true.

## Batch L + S — the viral pass (2026-07-06)

Feedback: "think deeper. more different. stop the scroll." Round 3 is
feed mechanics, not better videos — 9 formats, $0.45 total.

| ID | Model | Settings | Seed | Concept | Est. cost | My read | Verdict |
|---|---|---|---|---|---|---|---|
| L1 | seedance-2.0/i2v | 1080p 10s silent | seed_disc_hold x2 | PERFECT LOOP: `image_url == end_image_url` forces first frame = last frame; 360 orbit + sunset->night->sunrise between them | $0.44 | The trick WORKS — day-night cycle lands, streetlights glow at night (t7.5 is beautiful), t0.05 and t9.9 frames match. Loop verified on the sheet | keep |
| ASMR1F | mmaudio-v2 | 14s foley | ASMR1_silent (REAL footage) | cardboard slides, fingertip brushes, crackle, thuds; negative vocals/music | $0.01 | First mmaudio-on-real-footage: tracks the motion well. ASMR cut shippable | keep |

S1-S6 + P1 are $0 ffmpeg/PIL builds (captcha, dating profile, comment
rebuttal, nature doc, black-slam A/B, variant mystery, palindrome
loop) — see finals in `genmedia.json`.

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
- **Celestial audio descriptors fail moderation reliably** ("ambient
  synth swell" G2, "shimmering chimes" J3 — both billed). Divine/
  dreamy concepts: generate silent by default, mmaudio after
  (`--duration {len}` — default 8 truncates). Comedic/mechanical
  audio (pops, clinks, bus rumble, booms) passes.
- Meme grammar that worked in composites: 1 freeze + 1 stutter max
  per video, every beat captioned, back half faster, generated end
  cards never captioned over. Formats promoted to `vinyl-gen-meme`.
- **Perfect-loop trick proven:** seedance i2v accepts the SAME image
  as `--image_url` and `--end_image_url` — guaranteed seamless loop,
  script the journey between (orbit + day-night cycle). 1080p/10s is
  the right spec for loops ($0.44 vs $2.62; rewatch beats resolution).
  Promoted to `vinyl-scrollstop`.
- **PIL for UI chrome** (captcha, dating cards, comment bubbles) —
  pixel-exact interfaces beat ffmpeg drawbox approximations; ffmpeg
  then animates the PNGs. Promoted to `vinyl-gen-meme`.
- **mmaudio on REAL footage works** — foley tracks handling motion,
  not just generated video. The ASMR format is $0.01 per pack.
  Promoted to `vinyl-sound-design`.
