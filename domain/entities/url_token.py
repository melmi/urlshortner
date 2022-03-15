from dataclasses import dataclass


@dataclass
class UrlToken:
    url: str
    token: str
