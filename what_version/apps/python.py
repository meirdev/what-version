import re
import subprocess

import requests
from bs4 import BeautifulSoup

from ..logger import logger
from ._base import App


class Python(App):
    @classmethod
    def name(cls) -> str:
        return "python"

    def current_version(self) -> str:
        cmd = ["python3", "--version"]

        logger.debug(f"Running command: {' '.join(cmd)}")

        process = subprocess.run(cmd, text=True, stdout=subprocess.PIPE)

        logger.debug(f"Command status code: {process.returncode}")

        logger.debug(f"Command output: {process.stdout}")

        version = re.search(r"Python (?P<version>\S+)", process.stdout)

        logger.debug(f"Match result: {version}")

        return version.group("version")

    def latest_version(self) -> str:
        url = "https://www.python.org/downloads/"

        logger.debug(f"Requesting URL: {url}")

        tags = requests.get(url)

        logger.debug(f"Request status code: {tags.status_code}")

        logger.debug(f"Request text: {tags.text}")

        soup = BeautifulSoup(tags.text, "html.parser")

        a = soup.find("div", class_="download-for-current-os").find(
            "a", class_="button"
        )

        logger.debug(f"Found <a> tag: {a}")

        version = re.search(r"Download Python (?P<version>\S+)", a.text)

        logger.debug(f"Match result: {version}")

        return version.group("version")
