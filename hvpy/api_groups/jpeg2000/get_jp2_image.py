from typing import Optional
from datetime import datetime

from pydantic import validator

from hvpy.io import HvpyParameters, OutputType


class getJP2ImageInputParameters(HvpyParameters):
    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False

    # Use validator to convert date to isoformat with suffix 'Z'
    @validator("date")
    def convert_date_to_isoformat(cls, v):
        return v.isoformat() + "Z"

    def get_output_type(self):
        if self.Json == True and self.jpip == True:
            return OutputType.Json
        elif self.Json == False and self.jpip == True:
            return OutputType.String
        else:
            return OutputType.Raw
