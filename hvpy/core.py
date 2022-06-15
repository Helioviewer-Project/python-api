import requests
from hvpy.io import OutputType


def parse_response(response: requests.Response, output_parameters: OutputType):

    if output_parameters == OutputType.Raw:
        return response.content
    elif output_parameters == OutputType.String:
        return str(response.content)
    elif output_parameters == OutputType.Json:
        return response.json()


def execute_api_call(url: str, input_parameters: HvpyParameters, output_parameters: OutputType):

    response = requests.get(url, params=input_parameters())
    # check if we have a valid response
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}")

    return parse_response(response, input_parameters.get_output_type())
