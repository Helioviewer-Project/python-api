from hvpy import EventType

helioviewer_event_types = {
    "Active Region": "AR",
    "Coronal Cavity": "CC",
    "Coronal Dimming": "CD",
    "Coronal Hole": "CH",
    "Coronal Jet": "CJ",
    "Coronal Mass Ejection": "CE",
    "Coronal Rain": "CR",
    "Coronal Wave": "CW",
    "Emerging Flux": "EF",
    "Eruption": "ER",
    "Filament": "FI",
    "Filament Activation": "FA",
    "Filament Eruption": "FE",
    "Flare": "FL",
    "Loop": "LP",
    "Oscillation": "OS",
    "Plage": "PG",
    "Sigmod": "SG",
    "Spray Surge": "SP",
    "Sunspot": "SS",
}


def test_event_types():
    assert [x.value for x in EventType] == list(helioviewer_event_types.values())
