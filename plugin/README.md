# vinyl-os plugin

The workspace's skills, packaged in place. `plugin/skills/` is the source
of truth; `.agents/skills` symlinks here so Cursor and Codex discover the
same skills Claude does.

Pipeline skills: `vinyl-intake` (orchestrator) → `vinyl-ingest` →
`vinyl-analyze` → `vinyl-edit` → `vinyl-review` → `vinyl-caption`.

Maintenance organs: `vinyl-doctor` (read-only health), `vinyl-janitor`
(reconcile + prune), `vinyl-learn` (capture Molly's feedback),
`vinyl-reflect` (improve the system), `vinyl-skillify` (promote repeated
work into skills).
