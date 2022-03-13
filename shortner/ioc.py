import punq

from shortner.domain.boundaries.input.token_broker import TokenBroker
from shortner.domain.boundaries.output.random_generator import RandomGenerator
from shortner.domain.boundaries.output.token_generator_config import TokenGeneratorConfig
from shortner.domain.boundaries.output.url_validator import UrlValidator
from shortner.domain.boundaries.output.urltoken_repository import UrlTokenRepository
from shortner.domain.services.token_broker_service import TokenBrokerService
from shortner.domain.services.token_generation_service import TokenGenerationService
from shortner.domain.services.token_generator import TokenGenerator
from shortner.services.default_random_generator_service import DefaultRandomGeneratorService
from shortner.services.env_token_generator_config import EnvTokenGeneratorConfig
from shortner.services.validators_url_validator_service import ValidatorsUrlValidatorService
from shortner.services.model_url_token_repository import ModelUrlTokenRepository

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
