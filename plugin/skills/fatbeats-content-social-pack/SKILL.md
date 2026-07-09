---
name: fatbeats-content-social-pack
description: The full run - take one release from raw footage to a costed pack of ready-to-post social videos. Use when the user says "full run", "do everything for this release", "deliver the social pack", or "videos for {release}". Chains fatbeats-content-analyze, fatbeats-content-artist-context, fatbeats-content-gen-video, fatbeats-content-edit, fatbeats-content-review, fatbeats-content-gen-composite, fatbeats-content-gen-meme, fatbeats-content-scrollstop, fatbeats-content-sound-design, fatbeats-content-caption; ships releases/{slug}/social-pack.md with a dollar figure on every video.
---

# Fatbeats-content social-pack — the full run

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
- Budget gate before any fal spend: fatbeats-content-genmedia's pricing rules.

## Sequence

1. **Watch** (fatbeats-content-analyze) — every take.
2. **Research** (fatbeats-content-artist-context) — before any prompts or
   captions; product facts also sanity-check the release-type guess.
3. **Submit the gen slate** (fatbeats-content-gen-video) — generations render
   for 8-15 min, so submit the whole slate async FIRST and do the
   real edits while fal works. Log submissions immediately
   (fatbeats-content-genmedia rules).
4. **Real edits** (fatbeats-content-edit, then fatbeats-content-review until they pass).
5. **Composites** (fatbeats-content-gen-composite) — when generations land,
   verify each, then cut the composite layer.
6. **Viral pass** (fatbeats-content-scrollstop + fatbeats-content-sound-design +
   fatbeats-content-gen-meme) — nearly all $0: 2-3 scrollstop formats the pack
   doesn't already use, 1 perfect loop, 1 ASMR cut, 1 comment
   magnet, and an A/B pair (one existing asset re-hooked with a
   different first second).
7. **Captions** (fatbeats-content-caption) — post copy is per release, not per
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
