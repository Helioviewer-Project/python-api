from typing import Any

from hvpy import DataSource, getDataSources


def find_nested_keys(obj: dict, key: Any, out: list):
    """
    Recursively walks through a nested dictionary and extracts values
    associated with the given key.

    obj - dictionary with nested dictionaries
    key - Key to find within the nest
    out - values found are appended to this list
    """
    if key in obj:
        out.append(obj[key])
    else:
        for k, v in obj.items():
            if isinstance(v, dict):
                find_nested_keys(v, key, out)
            else:
                continue


def test_datasources():
    source_ids = []
    enum_values = [s_id.value for s_id in DataSource]
    response = getDataSources()
    find_nested_keys(response, "sourceId", source_ids)
    for source_id in source_ids:
        assert source_id in enum_values
