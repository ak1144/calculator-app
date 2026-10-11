"""Financial Calculator Application.

Provides basic arithmetic operations for financial analytics.
"""

from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Add two numbers and return the result."""
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Subtract y from x and return the result."""
    return x - y


if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Result:", add(100, 50))
