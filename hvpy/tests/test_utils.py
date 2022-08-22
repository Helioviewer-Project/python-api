import pytest

from hvpy import create_layers


def test_create_layers():
    assert create_layers([(9, 100), (11, 50)]) == "[9,1,100],[11,1,50]"

    with pytest.raises(ValueError, match="opacity: -1 must be between 0 and 100"):
        create_layers([(9, 100), (14, -1)])

    with pytest.raises(ValueError, match="123 is not a valid DataSources"):
        create_layers([(9, 100), (123, 100)])
