import pytest
from pydantic import ValidationError

from hvpy.api_groups.jpeg2000.get_jp2_header import getJP2HeaderInputParameters
from hvpy.core import execute_api_call


def test_getJP2HeaderInputParameters():
    params = getJP2HeaderInputParameters(id=9838343)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)

    params = getJP2HeaderInputParameters(id=9838343, callback="my_callback")
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, str)
    assert response.startswith("my_callback(")


def test_error_handling():
    with pytest.raises(ValidationError, match="getJP2HeaderInputParameters\nid\n  field required"):
        getJP2HeaderInputParameters(callback="my_callback")


def test_url_property():
    params = getJP2HeaderInputParameters(id=9838343)
    assert params.url == "https://api.helioviewer.org/v2/getJP2Header/"


def test_unknown_parameters():
    params = getJP2HeaderInputParameters(id=9838343, should_reject_this=True)
    response = execute_api_call(input_parameters=params)
    assert isinstance(response, bytes)
