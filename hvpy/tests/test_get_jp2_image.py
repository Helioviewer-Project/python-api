from hvpy.io import BASE_URL
from datetime import datetime
from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters
from hvpy.io import OutputType, execute_api_call

URL = BASE_URL + "getJP2Image/"


def test_get_jp2_image():

    DATE = datetime(2022, 1, 1, 23, 59, 59)

    input = {"date": DATE, "sourceId": 14}
    input = getJP2ImageInputParameters(**input)

    output = OutputType.String
    r = execute_api_call(url=URL, input_parameters=input.dict(), output_type=output)

    assert isinstance(r, str)
