from datetime import datetime, timedelta

import pytest

from hvpy import getJPX
from hvpy.api_groups.jpeg2000.get_jpx import getJPXInputParameters


@pytest.fixture
def start_time():
    return datetime.today() - timedelta(days=16)


@pytest.fixture
def end_time():
    return datetime.today() - timedelta(days=15)


def test_raw_response(start_time, end_time):
    response = getJPX(
        startTime=datetime.today() - timedelta(days=1),
        endTime=datetime.today(),
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=False,
        cadence=None,
    )
    assert isinstance(response, bytes)


def test_str_response(start_time, end_time):
    response = getJPX(
        startTime=start_time,
        endTime=end_time,
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=True,
        cadence=None,
    )
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response(start_time, end_time):
    response = getJPX(
        startTime=start_time,
        endTime=end_time,
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=True,
        cadence=None,
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    response = getJPX(
        startTime=start_time,
        endTime=end_time,
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=False,
        cadence=None,
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling(start_time, end_time):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'startTime'"):
        getJPX(endTime=end_time, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'endTime'"):
        getJPX(startTime=start_time, sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getJPX(startTime=start_time, endTime=end_time)


def test_url_property(start_time, end_time):
    params = getJPXInputParameters(
        startTime=start_time,
        endTime=end_time,
        sourceId=14,
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/getJPX/"
