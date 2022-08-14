from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class downloadMovieInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``downloadMovie`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique movie identifier, returned as a response by the ``queueMovie`` endpoint request.
    format
        Movie format.
    hq
        Download high quality movie file.
        Defaults to `False`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/movies.html#id9>`__
    {Shared}
    """

    id: str
    format: str
    hq: Optional[bool] = False

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.RAW
