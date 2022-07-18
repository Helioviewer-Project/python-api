import os
from enum import Enum, auto
from typing import Any, Dict

from pydantic import BaseModel

__all__ = ["HvpyParameters", "OutputType", "set_api_url"]


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
        base_url = get_api_url()
        return base_url + self.__class__.__name__[:-15] + "/"


def get_api_url() -> str:
    """
    Returns the base URL for all API calls.
    """
    if "PRIVATE_URL" in os.environ:
        base_url = os.environ["PRIVATE_URL"]
        del os.environ["PRIVATE_URL"]
        return base_url
    return os.environ.get("HVPY_BASE_URL", default="https://api.helioviewer.org/v2/")


def set_api_url(private_url: str) -> None:
    """
    Sets the base URL for all API calls.
    """
    os.environ["PRIVATE_URL"] = private_url
