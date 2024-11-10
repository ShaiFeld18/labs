def calculate_mathematical_expression(num1: float, num2: float, operation: str):
    """Receives two numbers and a mathematical operation and returns the result"""
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/" and num2 != 0:
        return num1 / num2
    else:
        return None


def calculate_from_string(expression: str):
    """Receives a string with a mathematical expression and returns the result"""
    split_expression = expression.split(' ')
    result = calculate_mathematical_expression(float(split_expression[0]),
                                               float(split_expression[2]),
                                               split_expression[1])
    return result
