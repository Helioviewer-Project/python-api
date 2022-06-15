from typing import Optional
from datetime import datetime

from hvpy.io import HvpyParameters


class getJP2ImageInputParameters(HvpyParameters):
    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False
