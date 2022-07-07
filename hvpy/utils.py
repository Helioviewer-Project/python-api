from datetime import datetime

__all__ = ["convert_date_to_isoformat", "convert_date_to_unix"]


def convert_date_to_isoformat(v: datetime) -> str:
    """
    Converts the date from a datetime object to a string in the ISO format.
    """
    return v.isoformat() + "Z"


def convert_date_to_unix(v: list) -> str:
    """
    Converts a list of datetimes to Unix timestamps format separated with
    commas.
    """
    return ",".join([str(int(datetime.timestamp(d))) for d in v])
