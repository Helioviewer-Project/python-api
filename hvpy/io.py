from enum import IntEnum, auto
from typing import Any, Dict

from pydantic.main import BaseModel

__all__ = ["HvpyParameters", "OutputType"]

BASE_URL = "https://api.helioviewer.org/v2/"


class OutputType(IntEnum):
    RAW = auto()
    """
    Defines the RAW output type.
    """
    STRING = auto()
    """
    Defines the STRING output type.
    """
    JSON = auto()
    """
    Defines the JSON output type.
    """


class HvpyParameters(BaseModel):
    """
    Base model for all Helioviewer API parameters.
    """

    def dict(self) -> Dict[str, Any]:  # type: ignore
        # pydantic doesn't allow using lowercase 'json' as a field
        d = super().dict()
        if "Json" in d:
            d["json"] = d["Json"]
            del d["Json"]
        return d

    def get_output_type(self) -> int:
        """
        Works out the return type of the API call.

        This by default is RAW (1), subclasses should redefine this.

        Returns
        -------
        int
            Output type based on the model.
        """
        return OutputType.RAW

    @property
    def url(self) -> str:
        """
        Final API endpoint URL.
        """
        return BASE_URL + self.__class__.__name__[:-15] + "/"
