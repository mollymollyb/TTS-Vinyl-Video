# vinyl-os plugin

The workspace's skills, packaged in place. `plugin/skills/` is the source
of truth; `.agents/skills` symlinks here so Cursor and Codex discover the
same skills Claude does.

Pipeline skills: `vinyl-intake` (orchestrator) → `vinyl-ingest` →
`vinyl-analyze` → `vinyl-edit` → `vinyl-review` → `vinyl-caption`.

The full run: `vinyl-social-pack` — one release from raw footage to a
costed pack of post-ready videos (every one full, every one costed).
Chains the pipeline, the generative wing, and the feed-mechanics
skills; ships `releases/{slug}/social-pack.md` with a dollar figure on
every video.

Generative wing (fal.ai, works for any release): `vinyl-genmedia`
(CLI mechanics + ledger discipline) → `vinyl-gen-video` (full scripted
generations, restyles, continuation chains) → `vinyl-gen-composite`
(cut generations + real footage into finished posts) →
`vinyl-gen-meme` (meme stills, slideshows, freeze/stutter/chaos and
UI-parody formats, the gen-z caption voice). `vinyl-artist-context`
feeds them all with verified recent-arc facts per artist.

Feed mechanics: `vinyl-scrollstop` (first-frame law, pattern
interrupts, genre theft, loop engineering, comment engineering,
Molly's human-hook layer) and `vinyl-sound-design` (ASMR cuts with
generated foley, beat-grid cutting, per-pack sound maps).

Maintenance organs: `vinyl-doctor` (read-only health), `vinyl-janitor`
(reconcile + prune), `vinyl-learn` (capture Molly's feedback),
`vinyl-reflect` (improve the system), `vinyl-skillify` (promote repeated
work into skills).
