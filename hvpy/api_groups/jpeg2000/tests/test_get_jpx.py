from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jpx import getJPXInputParameters
from hvpy.core import execute_api_call

startTime = datetime(2014, 1, 1, 0, 0, 0)
endTime = datetime(2014, 1, 1, 0, 45, 0)


@pytest.mark.parametrize(
    "startTime, endTime, sourceId, linked, verbose, jpip, candence",
    [
        (startTime, endTime, 14, False, False, False, None),
        (startTime, endTime, 14, False, False, True, None),
        (startTime, endTime, 14, False, True, True, None),
        (startTime, endTime, 14, False, True, False, None),
    ],
)
def test_getJPXInputParameters(startTime, endTime, sourceId, linked, verbose, jpip, candence):
    params = getJPXInputParameters(
        startTime=startTime,
        endTime=endTime,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
        cadence=candence,
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
    with pytest.raises(ValidationError, match="getJPXInputParameters\nstartTime\n  field required"):
        getJPXInputParameters(endTime=endTime, sourceId=14)

    with pytest.raises(ValidationError, match="getJPXInputParameters\nendTime\n  field required"):
        getJPXInputParameters(startTime=startTime, sourceId=14)

    with pytest.raises(ValidationError, match="getJPXInputParameters\nsourceId\n  field required"):
        getJPXInputParameters(startTime=startTime, endTime=endTime)


def test_url_property():
    params = getJPXInputParameters(startTime=startTime, endTime=endTime, sourceId=14)
    assert params.url == "https://api.helioviewer.org/v2/getJPX/"


def test_unknown_parameters():
    params = getJPXInputParameters(
        startTime=startTime,
        endTime=endTime,
        sourceId=14,
        linked=False,
        verbose=False,
        jpip=False,
        cadence=None,
        unknown_parameter="unknown",
    )
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)
