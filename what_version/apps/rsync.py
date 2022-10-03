import re
import subprocess

import requests
from bs4 import BeautifulSoup

from ..logger import logger
from ._base import App


class Rsync(App):
    @classmethod
    def name(cls) -> str:
        return "rsync"

    def current_version(self) -> str:
        cmd = ["rsync", "--version"]

        logger.debug(f"Running command: {' '.join(cmd)}")

        process = subprocess.run(cmd, text=True, stdout=subprocess.PIPE)

        logger.debug(f"Command status code: {process.returncode}")

        logger.debug(f"Command output: {process.stdout}")

        version = re.search(r"rsync\s+version\s+(?P<version>\S+)", process.stdout)

        logger.debug(f"Match result: {version}")

        return version.group("version")

    def latest_version(self) -> str:
        url = "https://github.com/WayneD/rsync/tags"

        logger.debug(f"Requesting URL: {url}")

        tags = requests.get(url)

        logger.debug(f"Request status code: {tags.status_code}")

        logger.debug(f"Request text: {tags.text}")

        soup = BeautifulSoup(tags.text, "html.parser")

        a = soup.find("a", href=re.compile(r"^/WayneD/rsync/releases/tag/"))

        logger.debug(f"Found <a> tag: {a}")

        version = a.text.strip()

        return version[1:]
