from datetime import datetime

from pydantic import Field, validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class getJP2ImageInputParameters(HvpyParameters):
    """
    Handles the input parameters of the getJP2Image API.

    {Shared}
    Attributes
    ----------
    date : datetime.datetime
        Desired date/time of the JP2 image.
    sourceId : int
        Unique image datasource identifier.
    jpip : bool, optional
        Returns a JPIP URI instead of the binary data of the image if set to `True`, defaults to `False`.
    json : bool, optional
        Returns the JSON if set to `True`, defaults to `False`.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2image>`__
    {Shared}
    """

    date: datetime
    sourceId: int
    jpip: bool = False
    Json: bool = Field(False, alias="json")
    _date_validator = validator("date", allow_reuse=True)(convert_date_to_isoformat)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.Json and self.jpip:
            return OutputType.JSON
        elif not self.Json and self.jpip:
            return OutputType.STRING
        else:
            return OutputType.RAW
