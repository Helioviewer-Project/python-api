import pytest

from hvpy import getMovieStatus
from hvpy.api_groups.movies.get_movie_status import getMovieStatusInputParameters


def test_json_response():
    response = getMovieStatus(
        id="h2n6n",
        format="mp4",
    )
    assert response["url"] is not None
    assert response["status"] is not None


def test_str_response():
    response = getMovieStatus(
        id="h2n6n",
        format="mp4",
        callback="myCallback",
    )
    assert response.startswith("myCallback(")


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        getMovieStatus(
            format="mp4",
            verbose=False,
            callback=None,
            token=None,
        )

    with pytest.raises(TypeError, match="missing 1 required positional argument: 'format'"):
        getMovieStatus(
            id="VXvX5",
            verbose=False,
            callback=None,
            token=None,
        )


def test_url_property():
    params = getMovieStatusInputParameters(
        id="VXvX5",
        format="mp4",
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/getMovieStatus/"
