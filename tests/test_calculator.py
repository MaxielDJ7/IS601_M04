""" tests/test_calculator.py """
import sys
import pytest
from io import StringIO

from pytest import MonkeyPatch
from app.calculator import calculator, display_history, display_help


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
    assert "Result: AddCalculation: 2.0 Add 3.0 = 5.0" in output


def test_subtraction(monkeypatch: MonkeyPatch):
    """Test subtraction operation in REPL."""
    inputs = ["subtract 5 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: SubtractCalculation: 5.0 Subtract 2.0 = 3.0" in output


def test_multiplication(monkeypatch: MonkeyPatch):
    """Test multiplication operation in REPL."""
    inputs = ["multiply 4 5", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: MultiplyCalculation: 4.0 Multiply 5.0 = 20.0" in output


def test_division(monkeypatch: MonkeyPatch):
    """Test division operation in REPL."""
    inputs = ["divide 10 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: DivideCalculation: 10.0 Divide 2.0 = 5.0" in output

def test_power(monkeypatch: MonkeyPatch):
    """Test power operation in REPL."""
    inputs = ["power 2 3", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: PowerCalculation: 2.0 Power 3.0 = 8.0" in output

def test_modulus(monkeypatch: MonkeyPatch):
    """Test modulus operation in REPL."""
    inputs = ["modulo 3 2", "exit"]
    output = run_calculator_with_input(monkeypatch, inputs)
    assert "Result: ModuloCalculation: 3.0 Modulo 2.0 = 1.0" in output


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

def test_calculator_history(monkeypatch, capsys):
    """
    Test the calculator's ability to display calculation history.

    AAA Pattern:
    - Arrange: Prepare a sequence of operations followed by 'history' and 'exit'.
    - Act: Call the calculator function.
    - Assert: Verify that the history is displayed correctly.
    """
    # Arrange
    user_input = 'add 10 5\nsubtract 20 3\nhistory\nexit\n'
    monkeypatch.setattr('sys.stdin', StringIO(user_input))

    # Act
    calculator()

    # Assert
    captured = capsys.readouterr()
    assert "Result: AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "Result: SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out
    assert "Calculation History:" in captured.out
    assert "1. AddCalculation: 10.0 Add 5.0 = 15.0" in captured.out
    assert "2. SubtractCalculation: 20.0 Subtract 3.0 = 17.0" in captured.out

def test_display_help(capsys):
    """
    Test the display_help function to ensure it prints the correct help message.

    AAA Pattern:
    - Arrange: No special setup required for this function.
    - Act: Call the display_help function.
    - Assert: Capture the output and verify it matches the expected help message.
    """
    # Arrange
    # No arrangement needed since display_help doesn't require any input or setup.

    # Act
    display_help()

    # Assert
    # Capture the printed output
    captured = capsys.readouterr()
    expected_output = """
    Calculator REPL Help
    --------------------
    Usage:
        <operation> <number1> <number2>
        - Perform a calculation with the specified operation and two numbers.
        - Supported operations:
            add       : Adds two numbers.
            subtract  : Subtracts the second number from the first.
            multiply  : Multiplies two numbers.
            divide    : Divides the first number by the second.

    Special Commands:
        help      : Display this help message.
        history   : Show the history of calculations.
        exit      : Exit the calculator.

    Examples:
        add 10 5
        subtract 15.5 3.2
        multiply 7 8
        divide 20 4
    """
    # Remove leading/trailing whitespace for comparison
    assert captured.out.strip() == expected_output.strip()
