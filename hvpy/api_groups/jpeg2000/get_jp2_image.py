from typing import Union
from datetime import datetime

from pydantic import Field, validator

from hvpy.datasource import DataSource
from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import _data_source_to_int, convert_date_to_isoformat


class getJP2ImageInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getJP2Image`` API.

    .. {Shared}
    Attributes
    ----------
    date
        Desired datetime of the JP2 image.
    sourceId
        Unique image datasource identifier.
    jpip
        Returns a JPIP URI instead of the binary data of the image if set to True.
        Default is `False`, optional.
    json
        Returns the JSON if set to `True`.
        Default is `False`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2image>`__

    .. {Shared}
    """

    date: datetime
    sourceId: Union[int, DataSource]
    jpip: bool = False
    Json: bool = Field(False, alias="json")
    _date_validator = validator("date", allow_reuse=True)(convert_date_to_isoformat)
    _source_id_validator = validator("sourceId", allow_reuse=True)(_data_source_to_int)

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
