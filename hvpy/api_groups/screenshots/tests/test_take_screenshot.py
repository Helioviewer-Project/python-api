import pytest

from hvpy import takeScreenshot
from hvpy.api_groups.screenshots.take_screenshot import takeScreenshotInputParameters


def test_json_response(date):
    response = takeScreenshot(
        date=date,
        imageScale=2.4204409,
        layers="[10,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert "id" in response


def test_raw_response(date):
    response = takeScreenshot(
        display=True,
        date=date,
        imageScale=2.4204409,
        layers="[10,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert isinstance(response, bytes)


def test_url_property(date):
    params = takeScreenshotInputParameters(
        date=date,
        imageScale=2.4204409,
        layers="[3,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/takeScreenshot/"


def test_error_handling(date):
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        takeScreenshot(
            imageScale=2.4204409,
            layers="[3,1,100]",
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'imageScale'"):
        takeScreenshot(
            date=date,
            layers="[3,1,100]",
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'layers'"):
        takeScreenshot(
            date=date,
            imageScale=2.4204409,
        )
