from typing import List
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_unix


class getJPXClosestToMidPointInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getJPXClosestToMidPoint`` API.

    Attributes
    ----------
    {Shared}
    startTimes
        A list of datetimes for the beginning of the JPX movie data.
    endTimes
        A list of datetimes for the end of the JPX movie data.
    sourceId
        Unique image datasource identifier.
    linked
        Generate a linked JPX file containing image pointers instead of data for each individual frame in the series.
        Default is `True`, optional.
    verbose
        If set, the JSON response will include timestamps for each frame in the resulting movie and any warning messages associated with the request, in addition to the JPX movie file URI.
        Default is `False`, optional.
    jpip
        Return a JPIP URI string instead of the binary data of the movie itself, or instead of an HTTP URI in the JSON response (if ``verbose`` is set to `True`).
        Default is `False`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjpxclosesttomidpoint>`__
    {Shared}
    """

    startTimes: List[datetime]
    endTimes: List[datetime]
    sourceId: int
    linked: bool = True
    verbose: bool = False
    jpip: bool = False
    _date_validator = validator("startTimes", "endTimes", allow_reuse=True)(convert_date_to_unix)

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
