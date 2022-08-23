import pytest

from hvpy import DataSources
from hvpy.utils import _create_layer_string, _to_datasource, create_layers


def test_create_layers():
    assert create_layers([(9, 100), (11, 50)]) == "[9,1,100],[11,1,50]"

    with pytest.raises(ValueError, match="999 is not a valid DataSources"):
        create_layers([(9, 100), (999, 100)])

    with pytest.raises(ValueError, match="must be between 0 and 100"):
        create_layers([(9, 101), (14, 100)])

    with pytest.raises(ValueError, match="must be between 0 and 100"):
        create_layers([(9, 100), (14, -1)])


def test_to_datasource():
    assert _to_datasource(9) == DataSources.AIA_131
    assert _to_datasource(DataSources.AIA_94) == DataSources.AIA_94
    with pytest.raises(ValueError, match="999 is not a valid DataSources"):
        _to_datasource(999)


def test_create_layers_string():
    assert _create_layer_string(DataSources.AIA_131, 100) == "[9,1,100]"
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        _create_layer_string(DataSources.AIA_131, 101)
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        _create_layer_string(DataSources.AIA_131, -1)
