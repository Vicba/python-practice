

from typing import Any


class Calculator():
    """
    This module provides basic arithmetic operations.
    """

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        sum = self.add(1, 2)
        sub = self.subtract(1, 2)
        mul = self.multiply(1, 2)
        div = self.divide(1, 2)

        return sum, sub, mul, div


    def add(self, a, b):
        """
        Add two numbers.

        Parameters:
            a (int or float): The first number.
            b (int or float): The second number.

        Returns:
            int or float: The sum of a and b.
        """
        return a + b

    def subtract(self, a, b):
        """
        Subtract one number from another.

        Parameters:
            a (int or float): The number to be subtracted from.
            b (int or float): The number to subtract.

        Returns:
            int or float: The result of a minus b.
        """
        return a - b

    def multiply(self, a, b):
        """
        Multiply two numbers.

        Parameters:
                a (int or float): The first number
                b (int or float): The second number.
        Returns:
            int or float: The product of a and b.
        """
        return a * b

    def divide(self, a, b):
        """
        Divide one number by another.

        Parameters:
            a (int or float): The numerator.
            b (int or float): The denominator.

        Returns:
            float: The result of a divided by b.

        Raises:
            ValueError: If b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b        



def main():
    calculator = Calculator()
    print(calculator.multiply.__doc__)

    print(calculator(1,2))

if __name__ == "__main__":
    main()