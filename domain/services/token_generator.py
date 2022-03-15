from typing import Protocol


class TokenGenerator(Protocol):
    def get_token(self) -> str: ...
