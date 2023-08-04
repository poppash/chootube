from typing import Any, Iterable

from googleapiclient.discovery import Resource

from chootube.factory import make_youtube
from chootube.typing import Response


class FetchException(Exception):
    ...


def get_resource(resource: str, *args, **kwargs) -> Resource:
    youtube = kwargs.get("youtube") or make_youtube()
    return getattr(youtube, resource)()


def fetch(
    resource: str | Resource,
    method: str,
    params: dict[str, Any],
    *args,
    **kwargs,
) -> Iterable[Response]:
    if type(resource) is str:
        resource = get_resource(resource, *args, **kwargs)

    if not type(resource) is Resource:
        raise FetchException  # TODO

    if not hasattr(resource, method):
        raise FetchException  # TODO

    fn = getattr(resource, method)
    if not callable(fn):
        raise FetchException  # TODO

    next_page_token = None

    while True:
        response = fn(**params, pageToken=next_page_token).execute()

        yield response

        next_page_token = response.get("nextPageToken", None)
        if not next_page_token:
            break
