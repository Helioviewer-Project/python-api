from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class shortenURLInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``shortenURL`` API.

    Attributes
    ----------
    {Shared}
    queryString
        The URL-encoded query string.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/official_clients.html#shortenurl>`__
    {Shared}
    """

    queryString: str
    callback: Optional[str] = None

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback:
            return OutputType.STRING
        return OutputType.JSON
