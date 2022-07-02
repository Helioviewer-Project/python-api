from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import getJP2ImageInputParameters

__all__ = ["getJP2Image"]


def copy_docstring(input_class):
    def decorator(func):
        func.__doc__ = func.__doc__ + input_class.__doc__
        return func

    return decorator


@copy_docstring(getJP2ImageInputParameters)
def getJP2Image(
    *,
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
):
    """
    Get a JP2 image from the helioviewer.org API.
    """
    params = locals()
    params = getJP2ImageInputParameters(**params)
    return execute_api_call(input_parameters=params)
