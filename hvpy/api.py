__all__ = ["fake_api_call"]

from datetime import datetime
from typing import Optional
import requests
from pydantic import BaseModel


Json = "json"


class InputParameters(BaseModel):
    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False


def binary(response: requests.Response):
    return response.content


def url(response: requests.Response):
    return response.url


def json(response: requests.Response):
    return response.json()


def parse_response(response, output_parameters: str):
    """
    _summary_

    Parameters
    ----------
    response: ?
        _description_
    output_parameters: ?
        _description_

    Returns
    -------
    _type_
        _description_
    """
    switch = {
        "binary": binary(response),
        "json": json(response),
        "url": url(response),
    }
    return switch.get(output_parameters, response)()


def execute_api_call(url: str, input_parameters: dict, output_parameters):
    """
    _summary_

    Parameters
    ----------
    url: str
        _description_
    input_parameters: dict
        _description_
    output_parameters: ?
        _description_

    Returns
    -------
    _type_
        _description_
    """
    params = InputParameters(**input_parameters)
    response = requests.get(url, params=params)
    print(response.url)
    # check if we have a valid response
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}")

    # return parse_response(response, output_parameters)


if __name__ == "__main__":

    URL = "https://api.helioviewer.org/v2/getJP2Image/"
    DATE = datetime(2003, 10, 6, 0, 0, 0, 0).isoformat() + "Z"
    SOURCE_ID = "14"
    data = {"date": DATE, "sourceId": SOURCE_ID}

    r = requests.get(url, params=data)
    print(r.url)
    # input_parameters = {"date": datetime(2014, 1, 1, 0, 0, 0).isoformat() + "Z", "sourceId": 14}

    # r = execute_api_call(url=URL, input_parameters=input_parameters, output_parameters="url")
    # print(r)
