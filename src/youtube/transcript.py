from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api._errors import (
    TranscriptsDisabled, NoTranscriptFound
)
import xml.etree.ElementTree as ET
import time

def get_transcript(video_id, lang="en", retries=3, delay=2):
    for attempt in range(retries):
        try:
            t = YouTubeTranscriptApi.get_transcript(video_id, languages=[lang])
            return " ".join(seg["text"] for seg in t)
        except (TranscriptsDisabled, NoTranscriptFound):
            raise              # nothing you can do
        except ET.ParseError:  # empty body / bad XML
            if attempt == retries - 1:
                raise
            time.sleep(delay * (attempt + 1))
