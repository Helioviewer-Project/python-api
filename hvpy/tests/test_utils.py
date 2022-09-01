from datetime import datetime

import pytest

from hvpy import DataSource, EventType, takeScreenshot
from hvpy.utils import (
    _create_events_string,
    _create_layer_string,
    _to_datasource,
    _to_event_type,
    create_events,
    create_layers,
    save_file,
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
    assert _to_event_type(EventType.ACTIVE_REGION) == _to_event_type("AR") == EventType.ACTIVE_REGION


def test_create_events():
    assert create_events(["ER"]) == "[ER,all,1]"
    assert create_events([EventType.ACTIVE_REGION]) == "[AR,all,1]"
    assert create_events([(EventType.ACTIVE_REGION, "SPoCA;NOAA_SWPC_Observer")]) == "[AR,SPoCA;NOAA_SWPC_Observer,1]"
    assert create_events([EventType.ACTIVE_REGION, EventType.CORONAL_DIMMING]) == "[AR,all,1],[CD,all,1]"
    assert (
        create_events([(EventType.ACTIVE_REGION, "ZXCV"), (EventType.CORONAL_DIMMING, "ZXCV")])
        == "[AR,ZXCV,1],[CD,ZXCV,1]"
    )
    assert create_events([EventType.ACTIVE_REGION, (EventType.CORONAL_DIMMING, "ASDF")]) == "[AR,all,1],[CD,ASDF,1]"
    assert create_events([(EventType.ACTIVE_REGION, "ASDF"), EventType.CORONAL_DIMMING]) == "[AR,ASDF,1],[CD,all,1]"
    assert (
        create_events([(EventType.ACTIVE_REGION, "SPoCA"), ("ER", "NOAA_SWPC_Observer")])
        == "[AR,SPoCA,1],[ER,NOAA_SWPC_Observer,1]"
    )
    assert create_events([("AR", "SPoCA"), ("ER", "NOAA_SWPC_Observer")]) == "[AR,SPoCA,1],[ER,NOAA_SWPC_Observer,1]"
    with pytest.raises(ValueError, match="XYZ is not a valid EventType"):
        create_events(["XYZ"])
    with pytest.raises(ValueError, match="is not a EventType or str or two-length tuple"):
        create_events([("AR", "SPoCA", 123)])


def test_create_events_string():
    assert _create_events_string(EventType.ACTIVE_REGION) == "[AR,all,1]"
    assert _create_events_string(EventType.ACTIVE_REGION, "xyz") == "[AR,xyz,1]"


def test_save_file(tmp_path):
    f1 = tmp_path / "test.png"
    res = takeScreenshot(
        date=datetime.today(),
        imageScale=2.44,
        layers="[10,1,100]",
        x0=0,
        y0=0,
        width=1920,
        height=1200,
        display=True,
    )
    save_file(res, f1, overwrite=False)
    assert f1.exists()
    with pytest.raises(ValueError, match="already exists"):
        save_file(res, f1, overwrite=False)
    save_file(res, f1, overwrite=True)
    assert f1.exists()

    f2 = tmp_path / "test2.png"
    save_file(res, str(f2), overwrite=False)
    assert f2.exists()
