---
name: vinyl-sound-design
description: Sound-first deliverables - ASMR cuts with generated foley, beat-grid cutting, and per-video sound maps for Molly's music layer. Use when the user says "ASMR", "sound design", "sync to the music", or during any pack's viral pass. Music licensing stays on Molly's layer; we design FOR it.
---

# Vinyl sound-design — cuts that win with sound ON

Sound is the top viral lever on TikTok and the one layer we don't
ship (licensing lives with Molly's account). This skill makes the
cut sound-ready instead of sound-ignorant.

## 1. ASMR cut (one per pack)

Vinyl ASMR is a proven genre: sleeve slides, crackle, needle drops.
Recipe:
- Select 4-6 MACRO real beats (sleeve slide, gatefold open, disc
  pull, label tilt); slow to 0.85x (setpts + atempo); minimal or no
  captions after a 0.8s "SOUND ON." intro card.
- Render silent-ish, upload to fal CDN (`genmedia upload`), then
  `fal-ai/mmaudio-v2 --duration {len}` with a foley prompt: "paper
  and cardboard slides, fingertips on textured sleeve, vinyl crackle,
  soft thuds" and negative_prompt "speech, vocals, singing, music".
  mmaudio on REAL footage tracks the motion surprisingly well.
- Cost: ~$0.001/s. Log both the upload and the foley call.

## 2. Beat-grid cutting

Cut lengths in multiples of 0.5s (a 4-count at 120bpm) so ANY
120-ish track lands on the cuts when Molly aligns the downbeat.
Money shots still own their full length — the grid bends at
sequence boundaries, never through them (editing-rules law).

## 3. The sound map (ships with every pack)

`releases/{slug}/sound-map.md` — one row per deliverable:
- which track from THIS release to attach (from the artist context
  file's fan-favorite list; never invent titles),
- where to align the drop/downbeat (timestamp of the money beat),
- whether the video's own audio should duck under or stay
  (ASMR/foley cuts: keep; caption-driven cuts: duck).
BPMs are usually unknown — say "align first downbeat to 0:00, drop
at the {t}s beat" rather than fabricating tempo numbers.

## 4. Principle

Every cut still WORKS silent (captions carry it) but is DESIGNED to
win with sound on. Both must be true before a video ships.
