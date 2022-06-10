from datetime import datetime
from api_groups.jpeg2000.getJp2Image import getJP2ImageInputParameters as InputParameters
import requests


# create `io.py` and add an enum class OutputType to handle the different output_parameters
def parse_response(response: requests.Response, output_parameters: str):

    # Once you have the OutputType class, let's change these to OutputType.Raw, OutputType.String, and OutputType.Json
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


# This should be in unit tests
if __name__ == "__main__":

    URL = "https://api.helioviewer.org/v2/getJP2Image/"
    DATE = datetime(2022, 1, 1, 23, 59, 59)

    input_parameters = InputParameters(date=DATE, sourceId=1)
    input_parameters.date = input_parameters.date.isoformat() + "Z"

    r = execute_api_call(url=URL, input_parameters=input_parameters.dict(), output_parameters="url")
