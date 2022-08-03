from hvpy.io import HvpyParameters, OutputType


class downloadScreenshotInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``downloadScreenshot`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique screenshot identifier (provided by the response to a ``takeScreenshot`` request).

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/screenshots.html#downloadscreenshot>`__
    {Shared}
    """

    id: int

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.RAW
