from datetime import datetime

from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.core import execute_api_call
from hvpy.io import BASE_URL

URL = BASE_URL + "getJP2Image/"


def test_get_jp2_image():

    DATE = datetime(2022, 1, 1, 23, 59, 59)

    input = {"date": DATE, "sourceId": 14}
    input = getJP2ImageInputParameters(**input)

    r = execute_api_call(url=URL, input_parameters=input)

    assert isinstance(r, str)
