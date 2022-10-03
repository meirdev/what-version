import re
import subprocess

import requests
from bs4 import BeautifulSoup

from ..logger import logger
from ._base import App


class Bash(App):
    @classmethod
    def name(cls) -> str:
        return "bash"

    def current_version(self) -> str:
        cmd = ["bash", "--version"]

        logger.debug(f"Running command: {' '.join(cmd)}")

        process = subprocess.run(cmd, text=True, stdout=subprocess.PIPE)

        logger.debug(f"Command status code: {process.returncode}")

        logger.debug(f"Command output: {process.stdout}")

        version = re.search(r"version (?P<version>\S+)", process.stdout)

        logger.debug(f"Match result: {version}")

        return version.group("version")

    def latest_version(self) -> str:
        url = "https://ftp.gnu.org/gnu/bash/"

        logger.debug(f"Requesting URL: {url}")

        tags = requests.get(url)

        logger.debug(f"Request status code: {tags.status_code}")

        logger.debug(f"Request text: {tags.text}")

        soup = BeautifulSoup(tags.text, "html.parser")

        a = soup.find_all("a", href=re.compile(r"^bash-\d+\.\d+\.tar\.gz$"))

        logger.debug(f"Found <a> tags: {a}")

        versions = sorted([i.text for i in a], reverse=True)

        version = re.search(r"bash-(?P<version>\d+\.\d+)", versions[0])

        logger.debug(f"Match result: {version}")

        return version.group("version")
