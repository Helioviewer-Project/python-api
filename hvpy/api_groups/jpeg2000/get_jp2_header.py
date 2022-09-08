from typing import Union, Optional

from pydantic import validator

from hvpy.datasource import DataSource
from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import _data_source_to_int


class getJP2HeaderInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getJP2Header`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique JP2 image identifier.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2header>`__
    {Shared}
    """

    id: Union[int, DataSource]
    callback: Optional[str] = None
    _id_validator = validator("id", allow_reuse=True)(_data_source_to_int)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.STRING
