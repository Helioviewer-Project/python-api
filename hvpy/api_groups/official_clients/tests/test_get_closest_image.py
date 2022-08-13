import pytest

from hvpy import getClosestImage
from hvpy.api_groups.official_clients.get_closest_image import getClosestImageInputParameters


def test_json_res(date):
    response = getClosestImage(date=date, sourceId=14)
    assert isinstance(response, dict)


def test_str_res(date):
    response = getClosestImage(date=date, sourceId=14, callback="callback")
    assert isinstance(response, str)
    assert response.startswith("callback")


def test_error_handling(date):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        getClosestImage(sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getClosestImage(date=date)


def test_url_property(date):
    params = getClosestImageInputParameters(date=date, sourceId=14)
    assert params.url == "https://api.beta.helioviewer.org/v2/getClosestImage/"
