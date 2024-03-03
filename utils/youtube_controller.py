import googleapiclient.discovery
from googleapiclient.errors import HttpError

class YouTubeController:
    """
    A class to interact with the YouTube API.
    """

    def __init__(self, api_key: str)  -> None:
        """
        Initializes the YouTubeController.

        Args:
        api_key : Get API key for youtube API V3

        """
        self.api_key = api_key

    def search_youtube_videos(self, query: str, max_results: str = 1000) -> list:
        """
        Send API request to YouTube API and return the response.

        Args:
        query (str): The query to search on YouTube.
        max_results (int): The maximum number of results to retrieve (default is 1000).

        Returns:
        list: A list of dictionaries containing video information.
        """
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=self.api_key)

        try:
            search_response = youtube.search().list(
                q=query,
                type="video",
                part="id",
                maxResults=max_results,
                videoCaption="closedCaption",
                regionCode="IE",
                relevanceLanguage="",
                safeSearch="strict",
                videoLicense="youtube"
            ).execute()

            videos = search_response.get("items", [])
            return videos

        except HttpError as e:
            print(f"An error occurred: {e}")
            return None
