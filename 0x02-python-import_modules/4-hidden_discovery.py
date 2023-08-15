#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    mylist = dir(hidden_4)
    for i in mylist:
        """check prefix of list item"""
        if not i.startswith("__"):
            print("{:s}".format(i))
