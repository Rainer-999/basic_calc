"""
Integration tests for the main script functionality.
"""

import pytest
from io import StringIO
import sys
from unittest.mock import patch
from app.user_interactions import main_repl_user_interaction

@pytest.fixture
def capture_stdout(monkeypatch):
    buffer = StringIO()
    monkeypatch.setattr(sys.stdout, "write", buffer.write)
    return buffer

def test_main_integration_addition(capture_stdout):
    def mock_input(prompt):
        if "choice" in prompt.lower():
            return "1"
        return "2"  # Both numbers will be 2
    
    result = main_repl_user_interaction(mock_input)
    assert result == "Add 2.0 + 2.0 is equal to 4.0"

def test_main_integration_subtraction(capture_stdout):
    def mock_input(prompt):
        if "choice" in prompt.lower():
            return "4"  # Assuming 4 is the choice for subtraction
        if "first" in prompt.lower():
            return "10"
        return "3"  # 10 minus 3
    
    result = main_repl_user_interaction(mock_input)
    assert result == "Subtract 10.0 - 3.0 is equal to 7.0"

def test_main_integration_multiplication(capture_stdout):
    def mock_input(prompt):
        if "choice" in prompt.lower():
            return "2"
        return "3"  # Both numbers will be 3
    
    result = main_repl_user_interaction(mock_input)
    assert result == "Multiply 3.0 * 3.0 is equal to 9.0"

def test_main_integration_division(capture_stdout):
    def mock_input(prompt):
        if "choice" in prompt.lower():
            return "3"
        if "first" in prompt.lower():
            return "10"
        return "2"  # 10 divided by 2
    
    result = main_repl_user_interaction(mock_input)
    assert result == "Divide 10.0 / 2.0 is equal to 5.0"

def test_main_integration_quit(capture_stdout):
    def mock_input(prompt):
        return "q"
    
    result = main_repl_user_interaction(mock_input)
    assert result == "Thank you for using the calculator. Goodbye!"