import pytest

from hvpy import reQueueMovie
from hvpy.api_groups.movies.re_queue_movie import reQueueMovieInputParameters


# Skipping since reQueueMovie will fail while the requested
# movie is being processed by Helioviewer. The test suite
# will call this for each python version that's tested.
# The first call will work, but following calls will fail
# with the API saying "Movie is already being processed"
@pytest.mark.skip(reason="Cannot be called multiple times in a test suite. All calls after the 1st will fail.")
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
    assert params.url == "https://api.beta.helioviewer.org/v2/reQueueMovie/"
