"""
Rate limit exceptions.
"""


class RateLimitException(Exception):
    """
    Rate limit exception class.
    """

    def __init__(self, message: str, period_remaining: float) -> None:
        """
        Custom exception raise when the number of function invocations exceeds
        that imposed by a rate limit. Additionally the exception is aware of
        the remaining time period after which the rate limit is reset.

        :param string message: Custom exception message.
        :param float period_remaining: The time remaining until the rate limit is reset.
        """
        super().__init__(message)
        self.period_remaining = period_remaining
