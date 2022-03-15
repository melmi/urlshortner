from domain.services.token_generator import TokenGenerator
from domain.boundaries.output.random_generator import RandomGenerator
from domain.boundaries.output.token_generator_config import TokenGeneratorConfig


class TokenGenerationService(TokenGenerator):
    def __init__(self,
                 token_generation_config: TokenGeneratorConfig,
                 random_generator: RandomGenerator):
        self.token_generation_config = token_generation_config
        self.random_generator = random_generator

    CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    def get_token(self) -> str:
        chars = [self.CHARS[self.random_generator.get_next_int(len(self.CHARS))]
                 for i in range(self.token_generation_config.get_token_length())]
        result = ''.join(chars)
        return result
