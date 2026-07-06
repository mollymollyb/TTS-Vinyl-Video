---
name: vinyl-gen-meme
description: Make meme-format vinyl content - meme stills via nano-banana, ken-burns meme slideshows, freeze-frame reaction edits, stutter repeats, chaos edits, and rapid-fire text formats. Use when the user says "make memes", "gen-z edit", "brainrot", "make it funny", or when a social pack needs attention-grab formats beyond straight showcases. Voice rules included - the meme IS the caption.
---

# Vinyl gen-meme — grab attention, hold attention

Meme formats sell vinyl because they're shareable BEFORE they're ads.
The product stays the punchline's proof. Everything renders 1080x1920
via the vinyl-gen-composite normalization contract.

## Voice (the caption IS the meme)

- Lowercase confidence, period endings: "manifesting." / "told you."
- ALL-CAPS only for the beat's peak word: "THE MARBLE." / "HELLO???"
- Collector-brain humor: cost-per-listen math, "one of one (basically)",
  shelf-space denial, "no skips. literally."
- Tie jokes to the ALBUM's own iconography (for Glimmer of God:
  divine/renaissance register - "biblically accurate pressing",
  "heaven has a listening party"). Album theme -> meme theme; check
  `knowledge/artists/{artist}.md` for the register.
- Never punch down at the artist or fans. The product is always the
  flex, never the joke's victim.

## Format 1 — Meme stills (nano-banana-2/edit, ~$0.05 each)

Seed = REAL footage still (product stays on-model). Prompt pattern:
"[absurd/elevated scenario], keep the record/cover EXACTLY
recognizable, vertical composition." Proven scenarios: renaissance
statue holding the disc; disc as full moon over the shoot location;
cover on a Times Square billboard; cherub on the gatefold in a museum;
disc in a fresco cloudscape; cover as stained glass. Submit the batch
async; stills complete in ~30s. Caption text goes ON via drawtext,
NOT in the generation prompt (AI text renders gibberish).

## Format 2 — Meme slideshow (photo-dump video, ~13s, $0.30)

`intro real beat (sets premise) -> 6 ken-burns meme cards @1.8s
(alternate zoom in/out) -> real outro beat ("anyway its out now")`.
Ken burns: `zoompan` 1.0->1.10 over the card, 30fps, silent audio bed
(`anullsrc`). One caption per card, top-center, Impact 56.

## Format 3 — Freeze-frame reaction (~15-20s, $0)

Real footage plays -> hard FREEZE on the money frame + big caption
("HOLD ON.") -> resume with commentary captions. Freeze = extract the
frame, loop it `-loop 1 -t {dur}` with `anullsrc` audio. The silence
IS the record-scratch. 1 freeze per video, 2 max.

## Format 4 — Stutter repeat ("HELLO???")

Slice 0.3-0.4s at the peak, concat x3 with the caption on every
repeat. Use ONCE per video, on the single most absurd beat (gatefold
chrome hit, variant reveal). More than once = noise.

## Format 5 — Chaos edit (~16-19s, $0)

The gen-z supercut: 9-11 beats, every beat captioned, speed-ramped
procedural stretches (1.15-1.6x), 1 freeze + 1 stutter allowed, money
shots at 1.0x, end card. Rhythm rule still applies: back half faster.
Sequence integrity still applies: show whole actions or don't show
them (cut AROUND, never INSIDE - the analysis sequence map is law
even in memes).

## Format 7 — UI parody (PIL + ffmpeg, $0)

Feeds train thumbs to respond to interfaces — a fake UI is the
strongest $0 scroll-stop we have. Build chrome with PIL (pixel-exact
cards saved as PNG), animate states with ffmpeg stills + real-footage
beats. Proven: **captcha** ("select all squares with a divine object"
— all 9 tiles are the product; 3 states: empty / checked / "9/9
correct"), **dating profile** (product as the profile; bio lines =
the specs; LIKE stamp; match screen), **fake pinned comment** (an
invented-username hater comment the video rebuts — never use a real
username). End on a real product beat + card so the joke converts.
Screenshot-ability is the point: shares > likes.

## Format 6 — Rapid-fire text (~14s, $0)

One claim proven N times: every track title flashed in pairs over
1.4s beats cycling through showcases, ending "15 TRACKS / NO SKIPS."
Pattern generalizes: pressing specs, colorways, "things in this box".

## Ledger + verify

Meme stills are generations (batch letter N) - log via
`genmedia_ledger` like any fal call. Composites log as finals with
their still lineage. Verify per vinyl-genmedia: preview stills, Read
them, honest notes. End cards: drawtext black card via lavfi color -
NEVER caption over a generated end card.
