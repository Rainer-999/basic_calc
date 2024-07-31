from app.operations import add, multiply, divide, subtract


class Calculator:

    @staticmethod
    def add(a: float, b: float) -> float:
        print(f"DEBUG: Adding {a} + {b}")
        return add(a, b)

    @staticmethod
    def multiply(a: float, b: float) -> float:
        print(f"DEBUG: Multiplying {a} * {b}")
        return multiply(a, b)

    @staticmethod
    def subtract(a: float, b: float) -> float:
        print(f"DEBUG: Subtracting {a} - {b}")
        return subtract(a, b)

    @staticmethod
    def divide(a: float, b: float) -> float:
        print(f"DEBUG: Dividing {a} / {b}")
        return divide(a, b)