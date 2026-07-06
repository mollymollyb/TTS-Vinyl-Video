# Improvements ledger (vinyl-reflect)

Dated entries: friction observed → change made → how we'll know it worked.

## 2026-07-06 — orchestrator deslop: one rule, one home

- Friction: vinyl-social-pack (100 lines) restated mechanics its
  sub-skills already own — the ~$10 budget gate (vinyl-genmedia), the
  3-round discard rule (vinyl-review), dense-probing (vinyl-analyze),
  end-card captioning (vinyl-gen-composite), the loop trick
  (vinyl-scrollstop) — five rules with two homes each, plus a numeric
  pack mix ("3 real edits, 3-4 gens, 2-3 memes...") that had already
  drifted from reality (pack v3's best-value layer wasn't in it).
- Change: rewrote the orchestrator to ~60 lines — contract (full
  videos, multi-mechanic coverage, ledger-costed, disk-verified),
  sequence with the async-first insight, per-stage pointers with zero
  embedded mechanics, manifest + ship contracts. Multi-take rule
  moved to its rightful owner (vinyl-analyze, which owns --take N).
  Numeric mix replaced with the principle (cover distinct mechanics,
  rebalance to the footage, say so in the manifest).
- We'll know it worked when a sub-skill rule changes and no stale
  copy in the orchestrator contradicts it.

## 2026-07-06 — round 3: feed mechanics (the viral pass)

- Friction: rounds 1-2 made better VIDEOS; virality lives in feed
  mechanics (stopped thumbs, rewatch, replies) which nothing owned.
- Change: (1) new `vinyl-scrollstop` skill — first-frame law, pattern
  interrupts (black-slam, unresolvable macro, genre theft, UI parody,
  4th-wall, fake beef), loop engineering, comment engineering, A/B
  hook discipline, molly-hooks.md contract. (2) New
  `vinyl-sound-design` skill — ASMR via mmaudio foley on REAL footage
  (proven, $0.01), beat-grid cutting, per-pack sound-map.md. (3)
  `vinyl-gen-meme` gained PIL UI-parody formats (captcha, dating
  profile, fake comment — pixel-exact chrome, ffmpeg animates). (4)
  `vinyl-social-pack` gained stage 5b (viral pass). (5) Proved the
  perfect-loop trick: seedance `image_url == end_image_url`
  guarantees first frame = last frame ($0.44 at 1080p/10s).
- Result: pack v3 = 26 videos; the 9-video viral pass cost $0.45
  total. Docs shipped: sound-map.md, molly-hooks.md.
- We'll know it worked when the A/B pair (G1 vs S5 black-slam) gets
  posted and hold-rate data picks a winner, and when comments arrive
  on S6 (variant mystery asks the audience a real question).

## 2026-07-05 — round 2: the pack quality bar + meme wing

- Friction: first Jean Dawson pack read "mid" — only a couple of FULL
  videos; hooks and short composites padded the count. The pack shape
  optimized for quantity, not attention.
- Change: (1) new quality bar — a deliverable is a FULL video (≥13s,
  hook → hold → payoff); hooks are ingredients. (2) New
  `vinyl-gen-meme` skill: meme stills, ken-burns slideshows,
  freeze-frame reactions, stutter repeats, chaos edits, rapid-fire
  text, and the caption voice rules. (3) vinyl-gen-video gained the
  proven arc patterns (portal, brainrot escalation, motif animation,
  ascension). (4) Confirmed moderation pattern: celestial audio
  descriptors fail (2/2); divine concepts generate silent + mmaudio.
- Result: pack v2 = 17 videos, 14 full, $22.00 total, including a 30s
  two-parter (J1X), a comedy generation (J2), and 4 meme edits from
  $0 of new inference.
- We'll know it worked when Molly's picks skew toward the new formats
  and the next release's pack starts from vinyl-gen-meme instead of
  improvising.

## 2026-07-05 — the full run, proven on Jean Dawson

- Friction: "make everything for this release" had no single entry
  point — intake covered real edits only, gen wing was separate, and no
  deliverable contract tied videos to dollars.
- Change: new `vinyl-social-pack` orchestrator skill (raw footage →
  ~10 post-ready videos + costed `social-pack.md` manifest). First run:
  jean-dawson-glimmer-of-god — 10 videos, $11.20 fal spend, one session.
- Walls hit → fixes shipped the same run: (1) `library/analyze.py`
  overwrote analysis.json per take — now writes `analysis-takeN.json`
  siblings; (2) genmedia root-alias submissions silently no-op — rule +
  post-mortem recipe added to vinyl-genmedia; (3) mmaudio default
  duration=8 truncates videos — flag documented; (4) `--download=path`
  template no-ops — bare `--download` + rename documented.
- We'll know it worked when the next release's full run needs zero new
  improvisation and lands within its slate estimate.

## 2026-07-05 — generative wing promoted to skills

- Friction: three days of fal.ai experimentation (batches A–F, V, X on
  Cabin Fever) lived only in one release's `genmedia-experiments.md` —
  unusable for the Mac Miller / Jeezy / Jean Dawson releases without
  re-derivation.
- Change: promoted the proven patterns into four modular skills —
  `vinyl-genmedia` (mechanics + ledger), `vinyl-gen-video` (scripted
  15s generations, chaining), `vinyl-gen-composite` (AI+real cutting
  recipes), `vinyl-artist-context` (recent-arc research files). CLAUDE.md
  routes gen work through them.
- Provenance (per vinyl-skillify's 2+ rule): every recipe ran ≥2 real
  times (two-step pipeline F1–F3; scripted videos V1–V7; composites
  X1–X6; context files/threads wiz ×3 uses).
- We'll know it worked when the next release's gen batch starts from
  the skills and its first batch quality matches Cabin Fever round 3.

## 2026-07-02 — system born

- Vendored auto-edit's proven pieces (scene detection, Twelve Labs shot
  labeling, EDL concat rendering) into single-purpose `library/` modules;
  fixed the SDK drift (`ResponseFormat` → `SyncResponseFormat`, native
  `start_time`/`end_time` scoping on analyze calls).
- Inverted the auto-edit optimization philosophy: sequence integrity is
  the hard constraint, engagement is Tier 3 tiebreak only — because the
  spike proved engagement-maximizing edits go incoherent.
