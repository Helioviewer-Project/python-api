from enum import Enum, auto
from pydantic import BaseModel

BASE_URL = "https://api.helioviewer.org/v2/"


class HvpyParameters(BaseModel):
    def dict(self):
        d = super().dict()
        # Pydantic doesn't allow using lower case 'json' as a field,
        # so override it here.
        if "Json" in d:
            d["json"] = d["Json"]
            del d["Json"]
        return d

    def get_output_type(self):
        # For now just return the raw output
        return OutputType.Raw


class OutputType(Enum):
    Raw = auto()
    String = auto()
    Json = auto()
