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
        Movie Format ("mp4", "webm", or "flv").
    hq
        Download a higher-quality movie file (valid for "mp4" movies only, ignored otherwise).
        Defaults to `False`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/movies.html#id9>`__
    {Shared}
    """

    id: str
    format: str
    hq: bool = False

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.RAW
