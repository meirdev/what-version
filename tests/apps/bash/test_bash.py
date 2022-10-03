from pathlib import Path

import pytest_subprocess
import requests_mock as req_mock

from what_version.apps.bash import Bash

BASE_DIR = Path(__file__).resolve().parent


def test_name():
    assert Bash.name() == "bash"


def test_current_version(fp):
    bash = Bash()

    with open(BASE_DIR / "./fixtures/stdout.txt") as file:
        stdout = file.read()

    fp.register([fp.any()], stdout=stdout)

    assert bash.current_version() == "3.2.57(1)-release"


def test_latest_version(requests_mock):
    bash = Bash()

    with open(BASE_DIR / "./fixtures/bash.html") as file:
        bash_html = file.read()

    requests_mock.get(req_mock.ANY, text=bash_html)

    assert bash.latest_version() == "5.2"
