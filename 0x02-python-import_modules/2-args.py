#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    len_ = len(argv) - 1
    print("{:d} {:s}{:s}".
          format(len_,
                 "arguments" if (len_) != 1 else "argument",
                 "." if (len_) == 0 else ":"))
    for i, argument in enumerate(argv[1:]):
        print("{:d}: {:s}".format(i + 1, argument))
