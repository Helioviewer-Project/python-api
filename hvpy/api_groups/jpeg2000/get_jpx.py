from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class getJPXInputParameters(HvpyParameters):
    """
    Handles the input parameters of the getJPX API.

    {Shared}
    Attributes
    ----------
    startTime : datetime
        Date/Time for the beginning of the JPX movie data.
    endTime : datetime
        Date/Time for the end of the JPX movie data.
    sourceId : int
        Unique image datasource identifier.
    linked : bool, optional
        Generate a linked JPX file containing image pointers instead of data for each individual frame in the series.
    verbose : bool, optional
        If set to true, the JSON response will include timestamps for each frame in the resulting movie and any warning messages associated with the request, in addition to the JPX movie file URI.
    jpip : bool, optional
        Optionally return a JPIP URI string instead of the binary data of the movie itself, or instead of an HTTP URI in the JSON response (if verbose is set to true).
    cadence : int, optional
        The desired amount of time (in seconds) between each frame in the movie.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjpx>`__
    {Shared}
    """

    startTime: datetime
    endTime: datetime
    sourceId: int
    linked: bool = True
    verbose: bool = False
    jpip: bool = False
    cadence: Optional[int] = None
    _date_validator = validator("startTime", "endTime", allow_reuse=True)(convert_date_to_isoformat)

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
