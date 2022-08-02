from datetime import datetime

import pytest

from hvpy import queueMovie
from hvpy.api_groups.movies.queue_movie import queueMovieInputParameters


def test_json_response():
    response = queueMovie(
        startTime=datetime(2022, 7, 20, 12, 12, 12),
        endTime=datetime(2022, 7, 21, 12, 12, 12),
        layers="[12,7,22],[13,7,22]",
        events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
        eventsLabels=False,
        imageScale=1,
    )
    assert response["id"] is not None
    assert response["eta"] is not None
    assert response["queue"] is not None
    assert response["token"] is not None


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'imageScale'"):
        queueMovie(
            startTime=datetime(2022, 7, 20, 12, 12, 12),
            endTime=datetime(2022, 7, 21, 12, 12, 12),
            layers="[12,7,22],[13,7,22]",
            events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
            eventsLabels=False,
        )


def test_url_property():
    params = queueMovieInputParameters(
        startTime=datetime(2022, 7, 20, 12, 12, 12),
        endTime=datetime(2022, 7, 21, 12, 12, 12),
        layers="[12,7,22],[13,7,22]",
        events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
        eventsLabels=False,
        imageScale=1,
    )
    assert params.url == "https://api.helioviewer.org/v2/queueMovie/"
