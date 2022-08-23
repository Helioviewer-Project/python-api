from typing import Any, Dict, List, Union, Optional
from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import *
from hvpy.utils import _add_shared_docstring

__all__ = [
    "getJP2Image",
    "getJP2Header",
    "getJPXClosestToMidPoint",
    "getJPX",
    "getStatus",
    "getClosestImage",
    "getDataSources",
    "takeScreenshot",
    "downloadScreenshot",
    "queueMovie",
    "reQueueMovie",
    "getMovieStatus",
    "downloadMovie",
    "getNewsFeed",
    "shortenURL",
    "getTile",
]


@_add_shared_docstring(getJP2ImageInputParameters)
def getJP2Image(
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Retrieve a JP2000 image from the helioviewer.org API.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getJP2Image
    >>> from datetime import datetime, timedelta
    >>> getJP2Image(date=datetime.today(), sourceId=14, jpip=True)
    'jpip://...'
    """
    params = getJP2ImageInputParameters(date=date, sourceId=sourceId, jpip=jpip, json=json)
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getJP2HeaderInputParameters)
def getJP2Header(
    id: int,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Get the XML header embedded in a JPEG2000 image. Includes the FITS header
    as well as a section of Helioviewer-specific metadata.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getJP2Header
    >>> getJP2Header(id=7654321,callback="xml_header")
    'xml_header(\\\'<?xml version="1.0" encoding="utf-8"?><meta><fits><SIMPLE>1</SIMPLE><BITPIX>16</BITPIX>...')'
    """
    params = getJP2HeaderInputParameters(id=id, callback=callback)
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getJPXClosestToMidPointInputParameters)
def getJPXClosestToMidPoint(
    startTimes: List[datetime],
    endTimes: List[datetime],
    sourceId: int,
    linked: bool = True,
    verbose: bool = False,
    jpip: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Generate and (optionally) download a custom JPX movie of the specified
    datasource with one frame per pair of start/endtimes given.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getJPXClosestToMidPoint
    >>> from datetime import datetime, timedelta
    >>> getJPXClosestToMidPoint(
    ...     startTimes=[datetime.today() - timedelta(days=15, minutes=5), datetime.today() - timedelta(days=16, minutes=5)],
    ...     endTimes=[datetime.today() - timedelta(days=15), datetime.today() - timedelta(days=16)],
    ...     sourceId=14,
    ...     linked=False,
    ...     jpip=True
    ... )
    'jpip://beta.helioviewer.org:8090/movies/SDO_AIA_335_...jpxmid'
    """
    params = getJPXClosestToMidPointInputParameters(
        startTimes=startTimes,
        endTimes=endTimes,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getJPXInputParameters)
def getJPX(
    startTime: List[datetime],
    endTime: List[datetime],
    sourceId: int,
    linked: bool = True,
    verbose: bool = False,
    jpip: bool = False,
    cadence: Optional[int] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Generate and (optionally) download a custom JPX movie of the specified
    datasource from the helioviewer.org API.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getJPX
    >>> from datetime import datetime, timedelta
    >>> getJPX(startTime=datetime.today() - timedelta(days=15, minutes=5),
    ...        endTime=datetime.today() - timedelta(days=15),
    ...        sourceId=14,
    ...        linked=False,
    ...        jpip=True,
    ...        verbose=False,
    ...        cadence=60)
    'jpip://beta.helioviewer.org:8090/movies/...'
    """
    params = getJPXInputParameters(
        startTime=startTime,
        endTime=endTime,
        sourceId=sourceId,
        linked=linked,
        verbose=verbose,
        jpip=jpip,
        cadence=cadence,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getStatusInputParameters)
def getStatus() -> Union[bytes, str, Dict[str, Any]]:
    """
    Returns information about how far behind the latest available JPEG2000
    images.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getStatus
    >>> getStatus()
    {'AIA': ..., 'COSMO': ..., 'EUI': ..., 'HMI': ..., 'LASCO': ..., 'SECCHI': ..., 'SWAP': ..., 'XRT': ...}
    """
    params = getStatusInputParameters()
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getClosestImageInputParameters)
def getClosestImage(
    date: datetime,
    sourceId: int,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Find the image data that is closest to the requested datetime.

    Return the associated metadata from the helioviewer database and the XML header of the JPEG2000 image file.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from datetime import datetime
    >>> from hvpy import getClosestImage
    >>> getClosestImage(
    ...     date=datetime.today(),
    ...     sourceId=14,
    ... )
    {'id': '...', 'date': '...', 'name': '...', ...}
    """
    params = getClosestImageInputParameters(date=date, sourceId=sourceId, callback=callback)
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getDataSourcesInputParameters)
def getDataSources(
    verbose: Optional[bool] = False,
    enable: Optional[str] = None,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Return a hierarchial list of the available datasources.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getDataSources
    >>> getDataSources()
    {'GOES-R': {'SUVI': {...: {'sourceId': ..., 'nickname': 'GOES-R SUVI 94', 'layeringOrder': 1, 'start': ..., 'end': ..., 'uiLabels': [{'label': 'Observatory', 'name': 'GOES-R'}, {'label': 'Detector', 'name': 'SUVI'}, ...}
    """
    params = getDataSourcesInputParameters(
        verbose=verbose,
        enable=enable,
        callback=callback,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(takeScreenshotInputParameters)
def takeScreenshot(
    date: datetime,
    imageScale: float,
    layers: str,
    events: Optional[str] = None,
    eventLabels: Optional[bool] = False,
    scale: Optional[bool] = False,
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
    display: Optional[bool] = False,
    watermark: Optional[bool] = False,
    callback: Optional[str] = None,
):
    """
    Generate a custom screenshot.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import takeScreenshot
    >>> from datetime import datetime
    >>> takeScreenshot(
    ...     date=datetime.today(),
    ...     imageScale=2.44,
    ...     layers="[10,1,100]",
    ...     x0=0,
    ...     y0=0,
    ...     width=1920,
    ...     height=1200,
    ... )
    {'id': ...}
    """
    params = takeScreenshotInputParameters(
        date=date,
        imageScale=imageScale,
        layers=layers,
        events=events,
        eventLabels=eventLabels,
        scale=scale,
        scaleType=scaleType,
        scaleX=scaleX,
        scaleY=scaleY,
        width=width,
        height=height,
        x0=x0,
        y0=y0,
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        display=display,
        watermark=watermark,
        callback=callback,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(downloadScreenshotInputParameters)
def downloadScreenshot(id: int) -> Union[bytes, str, Dict[str, Any]]:
    """
    Download a custom screenshot that was generated using the
    ``takeScreenshot`` API endpoint.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import downloadScreenshot
    >>> downloadScreenshot(id=26728529)
    b'...'
    """
    params = downloadScreenshotInputParameters(id=id)
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(queueMovieInputParameters)
def queueMovie(
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
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Queue a movie for download from the helioviewer.org API.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import queueMovie
    >>> from datetime import datetime, timedelta
    >>> queueMovie(
    ...     startTime=datetime.today() - timedelta(days=15, minutes=5),
    ...     endTime=datetime.today() - timedelta(days=15),
    ...     layers="[12,7,22],[13,7,11]",
    ...     events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
    ...     eventsLabels=False,
    ...     imageScale=2.44,
    ... )
    {'id': ...}
    """
    params = queueMovieInputParameters(
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
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(reQueueMovieInputParameters)
def reQueueMovie(
    id: str,
    force: Optional[bool] = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Re-generate a custom movie that is no longer cached on the server.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import reQueueMovie        # doctest: +SKIP
    >>> reQueueMovie(id="gxRN5", force=True) # doctest: +SKIP
    {'id': 'gxRN5', 'eta': 274, 'queue': 0, 'token': '...'}
    """
    params = reQueueMovieInputParameters(
        id=id,
        force=force,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getMovieStatusInputParameters)
def getMovieStatus(
    id: str,
    format: str,
    verbose: Optional[bool] = False,
    callback: Optional[str] = None,
    token: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Get the status of a movie.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getMovieStatus
    >>> getMovieStatus(id="h2n6n", format="mp4")
    {'frameRate': ..., 'numFrames': ..., 'startDate': '...', 'status': ..., 'endDate': '...', 'width': ..., 'height': ..., 'title': '...', 'thumbnails': {'icon': '...', 'small': '...', 'medium': '...', 'large': '...', 'full': '...'}, 'url': '...', 'statusLabel': 'Completed'}
    """
    params = getMovieStatusInputParameters(
        id=id,
        format=format,
        verbose=verbose,
        callback=callback,
        token=token,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(downloadMovieInputParameters)
def downloadMovie(
    id: str,
    format: str,
    hq: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Download a custom movie that was generated using the ``queueMovie`` API
    endpoint.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import downloadMovie
    >>> downloadMovie(id="h2n6n", format="mp4")
    b'...'
    """
    params = downloadMovieInputParameters(
        id=id,
        format=format,
        hq=hq,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getNewsFeedInputParameters)
def getNewsFeed(
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Get the XML RSS feed of the official Helioviewer Project Blog.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getNewsFeed
    >>> getNewsFeed()
    '<?xml version="1.0" encoding="utf-8"?><feed xmlns="..." >...</summary></entry></feed>'
    """
    params = getNewsFeedInputParameters(
        callback=callback,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(shortenURLInputParameters)
def shortenURL(
    queryString: str,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Shorten a Helioviewer.org URL with the bit.ly URL shortening web service.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import shortenURL
    >>> shortenURL(queryString="https://api.helioviewer.org/v2/queueMovie/?startTime=2010-03-01T12:12:12Z&endTime=2010-03-04T12:12:12Z")
    {'status_code': ..., 'status_txt': 'OK', 'data': {'long_url': ..., 'url': ...}}
    """
    params = shortenURLInputParameters(
        queryString=queryString,
        callback=callback,
    )
    return execute_api_call(input_parameters=params)


@_add_shared_docstring(getTileInputParameters)
def getTile(
    id: int,
    x: int,
    y: int,
    imageScale: int,
    difference: Optional[int] = None,
    diffCount: Optional[int] = None,
    diffTime: Optional[int] = None,
    baseDiffTime: Optional[datetime] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Request a single image tile to be used in the Helioviewer.org Viewport.
    Tiles are 512x512 pixel PNG images, generated for a given image scale from
    the intermediary JPEG2000 image files.

    Use the ``getClosestImage`` API endpoint to obtain the desired image identifier for the id parameter.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getTile
    >>> getTile(id=36275490,
    ...         x=-1,
    ...         y=-1,
    ...         imageScale=2,
    ...         )
    b'...'
    """
    params = getTileInputParameters(
        id=id,
        x=x,
        y=y,
        imageScale=imageScale,
        difference=difference,
        diffCount=diffCount,
        diffTime=diffTime,
        baseDiffTime=baseDiffTime,
    )
    return execute_api_call(input_parameters=params)
