# Contains I/O parameters for getJp2Image
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class getJP2ImageInputParameters(BaseModel):
    date: datetime
    sourceId: int
    jpip: Optional[bool] = False
    Json: Optional[bool] = False

    def dict(self):
        d = super().dict()
        # Pydantic doesn't allow using lower case 'json' as a field,
        # so override it here.
        if "Json" in d:
            d["json"] = d["Json"]
            del d["Json"]
        return d
