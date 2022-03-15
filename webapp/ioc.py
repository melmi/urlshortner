import punq

from domain.boundaries.input.token_broker import TokenBroker
from domain.boundaries.output.random_generator import RandomGenerator
from domain.boundaries.output.token_generator_config import TokenGeneratorConfig
from domain.boundaries.output.url_validator import UrlValidator
from domain.boundaries.output.urltoken_repository import UrlTokenRepository
from domain.services.token_broker_service import TokenBrokerService
from domain.services.token_generation_service import TokenGenerationService
from domain.services.token_generator import TokenGenerator
from adapters.default_random_generator_service import DefaultRandomGeneratorService
from adapters.validators_url_validator_service import ValidatorsUrlValidatorService
from webapp.shortner.services.env_token_generator_config import EnvTokenGeneratorConfig
from webapp.shortner.services.model_url_token_repository import ModelUrlTokenRepository

container = punq.Container()

container.register(TokenBroker, TokenBrokerService)
container.register(RandomGenerator, DefaultRandomGeneratorService)
container.register(UrlValidator, ValidatorsUrlValidatorService)
container.register(UrlTokenRepository, ModelUrlTokenRepository)
container.register(TokenGenerator, TokenGenerationService)
container.register(TokenGeneratorConfig, EnvTokenGeneratorConfig)


# based on https://github.com/django/django/blob/main/django/views/generic/base.py
def get_ioc_view(cls, **initkwargs):
    def view(request, *args, **kwargs):
        self = container.instantiate(cls, **initkwargs)
        self.setup(request, *args, **kwargs)
        return self.dispatch(request, *args, **kwargs)

    view.view_class = cls
    view.view_initkwargs = initkwargs
    view.__doc__ = cls.__doc__
    view.__module__ = cls.__module__
    view.__annotations__ = cls.dispatch.__annotations__
    view.__dict__.update(cls.dispatch.__dict__)

    return view
