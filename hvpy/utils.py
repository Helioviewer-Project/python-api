from typing import Any, List, Union, Callable
from pathlib import Path
from datetime import datetime

from hvpy.datasource import DataSource
from hvpy.event import EventType

__all__ = [
    "convert_date_to_isoformat",
    "convert_date_to_unix",
    "create_layers",
    "create_events",
    "save_file",
]


def _add_shared_docstring(input_class) -> Callable[[Any], Any]:
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
    if v is not None:
        return v.isoformat() + "Z"


def convert_date_to_unix(v: list) -> str:
    """
    Converts a list of datetimes to Unix timestamps format separated with
    commas.
    """
    return ",".join([str(int(datetime.timestamp(d))) for d in v])


def _to_datasource(val: Union[int, DataSource]) -> DataSource:
    """
    Validates the input and converts it to a DataSource enum.
    """
    if isinstance(val, int) and val in [x.value for x in DataSource]:
        return DataSource(val)
    elif isinstance(val, DataSource):
        return val
    else:
        raise ValueError(f"{val} is not a valid DataSource")


def _create_layer_string(source_id: DataSource, opacity: int) -> str:
    """
    Generates a string of the form "[source_id,1,opacity]" for a layer.
    """
    if not 0 <= opacity <= 100:
        raise ValueError(f"opacity ({opacity}) must be between 0 and 100")
    else:
        return f"[{source_id.value},1,{opacity}]"


def create_layers(layer: list) -> str:
    """
    Creates a string of layers separated by commas.

    Parameters
    ----------
    layer
        A list of tuples of the form (``source_id``, ``opacity``).

    Examples
    --------
    >>> from hvpy import create_layers
    >>> create_layers([(3, 50), (10, 50)])
    '[3,1,50],[10,1,50]'
    """
    return ",".join([_create_layer_string(_to_datasource(s), o) for s, o in layer])


def _to_event_type(val: Union[str, EventType]) -> EventType:
    """
    Validates the input and converts it to a EventType enum.
    """
    # This is an undocumented attribute of Enums
    if isinstance(val, str) and val in EventType._value2member_map_:
        return EventType(val)
    elif isinstance(val, EventType):
        return val
    else:
        raise ValueError(f"{val} is not a valid EventType")


def _create_events_string(event_type: EventType, recognition_method: str = "all") -> str:
    """
    Generates a string of the form "[event_type,recognition_method,1]" for a
    event.
    """
    return f"[{event_type.value},{recognition_method},1]"


def create_events(events: List[Union[EventType, str, tuple]]) -> str:
    """
    Creates a string of events separated by commas.

    Parameters
    ----------
    events
        Either a `list` of `tuple` of the form (``event_type``, ``recognition_methods``),
        or a `list` of `str` or `~hvpy.EventType`, e.g., ``["AR", EventType.CORONAL_CAVITY]``
        If ``recognition_methods`` is missing, it will use "ALL".

    Examples
    --------
    >>> from hvpy import create_events
    >>> create_events(["AR", ("ER", "SPoCA;NOAA_SWPC_Observer")])
    '[AR,all,1],[ER,SPoCA;NOAA_SWPC_Observer,1]'
    """
    constructed_events = ""
    for event in events:
        if isinstance(event, (str, EventType)):
            constructed_events += _create_events_string(_to_event_type(event)) + ","
        elif isinstance(event, tuple) and len(event) == 2:
            constructed_events += _create_events_string(_to_event_type(event[0]), event[1]) + ","
        else:
            raise ValueError(f"{event} is not a EventType or str or two-length tuple")
    # Strips the final comma
    return constructed_events[:-1]


def save_file(data: bytearray, filename: Union[Path, str], overwrite: bool = False) -> None:
    """
    Saves a file to the specified path.

    Parameters
    ----------
    data
        The data to save.
    filename
        The path to save the file to.
    overwrite
        Whether to overwrite the file if it already exists.
        Default is `False`.
    """
    if isinstance(filename, str):
        filename = Path(filename)
    if filename.exists() and not overwrite:
        raise ValueError(f"{filename} already exists. Use overwrite=True to overwrite.")
    filename.write_bytes(data)
