from hvpy import getDataSources


def test_json_response():
    response = getDataSources()
    assert isinstance(response, dict)


def test_str_response():
    response = getDataSources(callback="callback")
    assert isinstance(response, str)
    assert response.startswith("callback(")


def test_enable_parameter():
    response = getDataSources(verbose=False, enable="[Yohkoh,STEREO_A,STEREO_B]")
    assert isinstance(response, dict)
