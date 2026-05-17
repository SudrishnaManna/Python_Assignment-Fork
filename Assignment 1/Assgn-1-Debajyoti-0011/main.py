from dataclasses import dataclass

@dataclass
class Calculator:
    num1: float
    num2: float
    operation: str = "add"

    @property
    def result(obj):

        if obj.operation == "add":
            return obj.num1 + obj.num2

        elif obj.operation == "subtract":
            return obj.num1 - obj.num2

        elif obj.operation == "multiply":
            return obj.num1 * obj.num2

        elif obj.operation == "divide":
            if obj.num2 != 0:
                return obj.num1 / obj.num2
            else:
                return "Cannot divide by zero"
        else:
            return "Invalid operation"

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operation (add/subtract/multiply/divide): ")

if op == "":
    calc = Calculator(a, b)
else:
    calc = Calculator(a, b, op)

print("Result:", calc.result)
