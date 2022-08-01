from typing import Optional

from hvpy.io import HvpyParameters, OutputType


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

    id: int
    callback: Optional[str] = None

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.STRING
