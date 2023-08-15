#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    operators = ["+", "-", "*", "/"]
    mylist = argv[1:]
    if len(mylist) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(mylist[0])
    b = int(mylist[2])
    if mylist[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if mylist[1] == "+":
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif mylist[1] == "-":
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif mylist[1] == "*":
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    else:
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
