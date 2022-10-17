import time
from typing import Union, Optional
from pathlib import Path
from datetime import datetime

from hvpy.api_groups.movies.queue_movie import queueMovieInputParameters
from hvpy.api_groups.screenshots.take_screenshot import takeScreenshotInputParameters
from hvpy.facade import downloadMovie, downloadScreenshot, getMovieStatus, queueMovie, takeScreenshot
from hvpy.utils import _add_shared_docstring, save_file

__all__ = [
    "createMovie",
    "createScreenshot",
]


@_add_shared_docstring(queueMovieInputParameters)
def createMovie(
    startTime: datetime,
    endTime: datetime,
    layers: str,
    events: str,
    eventsLabels: bool,
    imageScale: float,
    format: str = "mp4",
    frameRate: str = "15",
    maxFrames: Optional[str] = None,
    scale: Optional[bool] = None,
    scaleType: Optional[str] = None,
    scaleX: Optional[float] = None,
    scaleY: Optional[float] = None,
    movieLength: Optional[float] = None,
    watermark: bool = True,
    width: Optional[str] = None,
    height: Optional[str] = None,
    x0: Optional[str] = None,
    y0: Optional[str] = None,
    x1: Optional[str] = None,
    y1: Optional[str] = None,
    x2: Optional[str] = None,
    y2: Optional[str] = None,
    size: int = 0,
    movieIcons: Optional[int] = None,
    followViewport: Optional[int] = None,
    reqObservationDate: Optional[datetime] = None,
    overwrite: bool = False,
    filename: Optional[Union[str, Path]] = None,
    hq: bool = False,
    timeout: float = 5,
) -> Path:
    """
    Automatically creates a movie using `queueMovie`, `getMovieStatus` and
    `downloadMovie` functions.

    Parameters
    ----------
    overwrite
        Whether to overwrite the file if it already exists.
        Default is `False`.
    filename
        The path to save the file to.
        Optional, will default to ``f"{res['title']}.{format}"``.
    hq
        Download a higher-quality movie file (valid for "mp4" movies only, ignored otherwise).
        Default is `False`, optional.
    timeout
        The timeout in minutes to wait for the movie to be created.
        Default is 5 minutes.
    {Insert}

    Examples
    --------
    >>> from hvpy import createMovie, DataSource, create_events, create_layers
    >>> from datetime import datetime, timedelta
    >>> movie_location = createMovie(
    ...     startTime=datetime.today() - timedelta(days=15, minutes=5),
    ...     endTime=datetime.today() - timedelta(days=15),
    ...     layers=create_layers([(DataSource.AIA_171, 100)]),
    ...     events=create_events(["AR"]),
    ...     eventsLabels=True,
    ...     imageScale=1,
    ...     filename="my_movie",
    ... )
    >>> # This is to cleanup the file created from the example
    >>> # you don't need to do this
    >>> from pathlib import Path
    >>> Path('my_movie.mp4').unlink()
    """
    input_params = locals()
    # These are used later on but we want to avoid passing
    # them into queueMovie.
    overwrite = input_params.pop("overwrite")
    filename = input_params.pop("filename")
    hq = input_params.pop("hq")
    timeout = input_params.pop("timeout")
    res = queueMovie(**input_params)
    if res.get("error"):
        raise RuntimeError(res["error"])
    timeout_counter = time.time() + 60 * timeout  # Default 5 minutes
    title = ""
    while True:
        status = getMovieStatus(
            id=res["id"],
            format=format,
            token=res["token"],
        )
        if status["status"] in [0, 1]:
            time.sleep(3)
        if status["status"] == 2:
            title = status["title"]
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
        filename = f"{title}.{format}"
    else:
        filename = f"{filename}.{format}"
    filename = save_file(
        data=binary_data,
        filename=filename,
        overwrite=overwrite,
    )
    return filename


@_add_shared_docstring(takeScreenshotInputParameters)
def createScreenshot(
    date: datetime,
    imageScale: float,
    layers: str,
    events: Optional[str] = None,
    eventLabels: bool = False,
    scale: bool = False,
    scaleType: Optional[str] = None,
    scaleX: Optional[int] = None,
    scaleY: Optional[int] = None,
    width: Optional[str] = None,
    height: Optional[str] = None,
    x0: Optional[str] = None,
    y0: Optional[str] = None,
    x1: Optional[str] = None,
    y1: Optional[str] = None,
    x2: Optional[str] = None,
    y2: Optional[str] = None,
    watermark: bool = False,
    overwrite: bool = False,
    filename: Optional[Union[str, Path]] = None,
) -> Path:
    """
    Automatically creates a screenshot using `takeScreenshot`,
    `downloadScreenshot` functions.

    Parameters
    ----------
    overwrite
        Whether to overwrite the file if it already exists.
        Default is `False`.
    filename
        The path to save the file to.
        Optional, will default to ``f"{res['id']}_{date.date()}.png"``.
    {Insert}

    Examples
    --------
    >>> from hvpy import createScreenshot, DataSource, create_events, create_layers, EventType
    >>> from datetime import datetime, timedelta
    >>> screenshot_location = createScreenshot(
    ...     date=datetime.today() - timedelta(days=15),
    ...     layers=create_layers([(DataSource.AIA_171, 100)]),
    ...     events=create_events([EventType.ACTIVE_REGION]),
    ...     eventLabels=True,
    ...     imageScale=1,
    ...     x0=0,
    ...     y0=0,
    ...     width=100,
    ...     height=100,
    ...     filename="my_screenshot",
    ... )
    >>> # This is to cleanup the file created from the example
    >>> # you don't need to do this
    >>> from pathlib import Path
    >>> Path('my_screenshot.png').unlink()
    """
    input_params = locals()
    # These are used later on but we want to avoid passing
    # them into takeScreenshot.
    input_params.pop("overwrite")
    input_params.pop("filename")
    res = takeScreenshot(**input_params)
    if res.get("error"):
        raise RuntimeError(res["error"])
    binary_data = downloadScreenshot(
        id=res["id"],
    )
    if filename is None:
        filename = f"{res['id']}_{date.date()}.png"
    else:
        filename = f"{filename}.png"
    filename = save_file(
        data=binary_data,
        filename=filename,
        overwrite=overwrite,
    )
    return filename
