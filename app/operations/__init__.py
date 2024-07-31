def add(a: float, b: float) -> float:
    print(f"DEBUG: Inside add function with {a} and {b}")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a + b

def multiply(a: float, b: float) -> float:
    print(f"DEBUG: Inside multiply function with {a} and {b}")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a * b

def subtract(a: float, b: float) -> float:
    print(f"DEBUG: Inside subtract function with {a} and {b}")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    return a - b

def divide(a: float, b: float) -> float:
    print(f"DEBUG: Inside divide function with {a} and {b}")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be int or float")
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b