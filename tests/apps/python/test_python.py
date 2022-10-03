from pathlib import Path

import pytest_subprocess
import requests_mock as req_mock

from what_version.apps.python import Python

BASE_DIR = Path(__file__).resolve().parent


def test_name():
    assert Python.name() == "python"


def test_current_version(fp):
    python = Python()

    with open(BASE_DIR / "./fixtures/stdout.txt") as file:
        stdout = file.read()

    fp.register([fp.any()], stdout=stdout)

    assert python.current_version() == "3.10.4"


def test_latest_version(requests_mock):
    python = Python()

    with open(BASE_DIR / "./fixtures/downloads.html") as file:
        downloads = file.read()

    requests_mock.get(req_mock.ANY, text=downloads)

    assert python.latest_version() == "3.10.7"
