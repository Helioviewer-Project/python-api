from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class getNewsFeedInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getNewsFeed`` API.

    Attributes
    ----------
    {Shared}
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/web_site.html#getnewsfeed>`__
    {Shared}
    """

    callback: Optional[str] = None

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.STRING
