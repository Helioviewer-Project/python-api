from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType
from hvpy.utils import convert_date_to_isoformat


class queueMovieInputParameters(HvpyParameters):
    """
    Handles the input parameters of the queueMovie API.

    Attributes
    ----------
    {Shared}
    startTime : datetime
        Date and time of the first frame of the movie.
    endTime : datetime
        Date and time of the final frame of the movie.
    layers : str
        Image datasource layers to include in the movie.
    events : str
        List of feature/event types and FRMs to use to annotate the movie.
    eventsLabels : bool
        Annotate each event marker with a text label.
    imageScale : float
        Image scale in arcseconds per pixel.
    format : str, optional
        Movie format (mp4, webm, flv). Default value is mp4.
    frameRate : str, optional
        Movie frames per second. 15 frames per second by default.
    maxFrames : str, optional
        Maximum number of frames in the movie. May be capped by the server.
    scale : bool, optional
        Optionally overlay an image scale indicator.
    scaleType : str, optional
        Image scale indicator
    scaleX : float, optional
        Horizontal offset of the image scale indicator in arcseconds with respect to the center of the Sun.
    scaleY : float, optional
        Vertical offset of the image scale indicator in arcseconds with respect to the center of the Sun.
    movieLength : float, optional
        movie length in seconds.
    watermark : bool, optional
        Optionally overlay a Helioviewer.org watermark image. Enabled by default
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
    callback : str, optional
        Wrap the response object in a function call of your choosing.
    size : int, optional
        Scale video to preset size. Default value is 0.
    movieIcons : int, optional
        Display other user generated movies on the video.
    followViewport : int, optional
        Rotate field of view of movie with Sun.
    reqObservationDate : datetime, optional
        Viewport time. Used when 'followViewport' enabled to shift viewport area to correct coordinates


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
    size: Optional[int] = None
    movieIcons: Optional[int] = None
    followViewport: Optional[int] = None
    reqObservationDate: Optional[datetime] = None
    _date_validator = validator("startTime", "endTime", "reqObservationalDate", allow_reuse=True, check_fields=False)(
        convert_date_to_isoformat
    )

    def get_output_type(self) -> OutputType:
        """
        Returns the output type of the API call.
        """
        return OutputType.JSON
