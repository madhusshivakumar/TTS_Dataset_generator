from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeTranscriptExtractor:
    """
    A class to extract transcripts from YouTube videos.
    """

    def __init__(self, preferred_language: str) -> None:
        """
        Initializes the YouTubeTranscriptExtractor.

        Args:
        preferred_language (str): The preferred language for the transcript.
        """
        self.preferred_language = preferred_language
        pass

    def extract_transcript(self, video_id: str) -> list:
        """
        Extract transcript from a YouTube video.

        Args:
        video_id (str): The ID of the YouTube video.

        Returns:
        dict: The transcript of the video.
        """
        try:
            transcripts = YouTubeTranscriptApi.list_transcripts(video_id)
            selected_transcript = None
            for transcript in transcripts:
                if transcript.language_code == self.preferred_language:
                    selected_transcript = transcript
                    break

            if selected_transcript is None:
                return None
            else:
                return selected_transcript.fetch()
            return transcript
        except Exception as e:
            return None
