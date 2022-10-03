from typing import Type

from .apps import App


class AppNotFoundError(Exception):
    pass


def what_version(app: str) -> App:
    apps: dict[str, Type[App]] = {i.name(): i for i in App.__subclasses__()}

    if app not in apps:
        raise AppNotFoundError(f"App '{app}' not found")

    app_cls = apps[app]
    app_obj = app_cls()

    return app_obj
