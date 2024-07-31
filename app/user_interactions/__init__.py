from app.calculator import Calculator
from app.utils import print_it


def get_user_choice(input_func=input):
    while True:
        print_it("\nPlease choose an operation:")
        print_it("1. Addition")
        print_it("2. Multiplication")
        print_it("3. Division")
        print_it("4. Subtraction")
        print_it("q. Quit")
        choice = input_func("Enter your choice (1/2/3/4/q): ").lower()
        if choice in ['1', '2', '3', '4', 'q']:
            return choice
        print_it("Invalid choice. Please try again.")


def get_numbers(operation, input_func=input):
    while True:
        try:
            num1 = float(input_func("Enter the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    while True:
        try:
            num2 = float(input_func("Enter the second number: "))
            if operation == '3' and num2 == 0:
                print("Division by zero is not allowed. Enter a non-zero number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    return num1, num2


def main_repl_user_interaction(input_func=input):
    while True:
        choice = get_user_choice(input_func)

        if choice == 'q':
            return "Thank you for using the calculator. Goodbye!"

        if choice not in ['1', '2', '3', '4']:
            print_it("Invalid choice. Please try again.")
            continue

        num1, num2 = get_numbers(choice, input_func)

        if choice == '1':
            result = Calculator.add(num1, num2)
            return f'Add {num1} + {num2} is equal to {result}'
        elif choice == '2':
            result = Calculator.multiply(num1, num2)
            return f'Multiply {num1} * {num2} is equal to {result}'
        elif choice == '3':
            result = Calculator.divide(num1, num2)
            return f'Divide {num1} / {num2} is equal to {result}'
        elif choice == '4':
            result = Calculator.subtract(num1, num2)
            return f'Subtract {num1} - {num2} is equal to {result}'


def interactive_main():
    while True:
        result = main_repl_user_interaction()
        print_it(result)
        if result.startswith("Thank you for using"):
            break


if __name__ == "__main__":
    interactive_main()