from datetime import datetime

import pytest

from hvpy import create_events, create_layers, createMovie
from hvpy.datasource import DataSource


def test_create_movie(start_time, end_time, tmp_path):
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
    )
    assert result.exists()
    assert result == tmp_path / "movie(1).mp4"

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
    assert result.exists()
    assert result == tmp_path / "movie.mp4"


def test_create_movie_with_none_filename(start_time, end_time):
    result = createMovie(
        startTime=start_time,
        endTime=end_time,
        layers=create_layers([(DataSource.AIA_171, 100)]),
        events=create_events(["AR"]),
        eventsLabels=True,
        imageScale=1,
    )
    assert result.exists()


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
