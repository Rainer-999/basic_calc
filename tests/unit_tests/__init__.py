"""
This module contains integration tests for the main program logic.

It tests the integration of arithmetic operations, string formatting,
and printing functionality.
"""

import pytest
from app.utils import print_it
from app.operations import add, multiply
from app.main import main  # Replace 'your_main_module' with the actual module name


def test_main_integration(capsys):
    """
    Test the integration of the main function.

    This test ensures that the main function correctly integrates
    the add, multiply, and print_it functions, producing the expected output.
    """
    # Call the main function
    main()

    # Capture the printed output
    captured = capsys.readouterr()

    # Define the expected output
    expected_output = (
        "Add 2 + 2 is equal to 4\n"
        "Multiply 2 * 2 is equal to 4\n"
    )

    # Assert that the captured output matches the expected output
    assert captured.out == expected_output


def test_add_integration():
    """
    Test the integration of the add function with string formatting.

    This test ensures that the add function produces the correct result
    and that the result is correctly formatted into a string.
    """
    result = add(2, 2)
    formatted_result = f'Add 2 + 2 is equal to {result}'
    assert formatted_result == 'Add 2 + 2 is equal to 4'


def test_multiply_integration():
    """
    Test the integration of the multiply function with string formatting.

    This test ensures that the multiply function produces the correct result
    and that the result is correctly formatted into a string.
    """
    result = multiply(2, 2)
    formatted_result = f'Multiply 2 * 2 is equal to {result}'
    assert formatted_result == 'Multiply 2 * 2 is equal to 4'


def test_print_it_integration(capsys):
    """
    Test the integration of the print_it function.

    This test ensures that the print_it function correctly prints
    the given string to the console.
    """
    test_string = "Test message"
    print_it(test_string)
    captured = capsys.readouterr()
    assert captured.out.strip() == test_string


if __name__ == '__main__':
    pytest.main()