from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
 
from src.youtube.extractor import get_video_id  

class TranscriptNotFoundError(RuntimeError):
    ...

def get_transcript(url: str, lang: str = "en") -> str:
    video_id = get_video_id(url)
    if not video_id:
        raise ValueError("Could not extract video ID from URL")

    try:
        segments = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
        return " ".join(seg["text"].strip() for seg in segments if seg["text"].strip())
    except (TranscriptsDisabled, NoTranscriptFound):
        raise TranscriptNotFoundError("Transcript unavailable for this video")
