# Problem-1: Calculator using Class
# Language: Python
# Author: Pratheeksha M R

class Calculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def calculate(self, operation: str) -> float:
        if operation.lower() == "add":
            return self.a + self.b
        elif operation.lower() == "subtract":
            return self.a - self.b
        elif operation.lower() == "multiply":
            return self.a * self.b
        elif operation.lower() == "divide":
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"


if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        operation = input("Enter operation (add, subtract, multiply, divide): ")

        calc = Calculator(a, b)
        result = calc.calculate(operation)
        print("Result:", result)
    except ValueError:
        print("Please enter valid numeric inputs.")
