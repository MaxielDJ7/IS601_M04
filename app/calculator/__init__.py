""" 
This file is the "app/calculator.py" file. It contains a simple calculator that can add, subtract, multiply, 
and divide numbers based on what the user types.
"""

# First, we need to get some functions that can actually do the math for us. These functions (addition, 
# subtraction, multiplication, and division) are in another file called "operations.py" in the "app" folder.
# This is like opening a toolbox and pulling out the tools we need to do our math.
from app.operations import Operations
import readline
from typing import List
from app.calculation import Calculation, CalculationFactory

def display_help() -> None:
    """
    Displays the help message with usage instructions and supported operations.
    """
    help_message = """
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
    print(help_message)


def display_history(history: List[Calculation]) -> None:
    """
    Displays the history of calculations performed during the session.

    Parameters:
        history (List[Calculation]): A list of Calculation objects representing past calculations.
    """
    if not history:
        print("No calculations performed yet.")
    else:
        print("Calculation History:")
        for idx, calculation in enumerate(history, start=1):
            print(f"{idx}. {calculation}")

def calculator():
    """Basic REPL calculator that performs addition, subtraction, multiplication, and division."""
    
     # Initialize an empty list to keep track of calculation history
    history: List[Calculation] = []
    print("Type 'help' for instructions or 'exit' to quit.\n")

    # First, we print a message to welcome the user to the calculator.
    print("Welcome to the calculator REPL! Type 'exit' to quit")
    
    # This is the part where the calculator keeps running. The 'while True' means we are going to keep 
    # doing something (in this case, asking the user for input) until we tell it to stop.
    while True:
        # Now we ask the user to type something, like "add 5 3". 
        # This will get the operation (like "add") and two numbers from the user.
        user_input = input("Enter an operation (add, subtract, multiply, divide, power, modulo) and two numbers, or 'exit' to quit: ")
       
        # Handle special commands
        command = user_input.lower()
        # This part checks if the user typed "exit". If they did, we print a message and stop the calculator.
        
        if user_input.lower() == "exit":
            print("Exiting calculator...")
            break  # This "break" command tells the program to stop running the loop and exit.
        elif not user_input:
            # Input is empty, so we skip processing and prompt again.
            continue # pragma: no cover

        # LBYL is used here to check if the user input matches any special commands.
        elif command == "help":
            display_help()
            continue
        elif command == "history":
            display_history(history)
            continue
        
        try:
            # Now we split the input into three parts: the operation (add, subtract, etc.) and the two numbers.
            operation, num1, num2 = user_input.split()
            # We have to make sure the numbers are actually numbers, so we convert them to floats.
            num1, num2 = float(num1), float(num2)
        except ValueError:
            # If the user doesn't type something correctly, like typing letters where numbers should be, we show an error.
            print("Invalid input. Please follow the format: <operation> <num1> <num2>")
            continue  # This "continue" means: try again by going back to the top of the loop.

        # Now we check what operation the user asked for and call the right function (addition, subtraction, etc.).
        # try:
        #     if operation == "add":
        #         result = Operations.addition(num1, num2)  # We call the addition function to add the two numbers.
        #     elif operation == "subtract":
        #         result = Operations.subtraction(num1, num2)  # We call the subtraction function to subtract the two numbers.
        #     elif operation == "multiply":
        #         result = Operations.multiplication(num1, num2)  # We call the multiplication function to multiply the two numbers.
        #     elif operation == "power":
        #         result = Operations.power(num1, num2)  # We call the power function.
        #     elif operation == "modulo":
        #         result = Operations.modulo(num1, num2)  # We call the modulus function.
        #     elif operation == "divide":
        #         result = Operations.division(num1, num2)  # We call the division function to divide the two numbers.
                
        #     else:
        #         # If the user types an operation we don't understand, we show them a message.
        #         print(f"Unknown operation '{operation}'. Supported operations: add, subtract, multiply, divide, power, modulo.")
        #         continue  # Go back to the top of the loop and try again.

        # Attempt to create a Calculation instance using the factory
        try:
            calculation = CalculationFactory.create_calculation(operation, num1, num2)
        except ValueError as ve:
            # Handle unsupported operations
            print(ve)
            print("Type 'help' to see the list of supported operations.\n")
            continue  # Prompt the user again

        # Attempt to execute the calculation
        try:
            result = calculation.execute()
        except ZeroDivisionError as e:
            # Handles divide or modulo by zero
            print("Division by zero is not allowed")
            continue

        except ValueError as e:
                    # This part handles the case where someone tries to divide by zero, which we can't do.
                    # The division function will throw an error if someone tries dividing by zero, and we catch that error here.
                    print(e)  # Show the error message.
                    continue  # Go back to the top of the loop and try again.
        
        #print(f"Result: {result}")

         # Prepare the result string for display
        result_str= f"Result: {result}"
        print(f"Result: {result_str}\n")


# Explanation of __init__.py:
# In Python, a file named "__init__.py" is really important. It tells Python that the folder it's in (in this case, "calculator") 
# is a special kind of folder called a "package". Think of a package like a folder that contains related code, like a toolbox with
# different tools inside.
# 
# Without the "__init__.py" file, Python won't know that the folder can be used to group code together. It’s like a flag that says,
# "Hey Python, this folder can be used to import code!"
# 
# For example, if we put the "__init__.py" file in the "calculator" folder, we can import anything inside it by saying something like:
# "from app.calculator import calculator". The "__init__.py" file can be empty, or it can have code in it, but its main job is just 
# to make the folder a package.
