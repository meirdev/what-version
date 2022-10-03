import pytest

from what_version.main import AppNotFoundError, what_version


def test_what_version():
    app = what_version("dummy")

    assert app.current_version() == "1.0.0"
    assert app.latest_version() == "2.0.0"


def test_what_version_not_found():
    with pytest.raises(AppNotFoundError):
        what_version("HaHaHa")
