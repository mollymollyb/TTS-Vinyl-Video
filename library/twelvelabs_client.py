"""twelvelabs_client.py — the ONLY module that talks to Twelve Labs.

This is the Tier 2 seam: everything else is written against this
interface, so a missing key just means is_available() == False and the
pipeline falls back to agent-vision labeling (Tier 1). Never import the
twelvelabs SDK anywhere else.

Adapted from sidney/labs/auto-edit/analyze_render.py (Sidney Swift,
2026): index + upload caching by content hash, per-shot Pegasus calls
(batched prompts degenerate), 429 back-off for the ~8 req/min free tier.

Usage:
    from library import twelvelabs_client as tl
    if tl.is_available():
        video_id = tl.get_or_upload_video(proxy_path)
        label = tl.describe_shot(video_id, 12.0, 18.5)
"""

import datetime as dt
import hashlib
import json
import time
from pathlib import Path

from library.env_config import REPO_ROOT, get_twelve_labs_key

CACHE_PATH = REPO_ROOT / ".tl_cache.json"
# pegasus1.2: the newest Pegasus this account can put in an index
# (native start_time/end_time scoping is pegasus1.5-only, so shot
# ranges are embedded in the prompt instead — the approach proven in
# the auto-edit spike). Model version is part of the index name
# because indexes are immutable; bumping the model = a new index.
PEGASUS_MODEL = "pegasus1.2"
INDEX_NAME = f"vinyl-video-editor-{PEGASUS_MODEL.replace('.', '-')}"
INDEX_MODELS = [
    {"model_name": "marengo3.0", "model_options": ["visual", "audio"]},
    {"model_name": PEGASUS_MODEL, "model_options": ["visual", "audio"]},
]

# The vocabulary fatbeats-content-analyze and knowledge/editing-rules.md share.
SEQUENCE_TYPES = [
    "unboxing", "gatefold-open", "vinyl-pull", "vinyl-spin",
    "pan-tracklist", "variant-reveal", "sleeve-detail", "insert-showcase",
    "dead-space", "other",
]

SHOT_SCHEMA = {
    "type": "json_schema",
    "json_schema": {
        "type": "object",
        "properties": {
            "visual": {"type": "string"},
            "key_action": {"type": "string"},
            "sequence_type": {"type": "string", "enum": SEQUENCE_TYPES},
            "motion_state": {
                "type": "string",
                "enum": ["starting", "mid-motion", "completing", "static"],
            },
        },
        "required": ["visual", "key_action", "sequence_type", "motion_state"],
    },
}


def is_available() -> bool:
    """Gate for Tier 2. Callers MUST check this and fall back cleanly."""
    return get_twelve_labs_key() is not None


def _client():
    from twelvelabs import TwelveLabs  # deferred: SDK optional at Tier 0/1

    return TwelveLabs(api_key=get_twelve_labs_key())


def _retry_on_rate_limit(call):
    """Honor 429 retry-after (free tier ~8 req/min)."""
    from twelvelabs.errors.too_many_requests_error import TooManyRequestsError

    while True:
        try:
            return call()
        except TooManyRequestsError as err:
            retry_after = 60
            try:
                retry_after = int(err.headers.get("retry-after", "60"))
            except (AttributeError, ValueError, TypeError):
                pass
            print(f"    [twelve-labs rate limit] sleeping {retry_after}s")
            time.sleep(retry_after + 1)


# --- content-hash cache (video re-uploads are the slow, costly part) --------


def _file_hash(path: Path) -> str:
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while chunk := handle.read(1024 * 1024):
            digest.update(chunk)
    return digest.hexdigest()[:16]


def _load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text())
    return {"index_id": None, "videos": {}}


def _save_cache(cache: dict) -> None:
    CACHE_PATH.write_text(json.dumps(cache, indent=2, default=str))


def get_or_create_index() -> str:
    """Resolve INDEX_NAME to an id: local cache, then remote lookup by
    name (indexes survive cache deletion), then create."""
    client, cache = _client(), _load_cache()
    cached_id = cache.get("index_id")
    if cached_id and cache.get("index_name") == INDEX_NAME:
        try:
            client.indexes.retrieve(index_id=cached_id)
            return cached_id
        except Exception:
            print(f"  cached index {cached_id} gone; re-resolving")

    index_id = None
    try:
        for index in client.indexes.list(index_name=INDEX_NAME):
            index_id = index.id if hasattr(index, "id") else index["id"]
            break
    except Exception:
        pass
    if index_id is None:
        response = client.indexes.create(index_name=INDEX_NAME, models=INDEX_MODELS)
        index_id = response.id if hasattr(response, "id") else response["id"]

    cache["index_id"] = index_id
    cache["index_name"] = INDEX_NAME
    _save_cache(cache)
    return index_id


def get_or_upload_video(video_path: Path) -> str:
    """Upload + index video (once per content hash); return video_id."""
    client, cache = _client(), _load_cache()
    digest = _file_hash(video_path)
    videos = cache.setdefault("videos", {})
    if digest in videos and videos[digest].get("video_id"):
        return videos[digest]["video_id"]

    index_id = get_or_create_index()
    print(f"  uploading {video_path.name} ({video_path.stat().st_size // (1024*1024)} MB) to Twelve Labs...")
    started = time.time()
    with open(video_path, "rb") as handle:
        task = client.tasks.create(index_id=index_id, video_file=handle)
    task_id = task.id if hasattr(task, "id") else task["id"]
    completed = client.tasks.wait_for_done(task_id=task_id)
    video_id = (
        completed.video_id if hasattr(completed, "video_id") else completed["video_id"]
    )
    videos[digest] = {
        "video_id": video_id,
        "filename": video_path.name,
        "indexed_at": dt.datetime.now().isoformat(),
        "elapsed_secs": round(time.time() - started, 1),
    }
    _save_cache(cache)
    print(f"  indexed in {videos[digest]['elapsed_secs']}s; video_id={video_id}")
    return video_id


def describe_shot(video_id: str, start: float, end: float) -> dict:
    """One Pegasus call labeling one shot with the vinyl vocabulary.

    The time range is embedded in the prompt (pegasus1.2 has no native
    start_time/end_time). Per-shot calls cost more than one batched
    prompt but batching degenerates descriptions — auto-edit finding."""
    from twelvelabs.types import SyncResponseFormat

    client = _client()
    prompt = (
        f"Focus ONLY on the time range {start:.2f}s to {end:.2f}s of this "
        "vinyl record showcase video (shot for TikTok Shop). Describe "
        "what happens in that range alone. Return JSON:\n"
        '  "visual": one sentence, what is on screen;\n'
        '  "key_action": short noun phrase (e.g. "pulls vinyl 2 from sleeve");\n'
        '  "sequence_type": one of '
        f"{SEQUENCE_TYPES} — dead-space means no product is being "
        "showcased (empty table, hands only, walking, blur);\n"
        '  "motion_state": at the END of the range is the action starting, '
        "mid-motion, completing, or is the frame essentially static?"
    )
    result = _retry_on_rate_limit(
        lambda: client.analyze(
            video_id=video_id,
            prompt=prompt,
            response_format=SyncResponseFormat(**SHOT_SCHEMA),
        )
    )
    raw = result.data if isinstance(result.data, str) else json.dumps(result.data)
    return json.loads(raw)
