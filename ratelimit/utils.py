"""
Rate limit utility functions.
"""
import time
from typing import Callable


def now() -> Callable[[], float]:
    """
    Use monotonic time if available, otherwise fall back to the system clock.

    :return: Time function.
    """
    if hasattr(time, "monotonic"):
        return time.monotonic

    return time.time
