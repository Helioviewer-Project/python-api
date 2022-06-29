from hvpy.io import HvpyParameters, OutputType


def test_default_get_output_type_is_raw():
    params = HvpyParameters()
    assert params.get_output_type() == OutputType.Raw


def test_url_property():
    params = HvpyParameters()
    assert params.url == "https://api.helioviewer.org/v2//"
