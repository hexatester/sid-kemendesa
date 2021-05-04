from typing import Tuple


class SidError(Exception):
    def __init__(self, message: str):
        super().__init__()
        message = message.strip()
        message = message.capitalize()
        self.message = message

    def __str__(self):
        return self.message

    def __reduce__(self) -> Tuple[type, Tuple[str]]:
        return self.__class__, (self.message,)
