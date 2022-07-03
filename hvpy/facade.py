from datetime import datetime

from hvpy.core import execute_api_call
from hvpy.parameters import getJP2ImageInputParameters

__all__ = ["getJP2Image"]


def _copy_docstring(input_class):
    def decorator(func):
        input_class_docstr = input_class.__doc__.split("\n")[1:]
        func_docstr = func.__doc__.split("\n")[1:]
        input_class_docstr[0] = func_docstr[0]
        input_class_docstr = "\n".join(input_class_docstr)
        func.__doc__ = input_class_docstr
        return func

    return decorator


@_copy_docstring(getJP2ImageInputParameters)
def getJP2Image(
    date: datetime,
    sourceId: int,
    jpip: bool = False,
    json: bool = False,
):
    """
    Retrieve a JP2000 image from the helioviewer.org API.
    """
    params = getJP2ImageInputParameters(**locals())
    return execute_api_call(input_parameters=params)
