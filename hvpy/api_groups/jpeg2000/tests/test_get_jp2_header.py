import os

import pytest

import hvpy
from hvpy import getJP2Header
from hvpy.api_groups.jpeg2000.get_jp2_header import getJP2HeaderInputParameters


def test_getJP2HeaderInputParameters():
    response = getJP2Header(id=9838343)
    assert isinstance(response, str)
    assert response.startswith("<?xml")
    assert response.endswith("</meta>")

    response = getJP2Header(id=9838343, callback="my_callback")
    assert isinstance(response, str)
    assert response.startswith("my_callback(")


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        getJP2Header(callback="my_callback")


def test_url_property():
    params = getJP2HeaderInputParameters(id=9838343)
    assert params.url == "https://api.helioviewer.org/v2/getJP2Header/"


def test_set_api():
    params = getJP2HeaderInputParameters(id=9838343)
    assert params.url == "https://api.helioviewer.org/v2/getJP2Header/"

    hvpy.set_api("https://api.beta.helioviewer.org/")
    params = getJP2HeaderInputParameters(id=9838343)
    assert params.url == "https://api.beta.helioviewer.org/getJP2Header/"

    os.environ["URL"] = "https://localhost:3000/"
    hvpy.set_api()
    params = getJP2HeaderInputParameters(id=9838343)
    assert params.url == "https://localhost:3000/getJP2Header/"
