def simple_calculator(num1, num2, operation="+"):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero."
        return num1 / num2
    else:
        return f"Error: '{operation}' is invalid. Please choose from +, -, *, /."

print(simple_calculator(10, 5))
print(simple_calculator(10, 5, "-"))
print(simple_calculator(10, 5, "*"))
print(simple_calculator(10, 5, "/"))
print(simple_calculator(10, 5, "%"))