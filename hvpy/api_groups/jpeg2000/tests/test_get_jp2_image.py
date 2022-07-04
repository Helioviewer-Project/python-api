from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.core import execute_api_call

date_obj = datetime(2020, 1, 1)


@pytest.mark.parametrize("date_obj", [date_obj])
def test_default_response(date_obj):
    params = getJP2ImageInputParameters(date=date_obj, sourceId=14)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)


@pytest.mark.parametrize(
    "date, sourceId, jpip, json",
    [
        (datetime(2022, 1, 1, 23, 59, 59), 14, True, False),
        (datetime(2022, 1, 1, 23, 59, 59), 14, True, True),
        (datetime(2022, 1, 1, 23, 59, 59), 14, False, True),
        (datetime(2022, 1, 1, 23, 59, 59), 14, False, False),
    ],
)
def test_getJP2ImageInputParameters(date, sourceId, jpip, json):
    params = getJP2ImageInputParameters(date=date, sourceId=sourceId, jpip=jpip, json=json)
    response = execute_api_call(input_parameters=params)
    if jpip and not json:
        assert isinstance(response, str)
        assert response.startswith("jpip://")
    elif jpip and json:
        assert isinstance(response, dict)
        assert "uri" in response
        assert response["uri"].startswith("jpip://")
    elif not jpip and json:
        assert isinstance(response, bytes)
    elif not jpip and not json:
        assert isinstance(response, bytes)


def test_error_handling():
    with pytest.raises(ValidationError, match="getJP2ImageInputParameters\ndate\n  field required"):
        getJP2ImageInputParameters(sourceId=14, jpip=True, json=True)


@pytest.mark.parametrize("date_obj", [date_obj])
def test_url_property(date_obj):
    params = getJP2ImageInputParameters(date=date_obj, sourceId=14, jpip=True, json=True)
    assert params.url == "https://api.helioviewer.org/v2/getJP2Image/"


@pytest.mark.parametrize("date_obj", [date_obj])
def test_unknown_parameters(date_obj):
    params = getJP2ImageInputParameters(date=date_obj, sourceId=14, jpip=True, json=True, should_reject_this=True)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")
