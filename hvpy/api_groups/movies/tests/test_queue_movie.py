from datetime import datetime

from hvpy import queueMovie


def test_queue():
    response = queueMovie(
        startTime=datetime(2022, 7, 12, 12, 12, 12),
        endTime=datetime(2022, 7, 13, 12, 12, 12),
        layers="[12,7,22],[13,7,22]",
        events="[AR,HMI_HARP;SPoCA,1],[CH,all,1]",
        eventsLabels=False,
        imageScale=21.04,
    )
    print(response)
