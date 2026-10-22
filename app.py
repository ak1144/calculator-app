"""Financial Calculator Application logic.

Provides arithmetic operations for financial analytics.
"""

from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Add two numbers and return the result."""
    return x + y
