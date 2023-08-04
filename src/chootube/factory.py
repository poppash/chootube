from os import getenv

from googleapiclient.discovery import Resource, build

YOUTUBE: Resource | None = None


def make_youtube(api_key: str | None = None) -> Resource:
    global YOUTUBE

    if not YOUTUBE:
        YOUTUBE = build(
            "youtube", "v3", developerKey=api_key or getenv("YOUTUBE_API_KEY")
        )

    return YOUTUBE
