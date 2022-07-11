from datetime import datetime

import pytest

from hvpy import getJPX
from hvpy.api_groups.jpeg2000.get_jpx import getJPXInputParameters


def test_raw_response():
    response = getJPX(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=False,
        cadence=None,
    )
    assert isinstance(response, bytes)


def test_str_response():
    response = getJPX(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=True,
        cadence=None,
    )
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    response = getJPX(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=True,
        cadence=None,
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    response = getJPX(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=False,
        cadence=None,
    )
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'startTime'"):
        getJPX(endTime=datetime(2014, 1, 1, 0, 45, 0), sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'endTime'"):
        getJPX(startTime=datetime(2014, 1, 1, 0, 0, 0), sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getJPX(startTime=datetime(2014, 1, 1, 0, 0, 0), endTime=datetime(2014, 1, 1, 0, 45, 0))


def test_url_property():
    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0), endTime=datetime(2014, 1, 1, 0, 45, 0), sourceId=14
    )
    assert params.url == "https://api.helioviewer.org/v2/getJPX/"
