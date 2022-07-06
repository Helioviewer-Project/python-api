from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jpx import getJPXInputParameters
from hvpy.core import execute_api_call


def test_raw_response():
    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=False,
        cadence=None,
    )
    response = execute_api_call(params)
    assert isinstance(response, bytes)


def test_str_response():
    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=True,
        cadence=None,
    )
    response = execute_api_call(params)
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=True,
        cadence=None,
    )
    response = execute_api_call(params)
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0),
        endTime=datetime(2014, 1, 1, 0, 45, 0),
        sourceId=14,
        linked=False,
        verbose=True,
        jpip=False,
        cadence=None,
    )
    response = execute_api_call(params)
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling():
    with pytest.raises(ValidationError, match="getJPXInputParameters\nstartTime\n  field required"):
        getJPXInputParameters(endTime=datetime(2014, 1, 1, 0, 45, 0), sourceId=14)

    with pytest.raises(ValidationError, match="getJPXInputParameters\nendTime\n  field required"):
        getJPXInputParameters(startTime=datetime(2014, 1, 1, 0, 0, 0), sourceId=14)

    with pytest.raises(ValidationError, match="getJPXInputParameters\nsourceId\n  field required"):
        getJPXInputParameters(startTime=datetime(2014, 1, 1, 0, 0, 0), endTime=datetime(2014, 1, 1, 0, 45, 0))


def test_url_property():
    params = getJPXInputParameters(
        startTime=datetime(2014, 1, 1, 0, 0, 0), endTime=datetime(2014, 1, 1, 0, 45, 0), sourceId=14
    )
    assert params.url == "https://api.helioviewer.org/v2/getJPX/"
