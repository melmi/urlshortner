import validators

from domain.boundaries.output.url_validator import UrlValidator


class ValidatorsUrlValidatorService(UrlValidator):
    def is_url_valid(self, url: str) -> bool:
        return validators.url(url)
