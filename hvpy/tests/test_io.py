import pytest

from hvpy.io import HvpyParameters, OutputType


def test_default_get_output_type():
    params = HvpyParameters()
    assert params.get_output_type() == OutputType.Raw


def test_get_output_type():
    class TestInputParameters(HvpyParameters):
        a: int

        def get_output_type(self):
            if self.a == 1:
                return OutputType.Raw
            else:
                return OutputType.String

    params = {"a": 1}
    params = TestInputParameters(**params)
    assert params.get_output_type() == OutputType.Raw

    params = {"a": 2}
    params = TestInputParameters(**params)
    assert params.get_output_type() == OutputType.String

    assert params.url == "https://api.helioviewer.org/v2/Test/"


def test_error_handling():
    error_message = "TestInputParameters\na\n  field required"

    class TestInputParameters(HvpyParameters):
        a: int

        def get_output_type(self):
            if self.a == 1:
                return OutputType.Raw
            else:
                return OutputType.String

    params = {"b": 1}
    with pytest.raises(ValueError, match=error_message):
        params = TestInputParameters(**params)
