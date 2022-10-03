import logging
from pathlib import Path

BASE_DIR = Path.cwd()

logger = logging.getLogger("what-version")

formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")

file_handler = logging.FileHandler(BASE_DIR / "what-version.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)
