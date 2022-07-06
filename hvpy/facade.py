from typing import Any, Dict, Union, Callable
from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import *

__all__ = ["getJP2Image"]


def _update_docstring(input_class) -> Callable[[Any], Any]:
    def decorator(func):
        docstring = input_class.__doc__.split("{{Shared}}", 1)[1].split("{{End Shared}}", 1)[0]
        func.__doc__ = func.__doc__.replace("{{Insert Shared}}", docstring)
        return func

    return decorator


@_update_docstring(getJP2ImageInputParameters)
def getJP2Image(
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
) -> Union[bytes, str, Dict[str, Any]]:
    """
    Retrieve a JP2000 image from the helioviewer.org API.

    {{Insert Shared}}

    Examples
    --------
        >>> from hvpy import getJP2Image
        >>> getJP2Image(date=datetime(2019,1,1), sourceId=1, jpip=True)
        'jpip://helioviewer.org:8090/EIT/2013/08/07/195/2013_08_07__01_13_50_146__SOHO_EIT_EIT_195.jp2'
    """
    params = getJP2ImageInputParameters(date=date, sourceId=sourceId, jpip=jpip, json=json)
    return execute_api_call(input_parameters=params)
