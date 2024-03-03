from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

class YouTubeAudioDownloader:
    """
    A class to download audio from YouTube videos.
    """

    def __init__(self, output_path : str) -> None:
        """
        Initializes the YouTubeAudioDownloader.


        Args:
        output_path (str): The path to save the audio file.
        """
        self.output_path = output_path
        pass

    def download_audio(self, video_id : str) -> str:
        """
        Download audio from a YouTube video.

        Args:
        video_id (str): The ID of the YouTube video.

        Returns:
        str: The path to the downloaded audio file.
        """
        try:
            youtube_link = f"https://www.youtube.com/watch?v={video_id}"
            print(youtube_link)
            yt = YouTube(youtube_link)
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_path = f"{self.output_path}/{video_id}"
            audio_stream.download(output_path=audio_path, filename=f"{video_id}.mp4")
            return f"{audio_path}/{video_id}.mp4"
        except AgeRestrictedError as e:
            print(f"The video with ID {video_id} is age restricted. Unable to download audio.")
            return None
