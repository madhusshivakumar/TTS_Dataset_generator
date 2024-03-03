import os
from pydub import AudioSegment
import re
from utils import youtube_audio_downloader, youtube_transcript_extractor

class TTSDatasetGenerator:
    """
    A class to generate datasets for text-to-speech tasks.
    """

    def __init__(self, output_path: str, youtube_downloader: youtube_audio_downloader,
                 transcript_extractor: youtube_transcript_extractor):
        """
        Initializes the TTSDatasetGenerator.

        Args:
        output_path (str): The path to save the generated dataset.
        youtube_downloader (YouTubeAudioDownloader): An instance of YouTubeAudioDownloader.
        transcript_extractor (YouTubeTranscriptExtractor): An instance of YouTubeTranscriptExtractor.
        """
        self.output_path = output_path
        self.youtube_downloader = youtube_downloader
        self.transcript_extractor = transcript_extractor

    def clean_text(self, text):
        """
        Clean text by removing speaker identifiers, timestamps, non-verbal sounds, and extra spaces.

        Args:
        text (str): The text to clean.

        Returns:
        str: The cleaned text.
        """
        cleaned_text = re.sub(r'[A-Za-z]+\s\d+:', '', text)
        cleaned_text = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', cleaned_text)
        cleaned_text = re.sub(r'\[[A-Za-z\s]+\]', '', cleaned_text)
        cleaned_text = re.sub(r'\(.*?\)', '', cleaned_text)
        cleaned_text = re.sub(r'\{.*?\}', '', cleaned_text)
        cleaned_text = re.sub(r'\[.*?\]', '', cleaned_text)
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
        return cleaned_text

    def generate_dataset(self, video_id, preferred_language):
        """
        Generate dataset for text-to-speech task.

        Args:
        video_id (str): The ID of the YouTube video.
        preferred_language (str): The preferred language for the transcript.
        """
        self.transcript = self.transcript_extractor.extract_transcript(video_id, preferred_language)
        if self.transcript:
            self.audio_path = self.youtube_downloader.download_audio(self.output_path, video_id)
            if self.audio_path:
                self.audio = AudioSegment.from_file(self.audio_path)
                self.matched_folder = os.path.join(self.output_path, video_id)
                self.matched_folder = os.path.join(self.matched_folder, "segments")
                os.makedirs(self.matched_folder, exist_ok=True)

                for i, line in enumerate(self.transcript):
                    start_time = line['start'] * 1000
                    end_time = start_time + line['duration'] * 1000
                    segment = self.audio[start_time:end_time]

                    normalized_text = self.clean_text(line['text'])
                    if len(normalized_text) != 0:
                        segment.export(os.path.join(self.matched_folder, f"segment_{i}.mp3"), format="mp3")
                        with open(os.path.join(self.matched_folder, f"segment_{i}.txt"), "w",
                                  encoding="utf-8") as f:
                            f.write(line['text'])
                        with open(os.path.join(self.matched_folder, f"segment_{i}_normalized.txt"), "w",
                                  encoding="utf-8") as f:
                            f.write(normalized_text)
