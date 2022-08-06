from hvpy import set_api_url
from hvpy.io import HvpyParameters, OutputType


def test_default_get_output_type_is_raw():
    params = HvpyParameters()
    assert params.get_output_type() == OutputType.RAW


def test_url_property():
    params = HvpyParameters()
    assert params.url == "https://api.beta.helioviewer.org/v2//"


def test_set_url():
    # This is not safe if we ever decide to parallelize the tests.
    params_first = HvpyParameters()
    assert params_first.url == "https://api.beta.helioviewer.org/v2//"

    set_api_url("https://api.beta.helioviewer.org/")
    params_second = HvpyParameters()
    assert params_second.url == "https://api.beta.helioviewer.org//"
    assert params_first.url == params_second.url

    set_api_url("https://api.beta.helioviewer.org/v2/")


def test_set_url_env(env):
    env.set("HELIOVIEWER_API_URL", "https://fake_env_url/")

    # We need to instantiate a new Settings since the environmental variable
    # is only read at init. Therefore using the live one in a test is tricky.
    from hvpy.config import LiveSettings, Settings

    temp_config = Settings()
    assert temp_config.api_url == "https://fake_env_url/"
    assert temp_config.api_url != LiveSettings.api_url

    set_api_url("https://api.beta.helioviewer.org/")
    params = HvpyParameters()
    assert params.url == "https://api.beta.helioviewer.org//"
    assert LiveSettings.api_url == "https://api.beta.helioviewer.org/"

    set_api_url("https://api.beta.helioviewer.org/v2/")
