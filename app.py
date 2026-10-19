"""Financial Calculator Application logic.

Provides basic arithmetic operations for financial analytics.
"""

import os
from typing import Union

Number = Union[int, float]

# Environment flag configuration
ENVIRONMENT = os.getenv("APP_ENV", "development")


def get_environment() -> str:
    """Return the current environment flag setting."""
    return os.getenv("APP_ENV", "development")


def is_build_enabled() -> bool:
    """Check if build is enabled based on environment flag."""
    flag = os.getenv("BUILD_FLAG", "true").lower()
    return flag in ("true", "1", "yes")


def add(x: Number, y: Number) -> Number:
    """Add two numbers and return the result."""
    return x + y


def subtract(x: Number, y: Number) -> Number:
    """Subtract y from x and return the result."""
    return x - y


if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Environment:", get_environment())
    print("Build Flag Active:", is_build_enabled())
    print("Result:", add(100, 50))
