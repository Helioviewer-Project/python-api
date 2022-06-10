# Add an enum class to handle different output_parameters
# OutputType.Raw, OutputType.String, and OutputType.Json
# Add a function to handle output_parameters
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
        return OutputType.Raw
