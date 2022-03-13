import os
from ..domain.boundaries.output.token_generator_config import TokenGeneratorConfig


class EnvTokenGeneratorConfig(TokenGeneratorConfig):
    def get_token_length(self) -> int:
        return int(os.environ.get('TOKEN_LENGTH', 10))
