import googleapiclient.discovery
from googleapiclient.errors import HttpError

class YouTubeController:
    """
    A class to interact with the YouTube API.
    """

    def __init__(self):
        """
        Initializes the YouTubeController.
        """
        self.api_key = "AIzaSyCUmbrtm2qcflGvuY9gYmeD3ItzxbgD2pA"

    def search_youtube_videos(self, query, max_results=1000):
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
