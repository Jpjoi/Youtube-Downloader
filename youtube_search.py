from googleapiclient.discovery import build

from config import YOUTUBE_API_KEY


def search_youtube(query):
    """
    Search YouTube and return the first video result.

    Returns:
        dict containing:
            title
            channel
            video_id
            url

    Returns None if no video was found.
    """

    youtube = build(
        "youtube",
        "v3",
        developerKey=YOUTUBE_API_KEY
    )

    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=1
    )

    response = request.execute()

    if not response.get("items"):
        return None

    item = response["items"][0]

    video_id = item["id"]["videoId"]
    snippet = item["snippet"]

    return {
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "video_id": video_id,
        "url": f"https://www.youtube.com/watch?v={video_id}"
    }