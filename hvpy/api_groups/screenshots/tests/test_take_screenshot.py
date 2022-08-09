from datetime import datetime

import pytest

from hvpy import takeScreenshot
from hvpy.api_groups.screenshots.take_screenshot import takeScreenshotInputParameters


def test_json_response():
    response = takeScreenshot(
        date=datetime.today(),
        imageScale=2.4204409,
        layers="[10,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert "id" in response


def test_raw_response():
    response = takeScreenshot(
        display=True,
        date=datetime.today(),
        imageScale=2.4204409,
        layers="[10,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert isinstance(response, bytes)


def test_url_property():
    params = takeScreenshotInputParameters(
        date=datetime.today(),
        imageScale=2.4204409,
        layers="[3,1,100]",
        width=1920,
        height=1200,
        x0=0,
        y0=0,
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/takeScreenshot/"


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'date'"):
        takeScreenshot(
            imageScale=2.4204409,
            layers="[3,1,100]",
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'imageScale'"):
        takeScreenshot(
            date=datetime(2014, 1, 1, 23, 59, 59),
            layers="[3,1,100]",
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'layers'"):
        takeScreenshot(
            date=datetime(2014, 1, 1, 23, 59, 59),
            imageScale=2.4204409,
        )
