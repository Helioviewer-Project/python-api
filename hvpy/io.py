from enum import Enum, auto

from pydantic import BaseModel

BASE_URL = "https://api.helioviewer.org/v2/"
__all__ = ["HvpyParameters", "OutputType"]


class HvpyParameters(BaseModel):
    def dict(self):
        """
        Pydantic doesn't allow using lowercase 'json' as a field, so we
        override it.
        """
        d = super().dict()
        if "Json" in d:
            d["json"] = d["Json"]
            del d["Json"]
        return d

    def get_output_type(self):
        return OutputType.Raw

    @property
    def url(self):
        return BASE_URL + self.__class__.__name__[:-15] + "/"


class OutputType(Enum):
    Raw = auto()
    String = auto()
    Json = auto()
