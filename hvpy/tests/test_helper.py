from pathlib import Path

from hvpy import create_events, create_layers, createMovie
from hvpy.datasource import DataSource


def test_create_movie(start_time, end_time, tmp_path):
    f1 = tmp_path / "movie"
    createMovie(
        startTime=start_time,
        endTime=end_time,
        layers=create_layers([(DataSource.AIA_131, 50)]),
        events=create_events(["AR"]),
        eventsLabels=True,
        imageScale=1,
        filename=f1,
    )
    assert Path(f"{f1}.mp4").exists()
