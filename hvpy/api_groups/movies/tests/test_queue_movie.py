import pytest

from hvpy import queueMovie
from hvpy.api_groups.movies.queue_movie import queueMovieInputParameters


def test_json_response(start_time, end_time):
    response = queueMovie(
        startTime=start_time,
        endTime=end_time,
        layers="[12,7,22],[13,7,22]",
        events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
        eventsLabels=False,
        imageScale=1,
    )
    assert response["id"] is not None
    assert response["eta"] is not None
    assert response["queue"] is not None
    assert response["token"] is not None


def test_error_handling(start_time, end_time):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'imageScale'"):
        queueMovie(
            startTime=start_time,
            endTime=end_time,
            layers="[12,7,22],[13,7,22]",
            events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
            eventsLabels=False,
        )


def test_url_property(start_time, end_time):
    params = queueMovieInputParameters(
        startTime=start_time,
        endTime=end_time,
        layers="[12,7,22],[13,7,22]",
        events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
        eventsLabels=False,
        imageScale=1,
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/queueMovie/"
