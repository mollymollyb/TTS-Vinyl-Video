"""Vinyl video editor library — single-purpose modules, no cross-cutting state.

Run modules from the repo root, e.g.:

    python3 -m library.ingest --all
    python3 -m library.analyze --release wiz-khalifa-cabin-fever-trilogy
    python3 -m library.edl_render releases/<slug>/edits/v1.edl.json

Every module resolves media byte paths through `media_paths` (backed by
media.config.json) and secrets through `env_config` (backed by .env).
Portions are adapted from sidney/labs/auto-edit (Sidney Swift, 2026).
"""
