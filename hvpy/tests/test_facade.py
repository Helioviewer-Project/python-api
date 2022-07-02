from datetime import datetime

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
