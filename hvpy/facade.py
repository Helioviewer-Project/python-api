from typing import Any, Dict, List, Union, Optional
from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import *
from hvpy.utils import add_shared_docstring


__all__ = [
    "getJP2Image",
    "getJP2Header",
    "getJPXClosestToMidPoint",
    "getJPX",
    "getStatus",
    "getClosestImage",
    "getDataSources",
]



@add_shared_docstring(getJP2ImageInputParameters)
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
    >>> getJP2Image(date=datetime(2019,1,1), sourceId=1, jpip=True)
    'jpip://helioviewer.org:8090/EIT/2013/08/07/195/2013_08_07__01_13_50_146__SOHO_EIT_EIT_195.jp2'
    """
    params = getJP2ImageInputParameters(date=date, sourceId=sourceId, jpip=jpip, json=json)
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getJP2HeaderInputParameters)
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
    >>> getJP2Header(id=9838343,callback="xml_header")
    'xml_header(\\\'<?xml version="1.0" encoding="utf-8"?><meta><fits><SIMPLE>1</SIMPLE><BITPIX>16</BITPIX>...')'
    """
    params = getJP2HeaderInputParameters(id=id, callback=callback)
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getJPXClosestToMidPointInputParameters)
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
    datasource with one frame per pair of startTimes/endTimes parameters.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from hvpy import getJPXClosestToMidPoint
    >>> from datetime import datetime
    >>> getJPXClosestToMidPoint(
    ...     startTimes=[datetime(2014, 1, 1, 0, 0, 0), datetime(2014, 1, 1, 2, 3, 3)],
    ...     endTimes=[datetime(2014, 1, 1, 0, 45, 0), datetime(2014, 1, 1, 2, 33, 3)],
    ...     sourceId=14,
    ...     linked=False,
    ...     jpip=True
    ... )
    'jpip://helioviewer.org:8090/movies/SDO_AIA_335_...jpxmid'
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


@add_shared_docstring(getJPXInputParameters)
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
    >>> from datetime import datetime
    >>> getJPX(startTime=datetime(2014, 1, 1, 0, 0, 0),endTime=datetime(2014, 1, 1, 0, 45, 0),sourceId=14,jpip=True)
    'jpip://helioviewer.org:8090/movies/SDO_AIA_335_F2014-01-01T00.00.00Z_T2014-01-01T00.45.00ZL.jpx'
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


@add_shared_docstring(getStatusInputParameters)
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
    {'AIA': {...}, 'COSMO': {...}, 'EIT': {...}, 'HMI': {...}, 'LASCO': {...}, 'MDI': {...}, 'SECCHI': {...}, 'SWAP': {...}, 'SXT': {...}, 'XRT': {...}}
    """
    params = getStatusInputParameters()
    return execute_api_call(input_parameters=params)


@add_shared_docstring(getClosestImageInputParameters)
def getClosestImage(
    date: datetime,
    sourceId: int,
    callback: Optional[str] = None,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Find the image data that is closest to the requested date/time. Return the
    associated metadata from the helioviewer database and the XML header of the
    JPEG2000 image file.

    Parameters
    ----------
    {Insert}
    Examples
    --------
    >>> from datetime import datetime
    >>> from hvpy import getClosestImage
    >>> getClosestImage(
    ...     date=datetime(2014,1,1,23,59,59),
    ...     sourceId=14,
    ... )
    {'id': '32271665', 'date': '2014-01-02 00:00:03', 'name': 'AIA 335', 'scale': 0.5899606831770233, 'width': 4096, 'height': 4096, 'refPixelX': 2048.5, 'refPixelY': 2048.5, 'sunCenterOffsetParams': [], 'layeringOrder': 1}
    """
    params = getClosestImageInputParameters(date=date, sourceId=sourceId, callback=callback)
    return execute_api_call(input_parameters=params)



@add_shared_docstring(getDataSourcesInputParameters)
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
    {'SDO': {'HMI': {'continuum': {'sourceId': 18, 'nickname': 'HMI Int', 'layeringOrder': 1, 'start': '2010-12-06 06:53:41', 'end': '2022-07-11 23:59:54', 'uiLabels': [{'label': 'Observatory', 'name': 'SDO'}, {'label': 'Instrument', 'name': 'HMI'}, {'label': 'Measurement', 'name': 'continuum'}]}, ...}
    """
    params = getDataSourcesInputParameters(
        verbose=verbose,
        enable=enable,
        callback=callback,
    )
    return execute_api_call(input_parameters=params)
