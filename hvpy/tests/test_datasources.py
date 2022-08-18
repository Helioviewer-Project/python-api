from hvpy.datasources import DataSources


def test_datasources():
    assert DataSources.EIT_171.name == "EIT_171"
    assert DataSources.EIT_171.value == 0

    assert DataSources.EIT_195.name == "EIT_195"
    assert DataSources.EIT_195.value == 1

    assert DataSources.EIT_284.name == "EIT_284"
    assert DataSources.EIT_284.value == 2

    assert DataSources.EIT_304.name == "EIT_304"
    assert DataSources.EIT_304.value == 3

    assert DataSources.LASCO_C2.name == "LASCO_C2"
    assert DataSources.LASCO_C2.value == 4

    assert DataSources.LASCO_C3.name == "LASCO_C3"
    assert DataSources.LASCO_C3.value == 5

    assert DataSources.MDI_MAG.name == "MDI_MAG"
    assert DataSources.MDI_MAG.value == 6
