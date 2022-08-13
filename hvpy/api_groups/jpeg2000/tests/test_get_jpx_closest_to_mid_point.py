import pytest

from hvpy import getJPXClosestToMidPoint
from hvpy.api_groups.jpeg2000.get_jpx_closest_to_mid_point import getJPXClosestToMidPointInputParameters


def test_raw_response(start_times, end_times):
    response = getJPXClosestToMidPoint(
        startTimes=start_times, endTimes=end_times, sourceId=14, linked=False, verbose=False, jpip=False
    )
    assert isinstance(response, bytes)


def test_str_response(start_times, end_times):
    response = getJPXClosestToMidPoint(
        startTimes=start_times, endTimes=end_times, sourceId=14, linked=False, verbose=False, jpip=True
    )
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response(start_times, end_times):
    response = getJPXClosestToMidPoint(
        startTimes=start_times, endTimes=end_times, sourceId=14, linked=False, verbose=True, jpip=True
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    response = getJPXClosestToMidPoint(
        startTimes=start_times, endTimes=end_times, sourceId=14, linked=False, verbose=True, jpip=False
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling(start_times, end_times):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'startTimes'"):
        getJPXClosestToMidPoint(endTimes=end_times, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'endTimes'"):
        getJPXClosestToMidPoint(startTimes=start_times, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getJPXClosestToMidPoint(startTimes=start_times, endTimes=end_times)


def test_url_property(start_times, end_times):
    params = getJPXClosestToMidPointInputParameters(startTimes=start_times, endTimes=end_times, sourceId=14)
    assert params.url == "https://api.beta.helioviewer.org/v2/getJPXClosestToMidPoint/"
