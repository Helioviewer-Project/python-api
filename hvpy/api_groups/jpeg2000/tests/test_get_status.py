from hvpy.api_groups.jpeg2000.get_status import getStatusInputParameters
from hvpy.core import execute_api_call


def test_getStatusInputParameters():
    params = getStatusInputParameters()
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, dict)


def test_url_property():
    params = getStatusInputParameters()
    assert params.url == "https://api.helioviewer.org/v2/getStatus/"
