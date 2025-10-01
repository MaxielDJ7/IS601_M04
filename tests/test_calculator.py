""" tests/test_calculator.py """
import sys
import pytest
from io import StringIO

from pytest import MonkeyPatch
from app.calculator import calculator


# Helper function to capture print statements
def run_calculator_with_input(monkeypatch, inputs):
    """
    Simulates user input and captures output from the calculator REPL.
    
    :param monkeypatch: pytest fixture to simulate user input
    :param inputs: list of inputs to simulate
    :return: captured output as a string
    """
    input_iterator = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iterator))

    # Capture the output of the calculator
    captured_output = StringIO()
    sys.stdout = captured_output
    calculator()
    sys.stdout = sys.__stdout__  # Reset stdout
    return captured_output.getvalue()


# Positive Tests
def test_addition(monkeypatch: MonkeyPatch):
    """Test addition operation in REPL."""
    inputs = ["add 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output


def test_subtraction(monkeypatch: MonkeyPatch):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 3.0" in output


def test_multiplication(monkeypatch: MonkeyPatch):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 20.0" in output


def test_division(monkeypatch: MonkeyPatch):
    """Test division operation in REPL."""
    inputs = ["divide 10 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 5.0" in output

def test_power(monkeypatch: MonkeyPatch):
    """Test power operation in REPL."""
    inputs = ["power 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 8.0" in output

def test_modulus(monkeypatch: MonkeyPatch):
    """Test modulus operation in REPL."""
    inputs = ["modulo 3 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: 1.0" in output


# Negative Tests
def test_invalid_operation(monkeypatch: MonkeyPatch):
    """Test invalid operation in REPL."""
    inputs = ["floor 5 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Type 'help' to see the list of supported operations.\n" in output


def test_invalid_input_format(monkeypatch: MonkeyPatch):
    """Test invalid input format in REPL."""
    inputs = ["add two three", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Invalid input. Please follow the format" in output


@pytest.mark.parametrize(
    "command",
    [
        "divide 5 0",
        "modulo 5 0",
    ],
    ids=[
        "divide_by_zero_in_repl",
        "mod_by_zero_in_repl",
    ]
)

def test_division_mod_by_zero(monkeypatch: MonkeyPatch, command: str):
    """Test division by zero in REPL."""
    inputs = [command, "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Division by zero is not allowed" in output
