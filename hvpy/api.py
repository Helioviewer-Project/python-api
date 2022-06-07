__all__ = ["fake_api_call"]

from datetime import datetime
from typing import Optional
import requests
from pydantic import BaseModel, Field


class InputParameters(BaseModel):
    date: datetime
    sourceId: int
    jpip: Optional[bool] = Field(False, alias="jpip")
    Json: Optional[bool] = Field(False, alias="json")


def parse_response(response: requests.Response, output_parameters: str):
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
    if output_parameters == "binary":
        return response.content
    elif output_parameters == "url":
        return response.url
    elif output_parameters == "json":
        return response.json()


def execute_api_call(url: str, input_parameters: dict, output_parameters: str):
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
    params.date = params.date.isoformat() + "Z"

    response = requests.get(url, params=params)
    # check if we have a valid response
    if response.status_code != 200:
        raise Exception(f"API call failed with status code {response.status_code}")

    return parse_response(response, output_parameters)


if __name__ == "__main__":

    URL = "https://api.helioviewer.org/v2/getJP2Image/"
    DATE = datetime(2022, 1, 1, 23, 59, 59)

    input_parameters = {"date": DATE, "sourceId": 14}

    r = execute_api_call(url=URL, input_parameters=input_parameters, output_parameters="binary")

    # Save the image to a file
    with open("test.jp2", "wb") as f:
        f.write(r)
