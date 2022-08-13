import pytest

from hvpy import downloadScreenshot
from hvpy.api_groups.screenshots.download_screenshot import downloadScreenshotInputParameters


def test_raw_response():
    response = downloadScreenshot(id=3240748)
    assert isinstance(response, bytes)


def test_url_property():
    params = downloadScreenshotInputParameters(id=3240748)
    assert params.url == "https://api.beta.helioviewer.org/v2/downloadScreenshot/"


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        downloadScreenshot()
