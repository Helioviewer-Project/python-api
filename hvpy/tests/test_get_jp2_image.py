from datetime import datetime

from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.core import execute_api_call


def test_get_jp2_image_str():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, str)


def test_get_jp2_image_json():
    date = datetime(2022, 1, 1, 23, 59, 59)
    input = {"date": date, "sourceId": 14}
    input = getJP2ImageInputParameters(**input)
    response = execute_api_call(input_parameters=input)
    assert isinstance(response, dict)
