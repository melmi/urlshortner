from typing import Protocol


class TokenGeneratorConfig(Protocol):
    def get_token_length(self) -> int: ...
