import pytest

from hvpy import getTile
from hvpy.api_groups.screenshots.get_tile import getTileInputParameters


def test_getTile():
    response = getTile(
        id=36275490,
        x=-1,
        y=-1,
        imageScale=2,
    )
    assert isinstance(response, bytes)


def test_error_handling():
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'id'"):
        getTile(
            x=-1,
            y=-1,
            imageScale=2,
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'x'"):
        getTile(
            id=36275490,
            y=-1,
            imageScale=2,
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'y'"):
        getTile(
            id=36275490,
            x=-1,
            imageScale=2,
        )
    with pytest.raises(TypeError, match="missing 1 required positional argument: 'imageScale'"):
        getTile(
            id=36275490,
            x=-1,
            y=-1,
        )


def test_url_property():
    params = getTileInputParameters(
        id=36275490,
        x=-1,
        y=-1,
        imageScale=2,
    )
    assert params.url == "https://api.beta.helioviewer.org/v2/getTile/"
