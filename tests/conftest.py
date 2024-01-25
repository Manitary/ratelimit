from typing import Iterator

import pytest


class Clock:
    def __init__(self) -> None:
        self.reset()

    def __call__(self) -> float:
        return self.now

    def reset(self) -> None:
        self.now: float = 0

    def increment(self, num: float = 1) -> None:
        self.now += num


@pytest.fixture(autouse=True, scope="class")
def clock() -> Iterator[Clock]:
    yield Clock()
