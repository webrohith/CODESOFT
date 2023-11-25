class Calculator:
    def __init__(self):
        self.operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide
        }

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2 if num2 != 0 else "Error: Division by zero"

    def calculate(self, num1, num2, operation):
        if operation in self.operations:
            return self.operationsoperation
        else:
            return "Error: Invalid operation"

def main():
    calculator = Calculator()
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    result = calculator.calculate(num1, num2, operation)
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()