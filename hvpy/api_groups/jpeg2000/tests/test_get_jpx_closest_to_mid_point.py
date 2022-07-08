from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jpx_closest_to_mid_point import getJPXClosestToMidPointInputParameters
from hvpy.core import execute_api_call

startTimes = [datetime(2014, 1, 1, 0, 0, 0), datetime(2014, 1, 1, 2, 3, 3), datetime(2014, 1, 1, 4, 5, 5)]
endTimes = [datetime(2014, 1, 1, 0, 45, 0), datetime(2014, 1, 1, 2, 33, 3), datetime(2014, 1, 1, 4, 54, 5)]


def test_raw_response():
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=False, jpip=False
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)


def test_str_response():
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=False, jpip=True
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=True, jpip=True
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert response["uri"].startswith("jpip://")

    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes, endTimes=endTimes, sourceId=14, linked=False, verbose=True, jpip=False
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert response["uri"].startswith("https://")


def test_error_handling():
    with pytest.raises(ValidationError, match="getJPXClosestToMidPointInputParameters\nstartTimes\n  field required"):
        getJPXClosestToMidPointInputParameters(endTimes=endTimes, sourceId=14)

    with pytest.raises(ValidationError, match="getJPXClosestToMidPointInputParameters\nendTimes\n  field required"):
        getJPXClosestToMidPointInputParameters(startTimes=startTimes, sourceId=14)

    with pytest.raises(ValidationError, match="getJPXClosestToMidPointInputParameters\nsourceId\n  field required"):
        getJPXClosestToMidPointInputParameters(startTimes=startTimes, endTimes=endTimes)


def test_url_property():
    params = getJPXClosestToMidPointInputParameters(startTimes=startTimes, endTimes=endTimes, sourceId=14)
    assert params.url == "https://api.helioviewer.org/v2/getJPXClosestToMidPoint/"
