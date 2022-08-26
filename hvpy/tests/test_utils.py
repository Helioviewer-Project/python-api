import pytest

from hvpy import DataSource, EventType
from hvpy.utils import (
    _create_events_string,
    _create_layer_string,
    _to_datasource,
    _to_event_type,
    create_events,
    create_layers,
)


def test_create_layers():
    assert create_layers([(9, 100), (11, 50)]) == "[9,1,100],[11,1,50]"
    with pytest.raises(ValueError, match="999 is not a valid DataSource"):
        create_layers([(9, 100), (999, 100)])
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        create_layers([(9, 101), (14, 100)])
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        create_layers([(9, 100), (14, -1)])


def test_to_datasource():
    assert _to_datasource(9) == DataSource.AIA_131
    assert _to_datasource(DataSource.AIA_94) == DataSource.AIA_94
    with pytest.raises(ValueError, match="999 is not a valid DataSource"):
        _to_datasource(999)


def test_create_layers_string():
    assert _create_layer_string(DataSource.AIA_131, 100) == "[9,1,100]"
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        _create_layer_string(DataSource.AIA_131, 101)
    with pytest.raises(ValueError, match="must be between 0 and 100"):
        _create_layer_string(DataSource.AIA_131, -1)


def test_to_event_type():
    assert _to_event_type("AR") == EventType.ACTIVE_REGION
    assert _to_event_type(EventType.ACTIVE_REGION) == EventType.ACTIVE_REGION


def test_create_events():
    assert create_events([(EventType.ACTIVE_REGION, "SPoCA;NOAA_SWPC_Observer")]) == "[AR,SPoCA;NOAA_SWPC_Observer,1]"
    assert create_events([(EventType.ACTIVE_REGION)]) == "[AR,all,1]"
    assert create_events([("ER")]) == "[ER,all,1]"
    with pytest.raises(ValueError, match="XYZ is not a valid EventType"):
        create_events([("XYZ")])
    assert (
        create_events([(EventType.ACTIVE_REGION, "SPoCA"), ("ER", "NOAA_SWPC_Observer")])
        == "[AR,SPoCA,1],[ER,NOAA_SWPC_Observer,1]"
    )


def test_create_events_string():
    assert _create_events_string(EventType.ACTIVE_REGION) == "[AR,all,1]"
    assert _create_events_string(EventType.ACTIVE_REGION, "xyz") == "[AR,xyz,1]"
