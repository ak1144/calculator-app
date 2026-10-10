"""Financial Calculator Application.

Provides basic mathematical and financial calculation utilities.
"""

from typing import Union

Number = Union[int, float]


def add(x: Number, y: Number) -> Number:
    """Add two numbers together.

    Args:
        x: First number.
        y: Second number.

    Returns:
        The sum of x and y.
    """
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Subtract y from x.

    Args:
        x: First number.
        y: Second number.

    Returns:
        The difference of x and y.
    """
    return x - y


if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Result:", add(100, 50))
