from hvpy import getNewsFeed
from hvpy.api_groups.communications.get_news_feed import getNewsFeedInputParameters


def test_string_response():
    response = getNewsFeed()
    assert isinstance(response, str)

    response = getNewsFeed(callback="test")
    assert isinstance(response, str)
    assert response.startswith("test(")


def test_url_response():
    params = getNewsFeedInputParameters()
    assert params.url == "https://api.beta.helioviewer.org/v2/getNewsFeed/"
