from enum import Enum, auto
from typing import Any, Dict

from pydantic import BaseModel

from hvpy.config import get_api_url

__all__ = ["HvpyParameters", "OutputType"]


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

    def model_dump(self) -> Dict[str, Any]:
        # pydantic doesn't allow using lowercase 'json' as a field
        import warnings

        with warnings.catch_warnings():
            # Our datetime fields are strings(???) and pydantic complains about that
            warnings.simplefilter("ignore")
            dump = super().model_dump()
        if "Json" in dump:
            dump["json"] = dump["Json"]
            del dump["Json"]
        return dump

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
        return get_api_url() + self.__class__.__name__[:-15] + "/"
