from hvpy.io import HvpyParameters, OutputType


def test_default_get_output_type_is_raw():
    params = HvpyParameters()
    assert params.get_output_type() == OutputType.Raw


def test_url_property():
    class MockInputParameters(HvpyParameters):
        jpip: bool

    params = {"jpip": True}
    params = MockInputParameters(**params)
    assert params.url == "https://api.helioviewer.org/v2/Mock/"
