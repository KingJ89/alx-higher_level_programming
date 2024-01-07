#!/usr/bin/python3
if __name__ == "__main__":
    """Handles basic operations"""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    operator = sys.argv[2]

    if operator not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    try:
        a, b = map(int, sys.argv[1:4])
    except ValueError:
        print("Invalid input. Please provide valid integers for <a> and <b>")
        sys.exit(1)

    if operator == "/" and b == 0:
        print("Error: Division by zero is not allowed")
        sys.exit(1)

    result = ops[operator](a, b)
    print(f"{a} {operator} {b} = {result}")
