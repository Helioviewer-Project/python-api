from datetime import datetime

import pytest

from hvpy import getClosestImage
from hvpy.api_groups.official_clients.get_closest_image import getClosestImageInputParameters


def test_json_res():
    response = getClosestImage(date=datetime(2014, 1, 1, 23, 59, 59), sourceId=14)
    assert isinstance(response, dict)


def test_str_res():
    response = getClosestImage(date=datetime(2014, 1, 1, 23, 59, 59), sourceId=14, callback="callback")
    assert isinstance(response, str)
    assert response.startswith("callback")


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        getClosestImage(sourceId=14)
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getClosestImage(date=datetime(2014, 1, 1, 23, 59, 59))


def test_url_property():
    params = getClosestImageInputParameters(date=datetime(2014, 1, 1, 23, 59, 59), sourceId=14)
    assert params.url == "https://api.beta.helioviewer.org/v2/getClosestImage/"
