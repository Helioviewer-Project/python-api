from hvpy import DataSources, getDataSources


def test_datasources():
    source_id_list = list()
    res = getDataSources()

    for name, observ in res.items():
        # TRACE only has measurements and is thus nested once
        if name == "TRACE":
            for instr, params in observ.items():
                source_id_list.append(params["sourceId"])
        else:
            for inst, detect in observ.items():
                for wavelength, params in detect.items():
                    if "sourceId" in params:
                        source_id_list.append(params["sourceId"])
                    else:
                        for wave, adict in params.items():
                            source_id_list.append(adict["sourceId"])

    data_sources_list = [source_id.value for source_id in DataSources]

    for source_id in source_id_list:
        assert source_id in data_sources_list
