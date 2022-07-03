from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import getJP2ImageInputParameters

__all__ = ["getJP2Image"]


def _copy_docstring(input_class):
    def decorator(func):
        docstring = input_class.__doc__.split("\n")[1:]
        docstring2 = func.__doc__.split("\n")[1:]
        docstring[0] = docstring2[0]
        docstring = "\n".join(docstring)
        func.__doc__ = docstring
        return func

    return decorator


@_copy_docstring(getJP2ImageInputParameters)
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
