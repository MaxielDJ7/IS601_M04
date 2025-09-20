class Operations:

    # Static methods allow us to use these methods without needing to create an instance of the class
    # This is an example of encapsulation. Methods are encapsulated within a class.
    
    @staticmethod
    def addition(a: float, b:float) -> float:
        return a + b

    @staticmethod
    def subtraction(a: float, b:float) -> float:
        return a - b

    @staticmethod
    def multiplication(a: float, b:float) -> float:
        return a * b

    @staticmethod
    def division(a: float, b:float) -> float:
        if b == 0:
            raise ValueError("Division by zero is not allowed.") 
        return a / b  