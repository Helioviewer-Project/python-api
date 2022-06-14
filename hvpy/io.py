from enum import Enum
from pydantic import BaseModel


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
    # temporary strings, untill meeting with the team
    Raw = "binary"
    String = "string"
    Json = "json"
