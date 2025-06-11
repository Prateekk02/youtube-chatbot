import re
from urllib.parse import urlparse, parse_qs
from typing import Final, Optional

class InvalidYouTubeURLError(ValueError):
    """Raised when *url* is not a valid YouTube video link."""


# Fallback regex for odd formats (embed, /v/, etc.)
_REGEX: Final[str] = (
    r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)/|.*[?&]v=)|'
    r'youtu\.be/)([^"&?/]{11})'
)


def get_video_id(url: str) -> Optional[str]:
    """
    Return the 11-character video ID or raise `InvalidYouTubeURLError`.

    Supported forms
    ---------------
    https://www.youtube.com/watch?v=ID
    https://m.youtube.com/watch?v=ID
    https://youtu.be/ID
    https://www.youtube.com/embed/ID
    https://www.youtube.com/v/ID
    """
    # Short share links -------------------------------------------------------
    if "youtu.be/" in url:
        candidate = url.split("youtu.be/")[1].split("?")[0][:11]
        if _is_valid_id(candidate):
            return candidate

    # Canonical watch URLs ----------------------------------------------------
    parsed = urlparse(url)
    if parsed.hostname in {"www.youtube.com", "youtube.com", "m.youtube.com"}:
        vid = parse_qs(parsed.query).get("v", [None])[0]
        if _is_valid_id(vid):
            return vid

    # Embed, /v/, other oddities ---------------------------------------------
    match = re.search(_REGEX, url)
    if match and _is_valid_id(match.group(1)):
        return match.group(1)

    raise InvalidYouTubeURLError(f"Not a recognised YouTube video URL: {url}")


def _is_valid_id(video_id: str | None) -> bool:
    """Return True when video_id looks like a legitimate YouTube ID."""
    return bool(video_id and re.fullmatch(r"[\w-]{11}", video_id))
