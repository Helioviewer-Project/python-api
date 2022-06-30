import pytest

from hvpy.core import parse_response


def test_wrong_input_type():
    with pytest.raises(ValueError, match="Unknown output type: 42"):
        parse_response(None, 42)
