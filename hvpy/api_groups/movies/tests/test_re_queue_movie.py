import pytest

from hvpy import reQueueMovie
from hvpy.api_groups.movies.re_queue_movie import reQueueMovieInputParameters


def test_json_response():
    response = reQueueMovie(id="gxRN5", force=True)
    assert response["id"] is not None
    assert response["eta"] is not None
    assert response["queue"] is not None
    assert response["token"] is not None


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        reQueueMovie()


def test_url_property():
    params = reQueueMovieInputParameters(id="gxRN5")
    assert params.url == "https://api.helioviewer.org/v2/reQueueMovie/"
