from hvpy import getStatus
from hvpy.api_groups.jpeg2000.get_status import getStatusInputParameters


def test_getStatusInputParameters():
    response = getStatus()
    assert isinstance(response, dict)


def test_url_property():
    params = getStatusInputParameters()
    assert params.url == "https://api.beta.helioviewer.org/v2/getStatus/"
