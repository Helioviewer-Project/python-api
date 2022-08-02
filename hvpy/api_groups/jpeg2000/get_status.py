from hvpy.io import HvpyParameters, OutputType


class getStatusInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getStatus`` API.

    {Shared}
    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getstatus>`__
    {Shared}
    """

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.JSON
