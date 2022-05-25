from hvpy import fake_api_call


def test_test_fake():
    assert True


def test_fake_api_call():
    assert fake_api_call() == {}
