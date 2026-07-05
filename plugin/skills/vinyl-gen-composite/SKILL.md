---
name: vinyl-gen-composite
description: Cut AI generations and real footage into finished platform-ready posts with ffmpeg - hook-then-real edits, supercuts, trims, caption passes, and two-parter stitches. Use when the user says "make the composite", "supercut", "trim and caption these", "cut this like a gen-z editor", or after vinyl-gen-video produces raw generations.
---

# Vinyl gen-composite

> Meme-format recipes (freeze-frame reaction, stutter repeat, chaos
> edit, ken-burns meme slideshow, rapid-fire text) live in
> `vinyl-gen-meme` — same normalization contract as here.

Generations are SELECTS, not finals. This skill is the edit bay:
everything here is plain ffmpeg on the media plane, logged as a
`finals` record via `library.genmedia_ledger add-final`.

## The normalization contract (why concat works)

Every piece — AI or real, any resolution — becomes 1080x1920@30fps,
aac 48k stereo, BEFORE concat:

```
scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1
```

Then `ffmpeg -f concat -safe 0 -i list.txt -c:v libx264 -crf 19 -c:a aac`.
Mono real-footage audio: `pan=stereo|c0=c0|c1=c0`. 4K sources survive
punch-ins without softening — crop AFTER scaling by the zoom factor.

## Recipes (all proven, IDs from Cabin Fever)

- **Hook + real edit (X1/X2)**: strongest 2-3s of an AI generation,
  one Impact caption, HARD CUT into an approved real cut (v2/v3).
  The AI hook buys the scroll-stop; the real edit sells the product.
- **Invisible transition (X3)**: real shot → first+last-frame morph
  generation → real shot. AI as connective tissue, not spectacle.
- **Supercut (X4)**: 12-16 beats x ~1.1s alternating AI/real, caption
  per beat carrying one running joke, punch-in jump cuts (zoom 1.08-
  1.14 on alternating beats), one 0.85x slow-mo money shot. Cutting
  this fast hides AI imperfections and reads as intentional style.
- **Select cut**: a 15s generation keeps its best ~10-12s — trim the
  weakest stretch (usually mid-video wander; find it by Reading probe
  frames every 2s), keep generated end cards, caption beats that lack
  generated text.
- **Two-parter stitch**: part1 + continuation (vinyl-gen-video
  chaining) trimmed at the transform seam so the dive/burn lands as
  one motion. Target 22-28s, not the raw 30.

## Captions

Impact (`/System/Library/Fonts/Supplemental/Impact.ttf`), fontsize
~72 (84 for closers), white, borderw=7-8 black, x centered, y=h*0.13.
Escape drawtext text (`' : , /`). One idea per caption, lowercase
gen-z register, caps for the punch words. Never caption over
generated end-card text.

## Speed + motion inside a beat

`setpts={1/speed}*PTS` + `atempo={speed}` (audio stays synced);
0.85x on ONE money shot per composite, 1.15-1.3x on procedural
stretches. Zoom punch-in per beat: scale to `1080*zoom` wide then
center-crop 1080x1920.

## Close out

Preview stills of the seams + first/last frame; watch duration vs
target (17-28s posts). `add-final` with every component listed
(`generation_id` per AI piece, `raw_footage` refs with seconds) so
cost rollup stays queryable. Update `genmedia-experiments.md` batch X
table. Finals stay on the media plane; only the ledgers enter git.
