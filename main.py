from utils.youtube_controller import YouTubeController
from utils.youtube_audio_downloader import YouTubeAudioDownloader
from utils.youtube_transcript_extractor import YouTubeTranscriptExtractor
from utils.tts_dataset_generator import TTSDatasetGenerator

if __name__ == "__main__":

    preferred_language = "ga"
    youtube_audio_downloader = YouTubeAudioDownloader("output")
    youtube_transcript_creator = YouTubeTranscriptExtractor(preferred_language)

    api_key = "API_KEY"
    api_object = YouTubeController(api_key)

    # You can update these querires to improvise the search
    # If you want to create a dataset for different languages, 
    # update these queries and update preferred language in line 12
    videos = api_object.search_youtube_videos("Gaeilge")
    videos += api_object.search_youtube_videos("Gaeilge interviews")
    videos += api_object.search_youtube_videos("Gaeilge podcasts")

    dataset_generator = TTSDatasetGenerator("output", youtube_audio_downloader, youtube_transcript_creator)

    for video in videos:
        video_id = video['id']['videoId']
        dataset_generator.generate_dataset(video_id)
