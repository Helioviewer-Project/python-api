from datetime import datetime

from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.core import execute_api_call


def test_str_response():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14, "jpip": True, "Json": False}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, str)
    assert response.startswith('jpip://')


def test_json_response():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14, "jpip": True, "Json": True}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, dict)
    assert 'uri' in response
    assert response['uri'].startswith('jpip://')


def test_raw_response():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14, "jpip": False, "Json": False}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, bytes)


def test_default_response():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, bytes)
