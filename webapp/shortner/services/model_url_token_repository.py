from domain.boundaries.output.urltoken_repository import UrlTokenRepository
from domain.entities.url_token import UrlToken as DomainUrlToken

from webapp.shortner.models import UrlToken


class ModelUrlTokenRepository(UrlTokenRepository):
    def get_by_token(self, token: str) -> UrlToken:
        try:
            return UrlToken.to_domain(UrlToken.objects.get(token=token))
        except UrlToken.DoesNotExist:
            return None

    def insert(self, data: DomainUrlToken):
        UrlToken.objects.create(url=data.url, token=data.token)
