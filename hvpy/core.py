from typing import Any, Union

import requests

from hvpy.io import HvpyParameters, OutputType


def parse_response(response: requests.Response, output_parameters: OutputType) -> Union[bytes, str, Any]:
    """
    Parses the response from the API call based on the output type.

    Parameters
    ----------
    response : `requests.Response`
        The response from the API call.
    output_parameters : `hvpy.io.OutputType`
        The output type.

    Returns
    -------
    `bytes` | `str` | `dict`
        The parsed response.
    """
    if output_parameters == OutputType.Raw:
        return response.content
    elif output_parameters == OutputType.String:
        return response.content.decode("utf-8")
    elif output_parameters == OutputType.Json:
        return response.json()
    else:
        raise ValueError("Unknown output type")


def execute_api_call(input_parameters: HvpyParameters) -> Union[bytes, str, dict]:
    """
    Executes the API call and returns a parsed response.

    Parameters
    ----------
    input_parameters : `HvpyParameters`
        The input parameters.

    Returns
    -------
    `bytes` | `str` | `dict`
        Parsed response from the API.
    """
    response = requests.get(input_parameters.url, params=input_parameters.dict())
    response.raise_for_status()
    return parse_response(response, input_parameters.get_output_type())
