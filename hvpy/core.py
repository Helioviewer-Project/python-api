import requests

from hvpy.io import HvpyParameters, OutputType


def parse_response(response: requests.Response, output_parameters: OutputType):
    """
    This function parses the response from the API call based on the output
    type.
    """

    if output_parameters == OutputType.Raw:
        return response.content
    elif output_parameters == OutputType.String:
        return response.content.decode("utf-8")
    elif output_parameters == OutputType.Json:
        return response.json()


def execute_api_call(input_parameters: HvpyParameters):
    """
    This function executes the API call and returns a parsed response.
    """

    response = requests.get(input_parameters.url, params=input_parameters.dict())
    response.raise_for_status()
    return parse_response(response, input_parameters.get_output_type())
