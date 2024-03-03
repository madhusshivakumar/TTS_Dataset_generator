from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeTranscriptExtractor:
    """
    A class to extract transcripts from YouTube videos.
    """

    def __init__(self):
        """
        Initializes the YouTubeTranscriptExtractor.
        """
        pass

    def extract_transcript(self, video_id, preferred_language):
        """
        Extract transcript from a YouTube video.

        Args:
        video_id (str): The ID of the YouTube video.
        preferred_language (str): The preferred language for the transcript.

        Returns:
        dict: The transcript of the video.
        """
        try:
            transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            selected_transcript = None
            for transcript in transcripts:
                if transcript.language_code == preferred_language:
                    selected_transcript = transcript
                    break

            if selected_transcript is None:
                return None
            else:
                return selected_transcript.fetch()
            return transcript
        except Exception as e:
            return None
