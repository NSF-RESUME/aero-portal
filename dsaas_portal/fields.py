import os
from urllib.parse import urlparse, urlsplit, urlunsplit, urlencode


def title(result):
    """The title for this Globus Search subject"""
    return result[0]["name"]


def globus_app_link(result):
    """A Globus Webapp link for the transfer/sync button on the detail page"""
    url = get_file(result).get("url")
    if not url:
        return
    parsed = urlparse(url)
    query_params = {
        "origin_id": "52f7f6bc-444f-439a-ad48-a4569d10c3d1", #parsed.netloc,
        "origin_path": os.path.dirname(parsed.path),
    }
    return urlunsplit(
        ("https", "app.globus.org", "file-manager", urlencode(query_params), "")
    )


def https_url(result):
    """Add a direct download link to files over HTTPS"""
    url = get_file(result).get("url")
    if not url:
        return
    path = urlparse(url).path
    return urlunsplit(("https", "g-c952d0.1305de.36fe.data.globus.org", path, "", ""))


def get_file(result):
    """To start, 'test' files are just a single file in a directory, so we'll always just look
    for the first file in the list."""
    return result[0]


def search_results(result):
    file_metadata = get_file(result)
    return [
        {
            "field": "name",
            "title": "Name",
            "value": file_metadata.get('filename')
        },
        {
            "field": "size",
            "title": "Size",
            "type": "int",
            "value": file_metadata.get('length')
        },
    ]
