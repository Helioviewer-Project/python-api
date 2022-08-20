from hvpy import DataSources, getDataSources

sids = list()


def find_key(obj, key):
    if key in obj:
        sids.append(obj[key])
    else:
        for k, v in obj.items():
            if isinstance(v, dict):
                find_key(v, key)
            else:
                continue


def test_datasources():
    enum_value_list = [s_id.value for s_id in DataSources]
    res = getDataSources()

    find_key(res, "sourceId")

    for sid in sids:
        assert sid in enum_value_list
