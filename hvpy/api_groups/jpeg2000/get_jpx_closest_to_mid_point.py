from typing import List
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType


class getJPXClosestToMidPointInputParameters(HvpyParameters):
    """
    Handles the input parameters of the getJPXClosestToMidPoint API.

    Attributes
    ----------
    startTimes : datetime
        Comma separated timestamps for the beginning of the JPX movie data.
    endTimes : datetime
        Comma separated timestamps for the end of the JPX movie data.
    sourceId : int
        Unique image datasource identifier.
    linked : bool, optional
        Generate a linked JPX file containing image pointers instead of data for each individual frame in the series.
    verbose : bool, optional
        If set to true, the JSON response will include timestamps for each frame in the resulting movie and any warning messages associated with the request, in addition to the JPX movie file URI.
    jpip : bool, optional
        Optionally return a JPIP URI string instead of the binary data of the movie itself, or instead of an HTTP URI in the JSON response (if verbose is set to true).

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjpxclosesttomidpoint>`__
    """

    startTimes: List[datetime]
    endTimes: List[datetime]
    sourceId: int
    linked: bool = False
    verbose: bool = False
    jpip: bool = False

    @validator("startTimes", "endTimes")
    def convert_date_to_unix(cls, v) -> str:
        """
        Converts date from datetime object to Unix timestamps format separated
        with commas.
        """
        return ",".join([str(int(datetime.timestamp(d))) for d in v])

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if not self.jpip and not self.verbose:
            return OutputType.RAW
        elif self.jpip and not self.verbose:
            return OutputType.STRING
        else:
            return OutputType.JSON
