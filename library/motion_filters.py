"""motion_filters.py — ffmpeg filter builders for EDL motion + speed.

The editor's deterministic toolkit, applied per segment at render time:

    "motion": {"type": "punch_in", "amount": 1.10}   digital push toward center
    "motion": {"type": "pull_back", "amount": 1.08}  start tight, ease out
    "speed": 1.25                                    tempo change (audio-safe)

Why zoompan and not scale/crop: crop output dimensions must be constant,
so an animated zoom has to be expressed as a moving crop window that
zoompan owns natively. Source footage is 4K (2160x3840); at the enforced
<=1.2x cap a punch-in still resolves well above delivery resolution, and
zoompan's integer-pixel stepping is invisible on moving handheld video.

WHEN to use these lives in knowledge/editing-rules.md ("Motion & pacing
grammar") — this module only knows HOW. Range enforcement lives in
edl.py's validate_edl, next to the rest of the schema rules.
"""

MOTION_TYPES = ("punch_in", "pull_back")

# Taste caps, shared with edl.py validation. Beyond 1.2x a digital zoom
# reads as a crop mistake; below 1.02x it reads as encoder wobble.
MOTION_AMOUNT_MIN = 1.02
MOTION_AMOUNT_MAX = 1.20
SPEED_MIN = 0.5
SPEED_MAX = 2.0


def build_zoom_filter(
    motion: dict, duration_seconds: float, fps: float,
    fps_rational: str, width: int, height: int,
) -> str:
    """One eased (cosine in/out) zoompan expression covering the segment.

    `on` is zoompan's output-frame counter; progress is clamped to 1 so
    the final frames hold the target framing instead of wrapping.
    """
    amount = float(motion["amount"])
    total_frames = max(1, round(duration_seconds * fps))
    eased = f"(0.5-0.5*cos(PI*min(on/{total_frames},1)))"
    if motion["type"] == "punch_in":
        zoom_expression = f"1+({amount}-1)*{eased}"
    else:  # pull_back
        zoom_expression = f"{amount}-({amount}-1)*{eased}"
    return (
        f"zoompan=z='{zoom_expression}'"
        ":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
        f":d=1:s={width}x{height}:fps={fps_rational}"
    )


def build_segment_filters(
    segment: dict, fps: float, fps_rational: str, width: int, height: int,
) -> tuple[str | None, str | None]:
    """(video_filter, audio_filter) for one EDL segment, or (None, None).

    Plain segments return no filters, keeping the untouched fast path
    byte-identical with pre-motion renders.
    """
    motion = segment.get("motion")
    speed = float(segment.get("speed", 1.0))
    video_chain: list[str] = []
    audio_chain: list[str] = []

    if motion:
        source_duration = float(segment["end"]) - float(segment["start"])
        video_chain.append(
            build_zoom_filter(motion, source_duration, fps, fps_rational, width, height)
        )
    if speed != 1.0:
        video_chain.append(f"setpts=PTS/{speed}")
        audio_chain.append(f"atempo={speed}")

    return (
        ",".join(video_chain) or None,
        ",".join(audio_chain) or None,
    )
