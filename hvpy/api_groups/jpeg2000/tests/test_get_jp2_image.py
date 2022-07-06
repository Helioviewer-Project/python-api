from datetime import datetime

import pytest

from hvpy import getJP2Image
from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters


def test_str_response():
    response = getJP2Image(date=datetime(2022, 1, 1, 23, 59, 59), sourceId=14, jpip=True, json=False)
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    response = getJP2Image(date=datetime(2022, 1, 1, 23, 59, 59), sourceId=14, jpip=True, json=True)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")


def test_raw_response():
    response = getJP2Image(date=datetime(2022, 1, 1, 23, 59, 59), sourceId=14, jpip=False, json=False)
    assert isinstance(response, bytes)


def test_raw_response_with_json():
    response = getJP2Image(date=datetime(2022, 1, 1, 23, 59, 59), sourceId=14, jpip=False, json=True)
    assert isinstance(response, bytes)


def test_default_response():
    response = getJP2Image(date=datetime(2022, 1, 1, 23, 59, 59), sourceId=14)
    assert isinstance(response, bytes)


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        getJP2Image(sourceId=14, jpip=True, json=True)


def test_unknown_parameters():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": True, "json": True, "should_reject_this": True}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")


def test_url_property():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": True, "json": True}
    params = getJP2ImageInputParameters(**params)
    assert params.url == "https://api.helioviewer.org/v2/getJP2Image/"
