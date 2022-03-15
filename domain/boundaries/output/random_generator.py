from typing import Protocol


class RandomGenerator(Protocol):
    def get_next_int(self, stop: int) -> int: ...
