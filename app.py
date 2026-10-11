"""Financial Calculator Module.

Provides basic arithmetic functions for financial calculations.
"""

from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Return the sum of x and y."""
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Return the difference of x and y (x - y)."""
    return x - y


if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Result:", add(100, 50))
