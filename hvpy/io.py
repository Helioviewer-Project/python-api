import os
from enum import Enum, auto
from typing import Any, Dict, Optional

from pydantic import BaseModel

__all__ = ["HvpyParameters", "OutputType", "set_api"]

base_url = "https://api.helioviewer.org/v2/"


class OutputType(Enum):
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


class BaseUrl(Enum):
    V2 = auto()
    """
    Defines the V2 base URL.
    """
    V3 = auto()
    """
    Defines the V3 base URL.
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

    def get_output_type(self) -> OutputType:
        """
        Works out the return type of the API call.

        This by default is RAW, subclasses should redefine this.

        Returns
        -------
        hvpy.io.OutputType
            Output type based on the model.
        """
        return OutputType.RAW

    @property
    def url(self) -> str:
        """
        Final API endpoint URL.
        """
        return base_url + self.__class__.__name__[:-15] + "/"


def set_api(url: Optional[str] = None) -> None:
    """
    Sets the base URL for the Helioviewer python API.
    """
    global base_url
    if url:
        base_url = url
    elif "URL" in os.environ:
        base_url = str(os.environ.get("URL"))
    else:
        base_url = "https://api.helioviewer.org/v2/"
