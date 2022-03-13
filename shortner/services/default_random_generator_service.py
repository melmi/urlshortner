import random

from ..domain.boundaries.output.random_generator import RandomGenerator


class DefaultRandomGeneratorService(RandomGenerator):
    def __init__(self):
        self.random = random.Random()

    def get_next_int(self, stop: int) -> int:
        return self.random.randrange(stop)
