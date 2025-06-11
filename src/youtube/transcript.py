from youtube_transcript_api._api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from extractor import get_video_id  

def get_transcript(url):
    video_id = get_video_id(url)
    if not video_id: 
        return "Cannot fetch video ID from the URL"
    print(video_id)
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=['en'])
        
        # Flatten into plain text
        transcript = ' '.join(chunk['text'] for chunk in transcript_list)
        return transcript
    except TranscriptsDisabled:
        return "Caption disabled."
    except NoTranscriptFound:
        return "No transcript found for this video."
    