from hvpy import shortenURL
from hvpy.api_groups.communications.shorten_url import shortenURLInputParameters


def test_string_response():
    response = shortenURL(
        queryString="https://api.helioviewer.org/v2/queueMovie/?startTime=2010-03-01T12:12:12Z&endTime=2010-03-04T12:12:12Z"
    )
    assert isinstance(response, dict)

    response = shortenURL(
        queryString="https://api.helioviewer.org/v2/queueMovie/?startTime=2010-03-01T12:12:12Z&endTime=2010-03-04T12:12:12Z",
        callback="test",
    )
    assert isinstance(response, str)
    assert response.startswith("test(")


def test_url_response():
    params = shortenURLInputParameters(
        queryString="https://www.google.com",
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/shortenURL/"
