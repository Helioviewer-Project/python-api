from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class queueMovieInputParameters(HvpyParameters):
    """
    Handles the input parameters of the ``queueMovie`` API.

    Attributes
    ----------
    {Shared}
    startTime
        Datetime of the first frame of the movie.
    endTime
        Datetime of the final frame of the movie.
    layers
        Image datasource layers to include in the movie.
    events
        List of feature/event types and FRMs to use to annotate the movie.
    eventsLabels
        Boolean to indicate if the event labels should be included in the movie.
    imageScale
        Image scale in arcseconds per pixel.
    format
        Movie format ("mp4", "webm", "flv").
        Default value is "mp4", optional.
    frameRate
        Movie frames per second.
        Default value is 15 frames per second, optional.
    maxFrames
        Maximum number of frames in the movie, can be capped by the server.
        Default value is `None`, optional.
    scale
        Overlay an image scale indicator.
        Default value is `None`, optional.
    scaleType
        Set the image scale indicator.
        Default value is `None`, optional.
    scaleX
        Horizontal offset of the image scale indicator in arcseconds with respect to the center of the Sun.
        Default value is `None`, optional.
    scaleY
        Vertical offset of the image scale indicator in arcseconds with respect to the center of the Sun.
        Default value is `None`, optional.
    movieLength
        Movie length in seconds.
        Default value is `None`, optional.
    watermark
        Overlay a Helioviewer.org watermark image.
        Default value is `True`, optional.
    width
        Width of the field of view in pixels. (Used in conjunction with ``x0``, ``y0``, and ``height``).
        Default value is `None`, optional.
    height
        Height of the field of view in pixels. (Used in conjunction with ``x0``, ``y0``, and ``width``).
        Default value is `None`, optional.
    x0
        The horizontal offset of the center of the field of view from the center of the Sun.
        Used in conjunction with ``y0``, ``width``, and ``height``.
        Default value is `None`, optional.
    y0
        The vertical offset of the center of the field of view from the center of the Sun. Used in conjunction with ``x0``, width, and height.
        Default value is `None`, optional.
    x1
        The horizontal offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``y1``, ``x2``, and ``y2``.
        Default value is `None`, optional.
    y1
        The vertical offset of the top-left corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``x2``, and ``y2``.
        Default value is `None`, optional.
    x2
        The horizontal offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``y1``, and ``y2``.
        Default value is `None`, optional.
    y2
        The vertical offset of the bottom-right corner of the field of view with respect to the center of the Sun (in arcseconds).
        Used in conjunction with ``x1``, ``y1``, and ``x2``.
        Default value is `None`, optional.
    callback
        Wrap the response object in a function call of your choosing.
        Default value is `None`, optional.
    size
        Scale video to preset size.
        Default value is 0, optional.
    movieIcons
        Display other user generated movies on the video.
        Default value is `None`, optional.
    followViewport
        Rotate field of view of movie with Sun.
        Default value is `None`, optional.
    reqObservationDate
        Viewport datetime.
        Used when 'followViewport' enabled to shift viewport area to correct coordinates
        Default value is `None`, optional.

    References
    ----------
    * `<https://api.helioviewer.org/docs/v2/api/api_groups/movies.html#queuemovie>`__
    {Shared}
    """

    startTime: datetime
    endTime: datetime
    layers: str
    events: str
    eventsLabels: bool
    imageScale: float
    format: Optional[str] = "mp4"
    frameRate: Optional[str] = "15"
    maxFrames: Optional[str] = None
    scale: Optional[bool] = None
    scaleType: Optional[str] = None
    scaleX: Optional[float] = None
    scaleY: Optional[float] = None
    movieLength: Optional[float] = None
    watermark: Optional[bool] = True
    width: Optional[str] = None
    height: Optional[str] = None
    x0: Optional[str] = None
    y0: Optional[str] = None
    x1: Optional[str] = None
    y1: Optional[str] = None
    x2: Optional[str] = None
    y2: Optional[str] = None
    callback: Optional[str] = None
    size: Optional[int] = 0
    movieIcons: Optional[int] = None
    followViewport: Optional[int] = None
    reqObservationDate: Optional[datetime] = None
    _date_validator = validator("startTime", "endTime", "reqObservationDate", allow_reuse=True)(
        convert_date_to_isoformat
    )

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.JSON
