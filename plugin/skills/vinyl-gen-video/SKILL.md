---
name: vinyl-gen-video
description: Generate complete scroll-stopping AI videos (not just shots) with seedance-2.0 - the prompt IS a timestamped edit script. Use when the user says "make a full AI video", "gen a 15 second video", "go crazy on this release", or wants hook assets, restyles, or 30s continuation chains. Builds on vinyl-genmedia mechanics.
---

# Vinyl gen-video

Read `plugin/skills/vinyl-genmedia/SKILL.md` first (seeds, async,
ledger). This skill is the creative playbook — proven on the Cabin
Fever Trilogy batches A-F and V (winners: V1, V3, F2).

## The format that works: prompt = shot-by-shot edit script

A "full video" is scripted INSIDE one generation, as literal
timestamped beats. seedance-2.0 (non-fast, 4K, 15s) executes camera
moves, cuts, sound cues, and end-card text nearly beat-for-beat:

```
0.0-1.5s: {opening shot, camera move} 1.5-4.0s: HARD CUT to {beat 2}
... 12.0-15.0s: end cards slam on in three beats: at 12.2s 'CARD ONE',
at 13.2s 'CARD TWO', at 14.0s 'CARD THREE'. Audio: {continuous bed +
one accent per beat}. No voices, no music with lyrics.
```

Rules learned the expensive way:
- **A 15s video needs an arc**: hook (0-2s) → escalation → payoff →
  end cards. If the energy is flat after the hook, the script (not the
  model) failed.
- **End cards ≤3 words render clean at 4K**; longer floating text gets
  typos (BIIG). Long copy belongs in ffmpeg drawtext, post-gen.
- **Audio prompt**: instrumental only — chants/crowd vocals/anything
  singable risks post-inference moderation rejection (still billed).
- Default duration 15s, `--resolution 4k`, `--aspect_ratio 9:16`,
  `--generate_audio true` unless the concept is moderation-risky.

## Choosing the operation

| Want | Use | Gotcha |
|---|---|---|
| Same product, new scene/story | `reference-to-video` + 1-3 seed images (`@Image1...`) | ignores style asks; nails product consistency |
| Re-stage our real shot, then break reality | `reference-to-video` + refclip (`@Video1`) | anchors to real motion (V3 pattern) |
| No product on screen (b-roll, claymation, parody) | `t2v` | product ID only via text/end cards |
| Art-directed restyle that MOVES | two-step: `nano-banana-2/edit` restyles a real frame → seedance i2v animates the still | full art-direction control (F2 = best hook) |
| Bridge two real shots | i2v + `end_image_url` (first+last frame morph) | reads as an invisible transition (E1/X3) |

## Context threads (sometimes, not always)

Default is product-first, zero context. When a concept needs a hook,
pull **exactly 1-2 threads** from `knowledge/artists/{artist}.md`
(create it via `vinyl-artist-context` if missing) and cite which
thread in the ledger notes. Context drives CONCEPT and COPY (V6's
time-machine, V7's real tracklist cards); product VISUALS still need
reference images — scenes far from any ref invent artwork.

## Continuation chaining (30s two-parters)

15s is the per-generation cap; chain for longer arcs:

1. Extract the final frame: `ffmpeg -sseof -0.15 -i part1.mp4 -frames:v 1 -q:v 2 seed_p1_lastframe.jpg`
2. Upload; generate part 2 with it as `@Image1`, prompt opening
   "This is PART 2 of a video that ended on this exact frame, so start
   exactly there and continue: 0.0-1.5s: the scene of @Image1..."
3. Script part 2 to immediately TRANSFORM the inherited frame (burn
   the end card away, dive into the disc) so the seam reads as a beat,
   not a stall. New end cards close part 2.
4. Stitch + trim via `vinyl-gen-composite` — generations are selects,
   not finals.

## Verify + log

Preview stills → honest read → both ledgers (vinyl-genmedia §3-4).
Winners and verdicts come from the user; never mark your own Verdict
column.
