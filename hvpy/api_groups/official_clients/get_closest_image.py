from typing import Union, Optional
from datetime import datetime

from pydantic import validator

from hvpy.datasource import DataSource
from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import _data_source_to_int, convert_date_to_isoformat


class getClosestImageInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getClosestImage`` API.

    .. {Shared}
    Attributes
    ----------
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

    .. {Shared}
    """

    date: datetime
    sourceId: Union[int, DataSource]
    callback: Optional[str] = None
    _date_validator = validator("date", allow_reuse=True)(convert_date_to_isoformat)
    _source_id_validator = validator("sourceId", allow_reuse=True)(_data_source_to_int)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback is None:
            return OutputType.JSON
        return OutputType.STRING
