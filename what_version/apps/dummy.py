from ._base import App


class Dummy(App):
    @classmethod
    def name(cls) -> str:
        return "dummy"

    def current_version(self) -> str:
        return "1.0.0"

    def latest_version(self) -> str:
        return "2.0.0"
