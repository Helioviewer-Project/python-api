import pytest

from hvpy import getJP2Image
from hvpy.api_groups.jpeg2000.get_jp2_image import getJP2ImageInputParameters


def test_str_response(date):
    response = getJP2Image(date=date, sourceId=14, jpip=True, json=False)
    assert isinstance(response, str)
    assert response.startswith("jpip://")


def test_json_response(date):
    response = getJP2Image(date=date, sourceId=14, jpip=True, json=True)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")


def test_raw_response(date):
    response = getJP2Image(date=date, sourceId=14, jpip=False, json=False)
    assert isinstance(response, bytes)


def test_raw_response_with_json(date):
    response = getJP2Image(date=date, sourceId=14, jpip=False, json=True)
    assert isinstance(response, bytes)


def test_default_response(date):
    response = getJP2Image(date=date, sourceId=14)
    assert isinstance(response, bytes)


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        getJP2Image(sourceId=14, jpip=True, json=True)


def test_url_property(date):
    params = {"date": date, "sourceId": 14, "jpip": True, "json": True}
    params = getJP2ImageInputParameters(**params)
    assert params.url == "https://api.beta.helioviewer.org/v2/getJP2Image/"
