import argparse
import logging
import sys
from typing import NoReturn

from . import __version__
from .logger import logger
from .main import AppNotFoundError, what_version


def get_arg_parser() -> argparse.ArgumentParser:
    arg_parser = argparse.ArgumentParser("What Version")
    arg_parser.add_argument("app", help="The app to check the version of")
    arg_parser.add_argument(
        "--latest", action="store_true", help="Show the latest version available"
    )
    arg_parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )
    arg_parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    return arg_parser


def main() -> NoReturn:
    arg_parser = get_arg_parser()
    args = arg_parser.parse_args()

    if args.debug:
        logger.setLevel(logging.DEBUG)

    try:
        version = what_version(args.app)
    except AppNotFoundError as error:
        print(error, file=sys.stderr)
        exit(1)
    except Exception as error:
        print(error, file=sys.stderr)

        logger.exception(error)

        exit(1)
    else:
        print("Current version:", version.current_version())

        if args.latest:
            print("Latest version:", version.latest_version())

    exit(0)


if __name__ == "__main__":  # pragma: no cover
    main()
