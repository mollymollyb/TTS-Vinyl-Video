# Editing rules — the philosophy every EDL must honor

Source: Molly <> Sidney call, 2026-06-29 (plus every subsequent decision
in `knowledge/decisions/`). These rules exist because the first-generation
AI edits kept failing in the same ways. When Molly gives new feedback,
fold the durable rule in here.

## Hard rules (violating any of these = the edit is unusable)

1. **Never cut inside a sequence.** A sequence is one complete event —
   pulling a vinyl from its sleeve, opening a gatefold, a pan across the
   back lettering. If the shot shows an action, the edit shows the WHOLE
   action. Cutting mid-pull or mid-pan reads as a mistake, not a style.
   (Mechanical check: `library/edl.py::check_sequence_integrity`.)
2. **Beats bend to sequences, not the other way around.** Beat-synced
   cutting is good TikTok grammar, but if finishing the sequence needs an
   extra second past the beat, extend past the beat. A rigid beat-cut that
   truncates a reveal is why edits "looked AI-edited".
3. **Drop dead space entirely.** Frames with no product being showcased
   (empty table, hands repositioning, walking) never belong in the cut.
   This includes **organizing hands inside a showcase**: re-arranging
   sleeves, tilting the product away, product half out of frame. A
   "fan-out" that dips into re-organizing mid-way is TWO showcases with
   dead space between them, not one (Cabin Fever, 2026-07-02).
4. **Respect the release's structure.** A 3xLP showing vinyls 1 → 2 → 3
   must show all three — cutting after two reads as broken (the Whiz
   Cabin Fever failure). Gatefolds must OPEN on screen, not tease and
   snap back. See `knowledge/release-types.md`.
5. **Endings are real.** Both rejected June edits died at the ending. End
   on a completed motion or a held product frame — never mid-motion, and
   never on dead space.

## Strong preferences (break only with a stated reason in the EDL notes)

- **Variant first when the variant is the seller.** Colored/splatter
  pressings often open the video (Molly's instinct on the June batch).
- **Target length scales with source**, roughly 15-45s from 1.5-3 min of
  raw. A 2.5-min 2xLP shoot lands near ~20s. Density over duration.
- **Vary the offer.** Always produce 2-3 EDL variants with genuinely
  different structure (different opener, different pacing), not the same
  cut ±1 second — Molly historically keeps 1-2 of 3.
- **Front-load the strongest visual** in the first ~1.5s (thumb-stop),
  as long as doing so breaks no hard rule.

## Motion & pacing grammar (Sidney, 2026-07-02: "feels static, a little slow")

How an editor adds energy, in priority order. Reach for tool 1 before 2,
2 before 3. Renderer support: optional per-segment `motion` and `speed`
in the EDL (`library/motion_filters.py`); caps are enforced in
validation so taste violations fail loudly.

1. **Rhythm first.** Energy comes from VARIED shot lengths, not effects.
   Open with the longest hold you'll ever show (the hook can breathe),
   then shorten: a cut that follows a 4s shot with a 1.5s shot feels
   fast without a single filter. If the back half of the cut isn't
   faster than the front half, fix that before touching motion.
2. **Digital motion (punch_in / pull_back), motivated or not at all.**
   - Motion follows meaning: punch IN toward a detail worth leaning at
     (artwork, tracklist, label on the variant); pull BACK to establish
     or to breathe before a close.
   - Only on shots where the CAMERA is basically still. Physical camera
     moves (pulls, pans, slide-outs) already have motion — digital zoom
     on top reads as drunk footage.
   - Subtle band only: 1.05–1.12 typical, 1.20 absolute cap. Eased, never
     linear (the module does this).
   - **Never every shot.** 2–3 moves per ~20s cut, alternating direction
     when two moved shots are adjacent. If every shot zooms, zoom means
     nothing — that IS the "AI edit" look.
3. **Speed (`speed`), for mechanics — never for money shots.**
   - 1.15–1.5x on procedural stretches: sliding a record back in,
     lowering/raising between showcases, long walks of a pan.
   - Money shots run 1.0x: the variant reveal, the gatefold open, any
     frame Molly would screenshot. Slowing below 1.0x is allowed for a
     peak moment but is rarely needed.
   - Never speed a shot with text the viewer is supposed to read.
4. **What we deliberately do NOT do digitally:** transition effects
   (wipes/whips/crossfades — hard cuts are the grammar of this format),
   filters/LUTs, stabilization crops. Music, captions, and stickers are
   Molly's layer, added in TikTok. Our job is a cut so strong it works
   silent.

## Working agreements

- Every EDL segment carries a `why` (which sequence it shows, why it's in).
- Every generated variant gets `vinyl-review` before Molly ever sees it.
  She reviews edits, not mistakes.
- When Molly picks a winner or rejects a cut, capture the WHY via
  `vinyl-learn` — that feedback is this file's future content.
