from typing import Protocol


class UrlValidator(Protocol):
    def is_url_valid(self, url: str) -> bool: ...
