def evaluate_equation(equation):
    parts = equation.split()
    operand1 = int(parts[0])
    operator = parts[1]
    operand2 = int(parts[2])


    if operator == "+":
        return operand1 + operand2
    elif operator == "-":
        return operand1 - operand2
    elif operator == "*":
        return operand1 * operand2
    elif operator == "/":
        return operand1 / operand2

equation = input("Give me a math equation: ")

result = evaluate_equation(equation)

result_float = float(result)

print(result_float)
