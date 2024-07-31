"""
This module demonstrates basic arithmetic operations and result printing.

It imports utility functions for printing and arithmetic operations,
then performs addition and multiplication before printing the results.
"""

from app.calculator import Calculator
from app.utils import print_it


def get_user_choice():
    options = """
    Please choose an operation:
    1. Addition
    2. Multiplication
    3. Subtraction
    4. Division
    q. Quit
    """
    while True:
        print_it(options)
        choice = input("Enter your choice (1/2/3/4/q): ").lower()
        print(f"DEBUG: User choice: {choice}")
        if choice in ['1', '2', '3', '4', 'q']:
            return choice
        print_it("Invalid choice. Please try again.")


def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            print(f"DEBUG: User input number: {value}")
            return value
        except ValueError:
            print_it("Invalid input. Please enter valid numbers.")


def get_numbers():
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    return num1, num2


def perform_calculation(operation, a, b):
    try:
        if operation == '1':
            return Calculator.add(a, b), 'Addition'
        elif operation == '2':
            return Calculator.multiply(a, b), 'Multiplication'
        elif operation == '3':
            return Calculator.subtract(a, b), 'Subtraction'
        elif operation == '4':
            if b == 0:
                raise ValueError("Cannot divide by zero")
            return Calculator.divide(a, b), 'Division'
        else:
            raise ValueError("Invalid operation")
    except Exception as e:
        print_it(f"DEBUG: Error in calculation: {str(e)}")
        return None, None


def main():
    """
    Execute the main program logic.

    This function runs a loop that repeatedly prompts the user to choose
    an operation, input numbers, perform the calculation, and print the results
    using the print_it function.
    """
    while True:
        choice = get_user_choice()
        if choice == 'q':
            print_it("Thank you for using the calculator. Goodbye!")
            break
        num1, num2 = get_numbers()
        print_it(f"DEBUG: Performing calculation with choice {choice}, "
                 f"numbers {num1} and {num2}")
        result, operation = perform_calculation(choice, num1, num2)
        if result is not None:
            message = f'{operation} of {num1} and {num2} is equal to {result}'
            print_it(message)
        else:
            print_it("Calculation failed. Please try again.")


if __name__ == '__main__':
    # Execute the main function if this script is run directly
    main()