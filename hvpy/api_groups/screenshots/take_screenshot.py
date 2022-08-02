from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class takeScreenshotInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``takeScreenshot`` API.

    Attributes
    ----------
    {Shared}
    date
        Desired datetime of the image.
    imageScale
        Image scale in arcseconds per pixel.
    layers
        Image datasource layer(s) to include in the screenshot.
    events
        List feature/event types and FRMs to use to annotate the movie.
        Use the empty string to indicate that no feature/event annotations should be shown.
        Default is `None`, optional.
    eventLabels
        Annotate each event marker with a text label.
        Default is `False`, optional.
    scale
        Overlay an image scale indicator.
        Default is `False`, optional.
    scaleType
        The Image scale indicator.
        Default is `None`, optional.
    scaleX
        Horizontal offset of the image scale indicator in arcseconds with respect to the center of the Sun.
        Default is `None`, optional.
    scaleY
        Vertical offset of the image scale indicator in arcseconds with respect to the center of the Sun.
        Default is `None`, optional.
    width
        Width of the field of view in pixels.
        Used in conjunction width ``x0``,``y0``, and ``height``.
        Default is `None`, optional.
    height
        Height of the field of view in pixels.
        Used in conjunction width ``x0``,``y0``, and ``width``.
        Default is `None`, optional.
    x0
        The horizontal offset of the center of the field of view from the center of the Sun.
        Used in conjunction with ``y0``, ``width``, and ``height``.
        Default is `None`, optional.
    y0
        The vertical offset of the center of the field of view from the center of the Sun.
        Used in conjunction with ``x0``, ``width``, and ``height``.
        Default is `None`, optional.
    x1
        The horizontal offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``y1``, ``x2``, and ``y2``.
        Default is `None`, optional.
    y1
        The vertical offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``x2``, and ``y2``.
        Default is `None`, optional.
    x2
        The horizontal offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``y1``, and ``y2``.
        Default is `None`, optional.
    y2
        The vertical offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``y1``, and ``x2``.
        Default is `None`, optional.
    display
        Set to true to directly output binary PNG image data.
        Default is `False` (which outputs a JSON object), optional.
    watermark
        Overlay a watermark consisting of a Helioviewer logo, the datasource abbreviation(s) and timestamp(s) displayed in the screenshot.
        Default is `False`, optional.
        Optional.
    callback
        Wrap the response object in a function call of your choosing.
        Default is `None` (no wrapping), optional.

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
