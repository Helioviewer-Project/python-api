import pytest

from hvpy import downloadMovie
from hvpy.api_groups.movies.download_movie import downloadMovieInputParameters


def test_raw_response():
    response = downloadMovie(
        id="h2n6n",
        format="mp4",
    )
    assert isinstance(response, bytes)


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        downloadMovie(
            format="mp4",
        )

    with pytest.raises(TypeError, match="missing 1 required positional argument: 'format'"):
        downloadMovie(
            id="VXvX5",
        )


def test_url_property():
    params = downloadMovieInputParameters(
        id="VXvX5",
        format="mp4",
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/downloadMovie/"
