from datetime import datetime

import pytest

from hvpy import getJP2Image


def test_getJP2Image():
    date_obj = datetime(2020, 1, 1)
    response = getJP2Image(date=date_obj, sourceId=1, json=True)
    assert isinstance(response, bytes)

    response = getJP2Image(date=date_obj, sourceId=1, jpip=True, json=False)
    assert isinstance(response, str)
    assert response.startswith("jpip://")

    response = getJP2Image(date=date_obj, sourceId=1, jpip=True, json=True)
    assert isinstance(response, dict)
    assert "uri" in response
    assert response["uri"].startswith("jpip://")

    response = getJP2Image(date=date_obj, sourceId=1, jpip=False, json=True)
    assert isinstance(response, bytes)


def test_invalid_inputs():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        getJP2Image(sourceId=1, json=True)

    with pytest.raises(TypeError, match="missing 1 required positional argument: 'sourceId'"):
        getJP2Image(date=datetime(2020, 1, 1), json=True)

    with pytest.raises(TypeError, match="missing 2 required positional arguments: 'date' and 'sourceId'"):
        getJP2Image(json=True)
