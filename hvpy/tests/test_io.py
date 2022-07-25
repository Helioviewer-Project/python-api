from hvpy import set_api_url
from hvpy.io import HvpyParameters, OutputType


def test_default_get_output_type_is_raw():
    params = HvpyParameters()
    assert params.get_output_type() == OutputType.RAW


def test_url_property():
    params = HvpyParameters()
    assert params.url == "https://api.helioviewer.org/v2//"


def test_set_url():
    # This is not safe if we ever decide to parallelize the tests.
    params_first = HvpyParameters()
    assert params_first.url == "https://api.helioviewer.org/v2//"

    set_api_url("https://api.beta.helioviewer.org/")
    params_second = HvpyParameters()
    assert params_second.url == "https://api.beta.helioviewer.org//"

    assert params_first.url == params_second.url
    set_api_url("https://api.helioviewer.org/v2/")


def test_set_url_env(env):
    env.set("HELIOVIEWER_API_URL", "https://fake_env_url/")

    from hvpy.config import Settings

    assert Settings().api_url == "https://fake_env_url/"
