import requests


def parse_response(response: requests.Response, output_parameters: str):
    # TODO: replace with OutputType class
    if output_parameters == "binary":
        return response.content
    elif output_parameters == "url":
        return response.url
    elif output_parameters == "json":
        return response.json()


def execute_api_call(url: str, input_parameters: dict, output_parameters: str):
    response = requests.get(url, params=input_parameters())
    # check if we have a valid response
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}")

    return parse_response(response, output_parameters)
