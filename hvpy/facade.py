from hvpy.core import execute_api_call
from hvpy.parameters import getJP2ImageInputParameters

__all__ = ["getJP2Image"]


def getJP2Image(**kwargs):
    """
    Get a JP2 image from the helioviewer.org API.
    """
    params = getJP2ImageInputParameters(**kwargs)
    return execute_api_call(input_parameters=params)
