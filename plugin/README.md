# vinyl-os plugin

The workspace's skills, packaged in place. `plugin/skills/` is the source
of truth; `.agents/skills` symlinks here so Cursor and Codex discover the
same skills Claude does.

Pipeline skills: `fatbeats-content-intake` (orchestrator) → `fatbeats-content-ingest` →
`fatbeats-content-analyze` → `fatbeats-content-edit` → `fatbeats-content-review` → `fatbeats-content-caption`.

The full run: `fatbeats-content-social-pack` — one release from raw footage to a
costed pack of post-ready videos (every one full, every one costed).
Chains the pipeline, the generative wing, and the feed-mechanics
skills; ships `releases/{slug}/social-pack.md` with a dollar figure on
every video.

Generative wing (fal.ai, works for any release): `fatbeats-content-genmedia`
(CLI mechanics + ledger discipline) → `fatbeats-content-gen-video` (full scripted
generations, restyles, continuation chains) → `fatbeats-content-gen-composite`
(cut generations + real footage into finished posts) →
`fatbeats-content-gen-meme` (meme stills, slideshows, freeze/stutter/chaos and
UI-parody formats, the gen-z caption voice). `fatbeats-content-artist-context`
feeds them all with verified recent-arc facts per artist.

Feed mechanics: `fatbeats-content-scrollstop` (first-frame law, pattern
interrupts, genre theft, loop engineering, comment engineering,
Molly's human-hook layer) and `fatbeats-content-sound-design` (ASMR cuts with
generated foley, beat-grid cutting, per-pack sound maps).

Maintenance organs: `fatbeats-content-doctor` (read-only health), `fatbeats-content-janitor`
(reconcile + prune), `fatbeats-content-learn` (capture Molly's feedback),
`fatbeats-content-reflect` (improve the system), `fatbeats-content-skillify` (promote repeated
work into skills).
