from typing import Any, Union, Callable, Optional
from datetime import datetime

from hvpy.datasource import DataSource
from hvpy.event import EventType

__all__ = [
    "convert_date_to_isoformat",
    "convert_date_to_unix",
    "create_layers",
    "create_events",
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
    if isinstance(val, str) and val in [x.value for x in EventType]:
        return EventType(val)
    elif isinstance(val, EventType):
        return val
    else:
        raise ValueError(f"{val} is not a valid EventType")


def _create_events_string(event_type: EventType, recognition_method: Optional[str] = "all") -> str:
    """
    Generates a string of the form "[event_type,recognition_method,1]" for a
    event.
    """
    if recognition_method is None:
        recognition_method = "all"
    return f"[{event_type.value},{recognition_method},1]"


def create_events(event: list) -> str:
    """
    Creates a string of events separated by commas.

    Parameters
    ----------
    event
        A list of tuples of the form (``event_type``, ``recognition_methods``).

    Examples
    --------
    >>> from hvpy import create_events, EventType
    >>> create_events([("AR"), ("ER", "SPoCA;NOAA_SWPC_Observer")])
    '[AR,all,1],[ER,SPoCA;NOAA_SWPC_Observer,1]'
    """
    buff = ""
    array = [e for e in event]
    for e in array:
        if isinstance(e, EventType) or isinstance(e, str):
            buff += _create_events_string(_to_event_type(e)) + ","
        elif isinstance(e, tuple) and len(e) == 2:
            buff += _create_events_string(_to_event_type(e[0]), e[1]) + ","
        else:
            raise ValueError(f"{e} is not a valid EventType or tuple")
    return buff[:-1]
