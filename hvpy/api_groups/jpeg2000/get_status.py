from hvpy.io import HvpyParameters, OutputType


class getStatusInputParameters(HvpyParameters):
    """
    Returns information about how far behind the latest available JPEG2000
    images.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/jpeg2000.html#getstatus>`__
    """

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.JSON
