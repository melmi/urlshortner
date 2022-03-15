from typing import Protocol

from domain.entities.url_token import UrlToken


class UrlTokenRepository(Protocol):
    def get_by_token(self, token: str) -> UrlToken: ...
    def insert(self, data: UrlToken): ...
