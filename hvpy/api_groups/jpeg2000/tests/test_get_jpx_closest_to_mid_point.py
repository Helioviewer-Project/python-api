from datetime import datetime, timedelta

import pytest

from hvpy import getJPXClosestToMidPoint
from hvpy.api_groups.jpeg2000.get_jpx_closest_to_mid_point import getJPXClosestToMidPointInputParameters

startTimes = [datetime.today() - timedelta(days=16), datetime.today() - timedelta(days=16, hours=1, minutes=30)]
endTimes = [datetime.today() - timedelta(days=15), datetime.today() - timedelta(days=15, hours=1, minutes=30)]


def test_raw_response():
    response = getJPXClosestToMidPoint(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=False, jpip=False
    )
    assert isinstance(response, bytes)


def test_str_response():
    response = getJPXClosestToMidPoint(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=False, jpip=True
    )
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    response = getJPXClosestToMidPoint(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=True, jpip=True
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    response = getJPXClosestToMidPoint(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=True, jpip=False
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'startTimes'"):
        getJPXClosestToMidPoint(endTimes=endTimes, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'endTimes'"):
        getJPXClosestToMidPoint(startTimes=startTimes, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getJPXClosestToMidPoint(startTimes=startTimes, endTimes=endTimes)


def test_url_property():
    params = getJPXClosestToMidPointInputParameters(startTimes=startTimes, endTimes=endTimes, sourceId=14)
    assert params.url == "https://api.beta.helioviewer.org/v2/getJPXClosestToMidPoint/"
