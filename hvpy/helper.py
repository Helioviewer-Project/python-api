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
    callback: Optional[str] = None,
    size: Optional[int] = None,
    movieIcons: Optional[int] = None,
    followViewport: Optional[int] = None,
    reqObservationDate: Optional[datetime] = None,
    overwrite: bool = False,
    filename: Union[str, Path] = None,
    hq: bool = False,
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
    """
    res = queueMovie(
        startTime=startTime,
        endTime=endTime,
        layers=layers,
        events=events,
        eventsLabels=eventsLabels,
        imageScale=imageScale,
        format=format,
        frameRate=frameRate,
        maxFrames=maxFrames,
        scale=scale,
        scaleType=scaleType,
        scaleX=scaleX,
        scaleY=scaleY,
        movieLength=movieLength,
        watermark=watermark,
        width=width,
        height=height,
        x0=x0,
        y0=y0,
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        callback=callback,
        size=size,
        movieIcons=movieIcons,
        followViewport=followViewport,
        reqObservationDate=reqObservationDate,
    )
    assert isinstance(res, dict)

    try:
        if res["error"] is not None:
            raise RuntimeError(res["error"])
    except KeyError:
        pass

    while True:
        status = getMovieStatus(
            id=res["id"],
            format=format,
            callback=callback,
            token=res["token"],
        )
        time.sleep(1)
        if status["status"] == 2:
            break

    binary_data = downloadMovie(
        id=res["id"],
        format=format,
        hq=hq,
    )

    if filename is None:
        filename = f"{startTime.isoformat()}_{endTime.isoformat()}"

    while True:
        try:
            save_file(
                data=binary_data,
                filename=f"{filename}.{format}",
                overwrite=overwrite,
            )
            break
        except FileExistsError:
            filename = f"{filename}(1)"

    return Path(f"{filename}.{format}")
