from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class getMovieStatusInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getMovieStatus`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique movie identifier, returned as a response by the ``queueMovie`` endpoint request.
    format
        Movie format.
    verbose
        Include extra metadata in the response.
        Defaults to `False`, optional.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.
    token
        API token.
        Defaults to `None`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/movies.html#id8>`__
    {Shared}
    """

    id: str
    format: str
    verbose: Optional[bool] = False
    callback: Optional[str] = None
    token: Optional[str] = None

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback is not None:
            return OutputType.STRING
        return OutputType.JSON
