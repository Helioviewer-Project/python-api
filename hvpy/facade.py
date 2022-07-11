from typing import Any, Dict, List, Union, Optional
from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import *
from hvpy.utils import add_shared_docstring

__all__ = ["getJP2Image", "getJP2Header", "getJPXClosestToMidPoint", "getJPX", "getStatus"]


@add_shared_docstring(getJP2ImageInputParameters)
def getJP2Image(
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Retrieve a JP2000 image from the helioviewer.org API.

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

    {Insert}
    Examples
    --------
    >>> from hvpy import getJP2Header
    >>> getJP2Header(id=9838343,callback="xml_header")
    'xml_header('<?xml version="1.0" encoding="utf-8"?><meta><fits><SIMPLE>1</SIMPLE><BITPIX>16</BITPIX>...'
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

    {Insert}
    Examples
    --------
    >>> from hvpy import getJPXClosestToMidPoint
    >>> from datetime import datetime
    >>> getJPXClosestToMidPoint(startTimes=[datetime(2014, 1, 1, 0, 0, 0), datetime(2014, 1, 1, 2, 3, 3)], endTimes=[datetime(2014, 1, 1, 0, 45, 0), datetime(2014, 1, 1, 2, 33, 3)], sourceId=14, linked=False, verbose=False, jpip=True)
    'jpip://helioviewer.org:8090/movies/SDO_AIA_335_F2014-01-01T00.00.00Z_T2014-01-01T02.33.03ZCMP.jpxmid'
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

    {Insert}
    Examples
    --------
    >>> from hvpy import getJPX
    >>> from datetime import datetime
    >>> getJPX(startTime=datetime(2014, 1, 1, 0, 0, 0),endTime=datetime(2014, 1, 1, 0, 45, 0),sourceId=14,linked=True,verbose=False,jpip=True,cadence=None)
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

    {Insert}
    Examples
    --------
    >>> from hvpy import getStatus
    >>> getStatus()
    {'AIA': {'time': '2022-07-11T08:01:35Z', 'level': 1, 'secondsBehind': 1801, 'measurement': 'AIA 94'}, 'COSMO': {'time': '2022-07-05T00:46:07Z', 'level': 4, 'secondsBehind': 546329, 'measurement': 'COSMO KCor'}, 'EIT': {'time': '2013-08-07T13:06:09Z', 'level': 5, 'secondsBehind': 281647527, 'measurement': 'EIT 284'}, 'HMI': {'time': '2022-07-11T06:00:39Z', 'level': 1, 'secondsBehind': 9057, 'measurement': 'HMI Mag'}, 'LASCO': {'time': '2022-07-11T06:30:07Z', 'level': 1, 'secondsBehind': 7289, 'measurement': 'LASCO C3'}, 'MDI': {'time': '2011-01-11T22:39:00Z', 'level': 5, 'secondsBehind': 362742756, 'measurement': 'MDI Int'}, 'SECCHI': {'time': '2022-07-08T23:57:30Z', 'level': 1, 'secondsBehind': 203646, 'measurement': 'EUVI-A 195'}, 'SWAP': {'time': '2022-07-11T06:17:19Z', 'level': 1, 'secondsBehind': 8057, 'measurement': 'SWAP 174'}, 'SXT': {'time': '2001-12-14T21:06:33Z', 'level': 5, 'secondsBehind': 649164303, 'measurement': 'SXT AlMgMn'}, 'XRT': {'time': '2022-06-24T23:56:45Z', 'level': 5, 'secondsBehind': 1413291, 'measurement': 'XRT Any/Any'}}
    """
    params = getStatusInputParameters()
    return execute_api_call(input_parameters=params)
