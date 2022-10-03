from what_version.apps.dummy import Dummy


def test_name():
    assert Dummy.name() == "dummy"


def test_current_version():
    dummy = Dummy()

    assert dummy.current_version() == "1.0.0"


def test_latest_version():
    dummy = Dummy()

    assert dummy.latest_version() == "2.0.0"
