import os
from pathlib import Path

import google_auth_oauthlib  # type: ignore[import]
from google.oauth2.credentials import Credentials  # type: ignore[import]
from googleapiclient.discovery import Resource, build

YOUTUBE: Resource | None = None

KWARGS_DEFAULT = {"serviceName": "youtube", "version": "v3"}
KWARGS_FROM_ENV = {"developerKey": os.getenv("YOUTUBE_API_KEY")}


def make_credentials_from_client_secrets_file(
    filepath: str | Path | None = None, scopes: list[str] = []
) -> Credentials:
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    filepath = filepath or os.getenv("YOUTUBE_CLIENT_SECRETS_FILE")
    if not filepath:
        raise Exception("No proper 'filepath' was specified.")

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        filepath, scopes
    )

    return flow.run_local_server()


def make_youtube(force: bool = False, **kwargs) -> Resource:
    global YOUTUBE

    kwargs_from_merger = {**KWARGS_DEFAULT, **KWARGS_FROM_ENV, **kwargs}

    if force or not YOUTUBE:
        YOUTUBE = build(**kwargs_from_merger)

    return YOUTUBE
