#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    arguments = argv[1:]
    summation = 0
    for i in range(0, len(arguments), 1):
        summation += int(arguments[i])
    print("{:d}".format(summation))
