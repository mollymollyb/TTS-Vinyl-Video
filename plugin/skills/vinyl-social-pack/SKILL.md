---
name: vinyl-social-pack
description: The full run - take one release from raw footage to a costed pack of ready-to-post social videos. Use when the user says "full run", "do everything for this release", "deliver the social pack", or "videos for {release}". Chains vinyl-analyze, vinyl-artist-context, vinyl-gen-video, vinyl-edit, vinyl-review, vinyl-gen-composite, vinyl-gen-meme, vinyl-scrollstop, vinyl-sound-design, vinyl-caption; ships releases/{slug}/social-pack.md with a dollar figure on every video.
---

# Vinyl social-pack — the full run

Footage in, a costed pack of post-ready videos out. This skill
sequences the other skills and owns the deliverable contract; every
mechanic lives in the skill each stage points to — stated once, there.

## The contract

- Every deliverable is a FULL video: ≥13s with hook → hold → payoff.
  Hooks are ingredients, not deliverables.
- The pack covers several distinct mechanics — real edits, scripted
  generations, meme formats, feed-mechanics formats. Rebalance to
  what the footage gives and say so in the manifest.
- Every video is costed from the ledger and verified on disk before
  it appears in the manifest.
- Budget gate before any fal spend: vinyl-genmedia's pricing rules.

## Sequence

1. **Watch** (vinyl-analyze) — every take.
2. **Research** (vinyl-artist-context) — before any prompts or
   captions; product facts also sanity-check the release-type guess.
3. **Submit the gen slate** (vinyl-gen-video) — generations render
   for 8-15 min, so submit the whole slate async FIRST and do the
   real edits while fal works. Log submissions immediately
   (vinyl-genmedia rules).
4. **Real edits** (vinyl-edit, then vinyl-review until they pass).
5. **Composites** (vinyl-gen-composite) — when generations land,
   verify each, then cut the composite layer.
6. **Viral pass** (vinyl-scrollstop + vinyl-sound-design +
   vinyl-gen-meme) — nearly all $0: 2-3 scrollstop formats the pack
   doesn't already use, 1 perfect loop, 1 ASMR cut, 1 comment
   magnet, and an A/B pair (one existing asset re-hooked with a
   different first second).
7. **Captions** (vinyl-caption) — post copy is per release, not per
   video.

## The manifest (releases/{slug}/social-pack.md)

- One row per video: id, file (media-plane path), duration, what it
  is (one line), suggested caption line, **cost_usd** from
  `genmedia_ledger` rollups — $0.00 for pure-real cuts, "unknown"
  only when a lineage cost is unknown, never guessed.
- Pack total + `summary --release {slug}` output included.
- Every listed file verified with ffprobe (exists, duration matches).
- Ships with `sound-map.md` (music alignment per video) and
  `molly-hooks.md` (5-6 selfie cold-open scripts).

## Ship

Ledger `validate`; release README, `_board.md`, dashboard,
`project-overview.md` updated; commit + push (media stays out of
git). Report: pack table, total spend, and the open human decisions
(type confirmation, winner picks, post order).
