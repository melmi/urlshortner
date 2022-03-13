from shortner.domain.boundaries.input.token_broker import TokenBroker
from shortner.domain.boundaries.output.url_validator import UrlValidator
from shortner.domain.boundaries.output.urltoken_repository import UrlTokenRepository
from shortner.domain.services.token_generator import TokenGenerator
from shortner.domain.entities.exceptions import BusinessException, NotFoundException
from shortner.domain.entities.url_token import UrlToken


class TokenBrokerService(TokenBroker):
    def __init__(self,
                 repository: UrlTokenRepository,
                 url_validator: UrlValidator,
                 token_generator: TokenGenerator):
        self.repository = repository
        self.url_validator = url_validator
        self.token_generator = token_generator

    def get_token(self, url: str) -> str:
        if not self.url_validator.is_url_valid(url):
            raise BusinessException('url is not valid')

        token = self.token_generator.get_token()

        self.repository.insert(UrlToken(url, token))

        return token

    def get_url(self, token: str) -> str:
        url_token = self.repository.get_by_token(token)
        if url_token is None:
            raise NotFoundException('token not found')

        return url_token.url
