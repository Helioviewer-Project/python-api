from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class reQueueMovieInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``reQueueMovie`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique movie identifier, returned as a response by the ``queueMovie`` endpoint request.
    force
        Boolean to force the re-queueing of the movie.
        Defaults to `False`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/movies.html#id2>`__
    {Shared}
    """

    id: str
    force: Optional[bool] = False

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.JSON
