import requests

from hvpy.io import HvpyParameters, OutputType


def parse_response(response: requests.Response, output_parameters: OutputType):
    """
    _summary_

    Returns
    -------
    _type_
        _description_
    """

    if output_parameters == OutputType.Raw:
        return response.content
    elif output_parameters == OutputType.String:
        return response.content.decode("utf-8")
    elif output_parameters == OutputType.Json:
        return response.json()


def execute_api_call(input_parameters: HvpyParameters):
    """
    _summary_

    Returns
    -------
    _type_
        _description_
    """
    response = requests.get(input_parameters.url(), params=input_parameters.dict())

    if response.raise_for_status() == None:
        return parse_response(response, input_parameters.get_output_type())
