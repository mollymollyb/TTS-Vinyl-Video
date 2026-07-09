---
name: fatbeats-content-scrollstop
description: Feed-mechanics playbook - stop the scroll in the first second, hold attention to the end, engineer rewatch and comments. Use when the user says "stop the scroll", "make it viral", "hold attention", or when building any pack's viral pass. Owns first-frame law, pattern interrupts, genre theft, UI parody, loop engineering, and comment engineering.
---

# Fatbeats-content scrollstop — the feed is the medium

A better video is not the same as a video the feed rewards. The feed
rewards: stopped thumbs (first 0.6s), watch-through (arc + withheld
payoff), rewatch (loops), and replies (arguments, questions,
mysteries). Design for those four explicitly.

## First-frame law

Frame 0 is both the thumb-stopper AND the profile-grid thumbnail.
Every deliverable opens on one of:
- **A readable claim** (black card, one line, ≤7 words: "what $30 of
  divinity looks like") — 0.6-0.8s then SLAM into content. The black
  frame reads as "video broke" = interrupt.
- **An unresolvable image** — extreme macro or mid-action frame the
  eye can't classify in 300ms ("is that marble? milk? a moon?").
  Resolution of the ambiguity IS the hold.
- **An interface** (see UI parody) — feeds train thumbs to respond
  to UI chrome.
Never open on a slow establishing shot; the feed already established.

## Pattern interrupts (proven set — pick ONE per video)

1. **Black-slam**: black + claim -> hard cut into the money shot.
2. **Unresolvable macro**: 2x crop of 4K footage = free macro; open
   abstract, pull back to reveal.
3. **Genre theft**: steal a genre's opening grammar (nature doc
   captions, crime-scene evidence board, cooking show, Apple ad).
   The stolen grammar is a pre-trained attention pattern; the swap
   to vinyl is the joke.
4. **UI parody**: captcha grids, dating-app profiles, system alerts,
   fake pinned comments. Build UI chrome with PIL (pixel-exact),
   animate with ffmpeg. Screenshot-able = share-able.
5. **4th-wall**: text that references the scroll itself ("you've
   scrolled past this 3 times").
6. **Fake beef**: pinned "hater" comment (generic invented username
   only, never a real user) -> the video is the rebuttal. Drives
   real comments taking sides.

## Hold mechanics

- **Withhold the payoff**: name it, delay it ("wait for the inside").
- **Mini-payoff chain**: a payoff every 2-3s, each raising the next
  ("and THEN"). M1-style.
- **Countdown**: visible "3...2...1" makes leaving feel like quitting.
- **Serialize**: 30s two-parters post as pt.1 (cliffhanger cut) +
  pt.2 next day. Follows come from unfinished stories.

## Rewatch engineering (loops)

- **Palindrome loop** ($0): clip A + reversed A. Zoom-out then
  zoom-back = seamless by construction. 6-10s max.
- **Generated loop**: seedance i2v with `--image_url X
  --end_image_url X` (SAME image both ends) forces first frame =
  last frame. Script an orbit/day-night cycle between them. 10s,
  1080p is enough — loops win on rewatch, not resolution.
- Loop captions go mid-video, never on the seam frames.

## Comment engineering

Captions ship as questions, hot takes, or mysteries — never
statements: "wrong answers only", "track 7 is the best and it's not
close", "if you know what pressing this is, comment". A real unknown
(unconfirmed variant) is the best comment magnet — ask the audience
honestly.

## A/B discipline

Every pack cuts at least one asset two ways (different first second,
same body). Two hooks on one render = free experiment; log both in
the manifest and let posting data pick.

## Human layer (Molly)

Faceless caps out. Ship `releases/{slug}/molly-hooks.md`: 5-6
two-second selfie hook scripts (exact line, exact video it splices
onto). Her 10 minutes of filming converts brand content into person
content — splice cold opens via fatbeats-content-gen-composite.
