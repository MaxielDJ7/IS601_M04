import pytest # Import the pytest framework for writing and running tests
# Import Union for type hinting multiple possible types
# This helps with future type cast errors that may occur otherwise
from typing import Union 
from app.operations import Operations

"""
Because we encapsulated these methods in a class we don't need to import
them individual (import addition, division, subtraction, multiplication).
Instead we just import the class.
"""

# Type alias for numbers. Either int or float

Number = Union[int, float]

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 6),
        (0, 0, 0),
        (-2, 2, 0),
        (5.5, 5.5, 11.0),
        (2.5, -5.5, -3.0),
    ],

    # List of labels for test cases above
    ids=[
        "add_two_positive_integers",
        "add_two_zeros",
        "add_negative_and_positive_floats",
        "add_two_positive_floats",
        "add_negative_and_positive_floats",
    ]


)

# Update the methods to accept the parameters from the parameterized test
# Using the acceptable types we defined 

def test_addition(a: Number, b: Number, expected: Number)-> None:

    # Create instance Ex. variable = Operations()
    # In that same line you can call methods within that class with the input

    result = Operations.addition(a,b,)

    # Confirm that the result matches the expected val from the parameterized list of tuples
    # old: assert addition(1,1) == 2

    # Python f-strings allow us to embed variables inside of the string
    assert result == expected, f"Expected addition({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 0),
        (0, 0, 0),
        (-2, 2, -4),
        (5.5, 5.5, 0.0),
        (2.5, -5.5, 8.0),
    ],

    # List of labels for test cases above
    ids=[
        "minus_two_positive_integers",
        "minus_two_zeros",
        "minus_negative_and_positive_floats",
        "minus_two_positive_floats",
        "minus_negative_and_positive_floats",
    ]

)

def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a,b)
    assert result == expected, f"Expected subtraction({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 9),
        (0, 10, 0),
        (-2, 2, -4),
        (5.5, 5.5, 30.25),
        (2.5, -5.5, -13.75),
    ],

    # List of labels for test cases above
    ids=[
        "mult_two_positive_integers",
        "mult_zero_with_positive_integer",
        "mult_negative_and_positive_floats",
        "mult_two_positive_floats",
        "mult_negative_and_positive_floats",
    ]

)
def test_multiplication(a: Number, b: Number, expected: Number) -> None:
    result = Operations.multiplication(a,b)
    assert result == expected, f"Expected multiplication({a}, {b}) to be {expected}, but got {result}"

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 1.0),
        (-4, -2, 2.0),
        (6.0, 2.0, 3.0),
        (-5.5, 5.5, -1.0),
        (0, 5, 0.0),
    ],

    # List of labels for test cases above
    ids=[
        "divide_two_positive_integers",
        "divide_two_negative_integers",
        "divide_two_positive_floats",
        "divide_negative_and_positive_floats",
        "divide_zero_by_positive_integer",
    ]

)

def test_division_positive(a: Number, b: Number, expected: Number) -> None:
    result = Operations.division(a,b)
    assert result == expected, f"Expected division({a}, {b}) to be {expected}, but got {result}"


@pytest.mark.parametrize(
    "a, b",
    [
        (1, 0),
        (-1, 0),
        (0, 0),
        
    ],

    # List of labels for test cases above
    ids=[
        "divide_positive_by_zero",
        "divide_negative_by_zero",
        "divide_zero_by_zero",
    ]

)
def test_division_negative(a: Number, b: Number) -> None:
    with pytest.raises(ValueError, match="Division by zero is not allowed.") as excinfo:
        Operations.division(a, b)
    
    assert "Division by zero is not allowed." in str(excinfo.value), \
        f"Expected error message 'Division by zero is not allowed.', but got '{excinfo.value}'"
