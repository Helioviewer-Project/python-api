from typing import Optional

from hvpy.io import HvpyParameters, OutputType


class getDataSourcesInputParameters(HvpyParameters):
    """
    Handles the input parameters of the getDataSources API.

    Attributes
    ----------
    {Shared}
    verbose : bool, optional
        Output the hierarchical list of available datasources in a format that is compatible with the JHelioviewer desktop client
    enable : str, optional
        Comma-separated list of observatories to enable.
    callback : str, optional
        Wrap the response object in a function call of your choosing.

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
