import sys

from what_version.__main__ import main


def test_what_version(capsys):
    try:
        sys.argv = ["", "dummy"]
        main()
    except SystemExit as e:
        assert e.code == 0

    captured = capsys.readouterr()

    assert "Current version: 1.0.0" in captured.out


def test_what_version_with_latest(capsys):
    try:
        sys.argv = ["", "dummy", "--latest"]
        main()
    except SystemExit as e:
        assert e.code == 0

    captured = capsys.readouterr()

    assert "Current version: 1.0.0" in captured.out
    assert "Latest version: 2.0.0" in captured.out


def test_what_version_not_found(capsys):
    try:
        sys.argv = ["", "HaHaHa"]
        main()
    except SystemExit as e:
        assert e.code == 1

    captured = capsys.readouterr()

    assert "App 'HaHaHa' not found" in captured.err
