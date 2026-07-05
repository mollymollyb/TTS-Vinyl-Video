# vinyl-os plugin

The workspace's skills, packaged in place. `plugin/skills/` is the source
of truth; `.agents/skills` symlinks here so Cursor and Codex discover the
same skills Claude does.

Pipeline skills: `vinyl-intake` (orchestrator) → `vinyl-ingest` →
`vinyl-analyze` → `vinyl-edit` → `vinyl-review` → `vinyl-caption`.

The full run: `vinyl-social-pack` — one release from raw footage to a
costed pack of ~10 post-ready videos. Chains the pipeline AND the
generative wing, ships `releases/{slug}/social-pack.md` with a dollar
figure on every video.

Generative wing (fal.ai, works for any release): `vinyl-genmedia`
(CLI mechanics + ledger discipline) → `vinyl-gen-video` (full scripted
generations, restyles, continuation chains) → `vinyl-gen-composite`
(cut generations + real footage into finished posts). `vinyl-artist-context`
feeds both with verified recent-arc facts per artist.

Maintenance organs: `vinyl-doctor` (read-only health), `vinyl-janitor`
(reconcile + prune), `vinyl-learn` (capture Molly's feedback),
`vinyl-reflect` (improve the system), `vinyl-skillify` (promote repeated
work into skills).
