from abc import ABC, abstractmethod


class App(ABC):
    @classmethod
    @abstractmethod
    def name(cls) -> str:  # pragma: no cover
        ...

    @abstractmethod
    def current_version(self) -> str:  # pragma: no cover
        ...

    @abstractmethod
    def latest_version(self) -> str:  # pragma: no cover
        ...
