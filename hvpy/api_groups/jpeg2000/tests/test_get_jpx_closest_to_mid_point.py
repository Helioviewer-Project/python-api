from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jpx_closest_to_mid_point import getJPXClosestToMidPointInputParameters
from hvpy.core import execute_api_call

startTimes = [datetime(2014, 1, 1, 0, 0, 0), datetime(2014, 1, 1, 2, 3, 3), datetime(2014, 1, 1, 4, 5, 5)]
endTimes = [datetime(2014, 1, 1, 0, 45, 0), datetime(2014, 1, 1, 2, 33, 3), datetime(2014, 1, 1, 4, 54, 5)]


@pytest.mark.parametrize(
    "startTimes, endTimes, sourceId, linked, verbose, jpip",
    [
        (startTimes, endTimes, 14, False, False, False),
        (startTimes, endTimes, 14, False, False, True),
        (startTimes, endTimes, 14, False, True, True),
        (startTimes, endTimes, 14, False, True, False),
    ],
)
def test_getJPXClosestToMidPointInputParameters(startTimes, endTimes, sourceId, linked, verbose, jpip):
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes,
        endTimes=endTimes,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
    )
    response = execute_api_call(input_parameters=params)
    if not jpip and not verbose:
        assert isinstance(response, bytes)
    elif jpip and not verbose:
        assert isinstance(response, str)
        assert response.startswith("jpip://")
    elif jpip and verbose:
        assert isinstance(response, dict)
        assert response["uri"].startswith("jpip://")
    elif not jpip and verbose:
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


def test_unknown_parameters():
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes,
        endTimes=endTimes,
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=False,
        unknown_parameter="unknown",
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)
