"""Financial Calculator Application logic."""


def add(x: int | float, y: int | float) -> int | float:
    """Add two numbers and return the result."""
    return x + y


def subtract(x: int | float, y: int | float) -> int | float:
    """Subtract y from x and return the result."""
    return x - y


if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Result:", add(100, 50))
    # Final check
