import time
from typing import Union, Optional
from pathlib import Path
from datetime import datetime

from hvpy import downloadMovie, getMovieStatus, queueMovie
from hvpy.api_groups.movies.queue_movie import queueMovieInputParameters
from hvpy.utils import _add_shared_docstring, save_file

__all__ = [
    "createMovie",
]


@_add_shared_docstring(queueMovieInputParameters)
def createMovie(
    startTime: datetime,
    endTime: datetime,
    layers: str,
    events: str,
    eventsLabels: bool,
    imageScale: float,
    format: Optional[str] = "mp4",
    frameRate: Optional[str] = "15",
    maxFrames: Optional[str] = None,
    scale: Optional[bool] = None,
    scaleType: Optional[str] = None,
    scaleX: Optional[float] = None,
    scaleY: Optional[float] = None,
    movieLength: Optional[float] = None,
    watermark: Optional[bool] = True,
    width: Optional[str] = None,
    height: Optional[str] = None,
    x0: Optional[str] = None,
    y0: Optional[str] = None,
    x1: Optional[str] = None,
    y1: Optional[str] = None,
    x2: Optional[str] = None,
    y2: Optional[str] = None,
    size: Optional[int] = None,
    movieIcons: Optional[int] = None,
    followViewport: Optional[int] = None,
    reqObservationDate: Optional[datetime] = None,
    overwrite: bool = False,
    filename: Union[str, Path] = None,
    hq: bool = False,
    timeout: float = 5,
) -> Path:
    """
    Automatically creates a movie using the endpoint `queueMovie`,
    `getMovieStatus` and `downloadMovie`.

    Parameters
    ----------
    {Insert}
    overwrite
        Whether to overwrite the file if it already exists.
        Default is `False`.
    filename
        The path to save the file to.
        Optional, will default to ``f"{starttime}_{endtime}.{format}"``.
    hq
        Download a higher-quality movie file (valid for "mp4" movies only, ignored otherwise).
        Default is `False`, optional.
    timeout
        The timeout in minutes to wait for the movie to be created.
        Default is 5 minutes.
    """
    input_params = locals()
    # These are used later on but we want to avoid passing
    # them into queueMovie.
    input_params.pop("overwrite")
    input_params.pop("filename")
    input_params.pop("hq")
    input_params.pop("timeout")

    res = queueMovie(**input_params)

    if res.get("error"):
        raise RuntimeError(res["error"])

    timeout_counter = time.time() + 60 * timeout  # Default 5 minutes
    while True:
        status = getMovieStatus(
            id=res["id"],
            format=format,
            token=res["token"],
        )
        if status["status"] in [0, 1]:
            time.sleep(5)
        if status["status"] == 2:
            break
        if time.time() > timeout_counter:
            raise RuntimeError(f"Exceeded timeout of {timeout} minutes.")
        if status["status"] == 3:
            raise RuntimeError(status["error"])

    binary_data = downloadMovie(
        id=res["id"],
        format=format,
        hq=hq,
    )

    if filename is None:
        filename = f"{startTime.date()}_{endTime.date()}.{format}"
    else:
        filename = f"{filename}.{format}"

    save_file(
        data=binary_data,
        filename=filename,
        overwrite=overwrite,
    )

    return Path(filename)
