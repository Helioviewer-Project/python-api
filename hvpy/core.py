from typing import Any, Dict, Union

import requests

from hvpy.io import HvpyParameters, OutputType

__all__ = ["execute_api_call", "parse_response"]


def parse_response(response: requests.Response, output_type: OutputType) -> Union[bytes, str, Dict[str, Any]]:
    """
    Parses the response from the API call based on the output type.

    Parameters
    ----------
    response
        The response from the API call.
    output_type
        The output type.

    Returns
    -------
    Union[bytes, str, Dict[str, Any]]
        The parsed response.
    """
    if output_type == OutputType.RAW:
        return response.content
    elif output_type == OutputType.STRING:
        return response.content.decode("utf-8")
    elif output_type == OutputType.JSON:
        return response.json()
    else:
        raise ValueError(f"Unknown output type: {output_type}")


def execute_api_call(input_parameters: HvpyParameters) -> Union[bytes, str, Dict[str, Any]]:
    """
    Executes the API call and returns a parsed response.

    Parameters
    ----------
    input_parameters
        The input parameters.

    Returns
    -------
    Union[bytes, str, Dict[str, Any]]
        Parsed response from the API.
    """
    response = requests.get(input_parameters.url, params=input_parameters.dict())
    response.raise_for_status()
    return parse_response(response, input_parameters.get_output_type())
