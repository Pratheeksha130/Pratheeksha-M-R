# Problem-1: Simple Calculator using Class
# Author: Pratheeksha M R

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"

# Get user input
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))
operation = input("Enter operation (add, subtract, multiply, divide): ")

# Create Calculator object
calc = Calculator()

# Perform operation
if operation == "add":
    result = calc.add(a, b)
elif operation == "subtract":
    result = calc.subtract(a, b)
elif operation == "multiply":
    result = calc.multiply(a, b)
elif operation == "divide":
    result = calc.divide(a, b)
else:
    result = "Invalid operation"

print("Result:", result)
