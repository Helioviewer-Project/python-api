from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class takeScreenshotInputParameters(HvpyParameters):
    """
    Handles the input parameters of the takeScreenshot API.

    Attributes
    ----------
    {Shared}
    date : datetime.datetime
        Desired date/time of the image.
    imageScale : float
        Image scale in arcseconds per pixel.
    layers : str
        Image datasource layer(s) to include in the screenshot.
    eventLabels : bool
        Optionally annotate each event marker with a text label.
    events : str, optional
        List feature/event types and FRMs to use to annoate the movie. Use the empty string to indicate that no feature/event annotations should be shown.
    scale : bool, optional
        Optionally overlay an image scale indicator.
    scaleType : str, optional
        Image scale indicator.
    scaleX : int, optional
        Horizontal offset of the image scale indicator in arcseconds with respect to the center of the Sun.
    scaleY : int, optional
        Vertical offset of the image scale indicator in arcseconds with respect to the center of the Sun.
    width : str, optional
        Width of the field of view in pixels. (Used in conjunction width x0,`y0`, and height).
    height : str, optional
        Height of the field of view in pixels. (Used in conjunction width x0,`y0`, and width).
    x0 : str, optional
        The horizontal offset of the center of the field of view from the center of the Sun. Used in conjunction with y0, width, and height.
    y0 : str, optional
        The vertical offset of the center of the field of view from the center of the Sun. Used in conjunction with x0, width, and height.
    x1 : str, optional
        The horizontal offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds). Used in conjunction with y1, x2, and y2.
    y1 : str, optional
        The vertical offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds). Used in conjunction with x1, x2, and y2.
    x2 : str, optional
        The horizontal offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds). Used in conjunction with x1, y1, and y2.
    y2 : str, optional
        The vertical offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds). Used in conjunction with x1, y1, and x2.
    display : bool, optional
        Set to true to directly output binary PNG image data. Default is `False` (which outputs a JSON object).
    watermark : bool, optional
        Optionally overlay a watermark consisting of a Helioviewer logo and the datasource abbreviation(s) and timestamp(s) displayed in the screenshot.
    callback : str, optional
        Wrap the response object in a function call of your choosing.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/screenshots.html#takescreenshot>`__
    {Shared}
    """

    date: datetime
    imageScale: float
    layers: str
    events: Optional[str] = None
    eventLabels: Optional[bool] = False
    scale: Optional[bool] = False
    scaleType: Optional[str] = None
    scaleX: Optional[int] = None
    scaleY: Optional[int] = None
    width: Optional[str] = None
    height: Optional[str] = None
    x0: Optional[str] = None
    y0: Optional[str] = None
    x1: Optional[str] = None
    y1: Optional[str] = None
    x2: Optional[str] = None
    y2: Optional[str] = None
    display: Optional[bool] = False
    watermark: Optional[bool] = False
    callback: Optional[str] = None
    _date_vaidator = validator("date", allow_reuse=True)(convert_date_to_isoformat)

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.RAW if self.display else OutputType.JSON
