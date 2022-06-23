from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType


class getJP2ImageInputParameters(HvpyParameters):
    """
    Handles the input parameters of the `getJP2Image API.

    <https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2image>`__.

    Attributes
    ----------
    date : datetime
        Desired date/time of the JP2 image.
    sourceId : int
        Unique image datasource identifier.
    jpip : bool, optional
        Returns a JPIP URI instead of the binary data of the image if set to `True`, defaults to `False`.
    Json : bool, optional
        Returns the JSON if set to `True`, defaults to `False`.
    """

    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False

    @validator("date")
    def convert_date_to_isoformat(cls, v):
        """
        Converts the date from a datetime object to a string in the ISO format.
        """
        return v.isoformat() + "Z"

    def get_output_type(self):
        """
        Returns the output type of the API call.
        """
        if self.Json == True and self.jpip == True:
            return OutputType.Json
        elif self.Json == False and self.jpip == True:
            return OutputType.String
        else:
            return OutputType.Raw
