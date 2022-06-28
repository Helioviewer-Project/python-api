from datetime import datetime

import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.core import execute_api_call


def test_str_response():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": True, "json": False}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": True, "json": True}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")


def test_raw_response():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": False, "json": False}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)


def test_raw_response_with_json():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": False, "json": True}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)


def test_default_response():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)


def test_error_handling():
    error_message = "getJP2ImageInputParameters\ndate\n  field required"

    params = {"sourceId": 14, "jpip": True, "json": True}
    with pytest.raises(ValidationError, match=error_message):
        params = getJP2ImageInputParameters(**params)


def test_unknown_parameters():
    date_obj = datetime(2022, 1, 1, 23, 59, 59)
    params = {"date": date_obj, "sourceId": 14, "jpip": True, "json": True, "should_reject_this": True}
    params = getJP2ImageInputParameters(**params)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")
