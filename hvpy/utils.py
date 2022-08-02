from typing import Any, Callable
from datetime import datetime

__all__ = ["add_shared_docstring", "convert_date_to_isoformat", "convert_date_to_unix"]


def add_shared_docstring(input_class) -> Callable[[Any], Any]:
    def decorator(func):
        if "{Shared}" in input_class.__doc__:
            split_doc = input_class.__doc__.split("{Shared}")
            func.__doc__ = func.__doc__.replace("{Insert}", split_doc[1])
            input_class.__doc__ = input_class.__doc__.replace("{Shared}", "")
        return func

    return decorator


def convert_date_to_isoformat(v: datetime) -> str:
    """
    Converts the date from a datetime object to a string in the ISO format.
    """
    if v:
        return v.isoformat() + "Z"
    return ""


def convert_date_to_unix(v: list) -> str:
    """
    Converts a list of datetimes to Unix timestamps format separated with
    commas.
    """
    return ",".join([str(int(datetime.timestamp(d))) for d in v])
