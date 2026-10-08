def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

def calculate_simple_interest(principal, rate, time):
    """
    Calculate simple interest.
    principal: initial amount
    rate: annual interest rate in percentage (e.g. 5 for 5%)
    time: time in years
    """
    return (principal * rate * time) / 100.0

def calculate_compound_interest(principal, rate, time, n=1):
    """
    Calculate compound interest.
    principal: initial amount
    rate: annual interest rate in percentage (e.g. 5 for 5%)
    time: time in years
    n: number of times interest is compounded per year
    """
    if n <= 0:
        raise ValueError("Compounding frequency n must be greater than zero.")
    amount = principal * ((1 + (rate / 100.0) / n) ** (n * time))
    return amount - principal

if __name__ == "__main__":
    print("--- Financial Calculator App ---")
    print("Add (100, 50):", add(100, 50))
    print("Simple Interest (1000, 5%, 2 yrs):", calculate_simple_interest(1000, 5, 2))
    print("Compound Interest (1000, 5%, 2 yrs):", calculate_compound_interest(1000, 5, 2))
