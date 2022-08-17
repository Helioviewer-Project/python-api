from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class getDataSourcesInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getDataSources`` API.

    Attributes
    ----------
    {Shared}
    verbose
        Output the hierarchical list of available datasources in a format that is compatible with the JHelioviewer desktop client.
        Default is `False`, optional.
    enable
        Comma-separated list of observatories to enable.
        Default is `None` (all observatories are enabled), optional.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/official_clients.html#getdatasources>`__
    {Shared}
    """

    verbose: Optional[bool] = False
    enable: Optional[str] = None
    callback: Optional[str] = None

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        if self.callback:
            return OutputType.STRING
        else:
            return OutputType.JSON
