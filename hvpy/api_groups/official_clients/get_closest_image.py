from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class getClosestImageInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getClosestImage`` API.

    Attributes
    ----------
    {Shared}
    date
        Datetime of the image.
    sourceId
        Unique image datasource identifier.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/official_clients.html#getclosestimage>`__
    {Shared}
    """

    date: datetime
    sourceId: int
    callback: Optional[str] = None
    _date_validator = validator("date", allow_reuse=True)(convert_date_to_isoformat)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback is None:
            return OutputType.JSON
        return OutputType.STRING
