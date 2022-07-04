from pydantic import Field

from hvpy.io import HvpyParameters, OutputType


class getJP2HeaderInputParameters(HvpyParameters):
    """
    Handles the input parameters of the getJP2Header API.

    Attributes
    ----------
    id : int
        Unique JP2 image identifier.
    callback : str, optional
        Wrap the response object in a function call of your choosing.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getjp2header>`__
    """

    id: int
    callback: str = Field(default=None)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback is not None:
            return OutputType.STRING
        else:
            return OutputType.RAW