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
    assert result == expected, f"Expected addition({a}, {b}) to be {expected,}, but got {result}"


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (3, 3, 0),
        (0, 0, 0),
        (-2, 2, -4),
        (5.5, 5.5, 0),
        (2.5, -5.5, 8),
    ],

    # List of labels for test cases above
    ids=[
        "minus_two_positive_integers",
        "minus_two_zeros",
        "minus-_negative_and_positive_floats",
        "minus-_two_positive_floats",
        "minus_negative_and_positive_floats",
    ]

)

def test_subtraction(a: Number, b: Number, expected: Number) -> None:
    result = Operations.subtraction(a,b)
    assert result == expected, f"Expected addition({a}, {b}) to be {expected,}, but got {result}"


"""def test_multiplication():
    assert multiplication(1,1) == 1

def test_division_positive():
    assert division(1,1) == 1

def test_division_negative():
     with pytest.raises(ValueError, match="Division by zero is not allowed."):
        division(1, 0)"""