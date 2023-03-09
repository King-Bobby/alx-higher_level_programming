#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] == '+':
        operator = add
    elif argv[2] == '-':
        operator = sub
    elif argv[2] == '*':
        operator = mul
    elif argv[2] == '/':
        operator = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    print("{} {} {} = {}".format(a, argv[2], b, operator(a, b)))
    exit(0)
