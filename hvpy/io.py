from enum import Enum, auto
from typing import Literal

from pydantic.main import BaseModel

__all__ = ["HvpyParameters", "OutputType"]

BASE_URL = "https://api.helioviewer.org/v2/"


class OutputType(Enum):
    Raw = auto()
    String = auto()
    Json = auto()


class HvpyParameters(BaseModel):
    """
    Base model for all Helioviewer API parameters.
    """

    def dict(self):
        # pydantic doesn't allow using lowercase 'json' as a field
        d = super().dict()
        if "Json" in d:
            d["json"] = d["Json"]
            del d["Json"]
        return d

    def get_output_type(self) -> Literal[OutputType.Raw, OutputType.String, OutputType.Json]:
        return OutputType.Raw

    @property
    def url(self) -> str:
        return BASE_URL + self.__class__.__name__[:-15] + "/"
