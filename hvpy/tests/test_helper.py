from pathlib import Path
from datetime import datetime

import pytest

from hvpy.datasource import DataSource
from hvpy.helpers import createMovie
from hvpy.utils import create_events, create_layers


def test_createMovie(start_time, end_time, tmp_path):
    f1 = tmp_path / "movie"
    result = createMovie(
        startTime=start_time,
        endTime=end_time,
        layers=create_layers([(DataSource.AIA_171, 100)]),
        events=create_events(["AR"]),
        eventsLabels=True,
        imageScale=1,
        filename=f1,
    )
    assert isinstance(result, Path)
    assert result.exists()
    assert result == tmp_path / "movie.mp4"

    result = createMovie(
        startTime=start_time,
        endTime=end_time,
        layers=create_layers([(DataSource.AIA_171, 100)]),
        events=create_events(["AR"]),
        eventsLabels=True,
        imageScale=1,
        filename=f1,
        overwrite=True,
    )
    assert isinstance(result, Path)
    assert result.exists()
    assert result == tmp_path / "movie.mp4"


def test_createMovie_with_none_filename(start_time, end_time):
    result = createMovie(
        startTime=start_time,
        endTime=end_time,
        layers=create_layers([(DataSource.AIA_171, 100)]),
        events=create_events(["AR"]),
        eventsLabels=True,
        imageScale=1,
    )
    assert isinstance(result, Path)
    assert result.exists()
    result.unlink()  # clean up


def test_createMovie_timeout(start_time, end_time, tmp_path):
    f1 = tmp_path / "movie"
    with pytest.raises(RuntimeError):
        createMovie(
            startTime=start_time,
            endTime=end_time,
            layers=create_layers([(DataSource.AIA_171, 100)]),
            events=create_events(["AR"]),
            eventsLabels=True,
            imageScale=1,
            filename=f1,
            timeout=0.5,
        )


def test_error_handling2(tmp_path):
    f1 = tmp_path / "movie"
    with pytest.raises(RuntimeError):
        createMovie(
            startTime=datetime(2010, 1, 1),
            endTime=datetime(2010, 1, 2),
            layers=create_layers([(DataSource.AIA_171, 100)]),
            events=create_events(["AR"]),
            eventsLabels=True,
            imageScale=1,
            filename=f1,
        )


def test_error_handling(tmp_path):
    f1 = tmp_path / "movie"
    with pytest.raises(RuntimeError):
        createMovie(
            startTime=datetime(2010, 1, 1),
            endTime=datetime(2010, 1, 2),
            layers=create_layers([(DataSource.AIA_171, 100)]),
            events=create_events(["AR"]),
            eventsLabels=True,
            imageScale=1,
            filename=f1,
        )
