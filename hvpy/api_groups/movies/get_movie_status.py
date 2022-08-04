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
        Optionally include extra metadata in the response.
        Defaults to `False`.
    calback
        Optionally wrap the response in a callback function.
    token
        API token.

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
