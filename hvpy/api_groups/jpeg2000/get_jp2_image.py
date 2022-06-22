from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType


class getJP2ImageInputParameters(HvpyParameters):
    """
    A class for the input parameters of the getJP2Image API call.
    ref: https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2image


    ...

    Attributes
    ----------
    date : datetime
        Desired date/time of the JP2 image.
    sourceId : int
        Unique image datasource identifier.
    jpip : bool
        Optionally return a JPIP URI instead of the binary data of the image itself.
    Json : bool
        Optionally return a JSON object.


    Methods
    -------
    convert_date_to_isoformat
        Converts the date from a datetime object to a string in the ISO format.

    get_output_type
        Returns the output type of the API call.
    """

    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False

    @validator("date")
    def convert_date_to_isoformat(cls, v):
        return v.isoformat() + "Z"

    def get_output_type(self):
        if self.Json == True and self.jpip == True:
            return OutputType.Json
        elif self.Json == False and self.jpip == True:
            return OutputType.String
        else:
            return OutputType.Raw
