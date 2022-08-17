from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class getTileInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``getTile`` API.

    Attributes
    ----------
    {Shared}
    id
        Unique image identifier.
    x
        Tile x-coordinate.
    y
        Tile y-coordinate.
    imageScale
        Image scale in arcseconds per pixel.
    difference
        Specify image type difference.

        * ``0`` - Display regular image
        * ``1`` - Running difference image
        * ``2`` - Base difference image

        Default is `None`, optional.
    diffCount
        Used to display Running difference image.
        Work with ``diffTime`` parameter and set amount of time to use in time period.
        Default is `None`, optional.
    diffTime
        Select Running difference time period:

        * ``1`` - Minutes
        * ``2`` - Hours
        * ``3`` - Days
        * ``4`` - Weeks
        * ``5`` - Month
        * ``6`` - Years

        Default is `None`, optional.
    baseDiffTime
        Datetime for base difference images.
        Default is `None`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/official_clients.html#gettile>`__
    {Shared}
    """

    id: int
    x: int
    y: int
    imageScale: int
    difference: Optional[int] = None
    diffCount: Optional[int] = None
    diffTime: Optional[int] = None
    baseDiffTime: Optional[datetime] = None

    _date_vaidator = validator("baseDiffTime", allow_reuse=True)(convert_date_to_isoformat)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.RAW
