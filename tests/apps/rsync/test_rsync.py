from pathlib import Path

import pytest_subprocess
import requests_mock as req_mock

from what_version.apps.rsync import Rsync

BASE_DIR = Path(__file__).resolve().parent


def test_name():
    assert Rsync.name() == "rsync"


def test_current_version(fp):
    rsync = Rsync()

    with open(BASE_DIR / "./fixtures/stdout.txt") as file:
        stdout = file.read()

    fp.register([fp.any()], stdout=stdout)

    assert rsync.current_version() == "2.6.9"


def test_latest_version(requests_mock):
    rsync = Rsync()

    with open(BASE_DIR / "./fixtures/tags.html") as file:
        tags = file.read()

    requests_mock.get(req_mock.ANY, text=tags)

    assert rsync.latest_version() == "3.2.7pre1"
