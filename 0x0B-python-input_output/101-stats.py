#!/usr/bin/python3
"""
Module: 101-stats
Description: performs log parsing and computes metrics.
"""


def print_statistics(total_size: int, my_dict: dict):
    """Performs metrics."""
    print("File size: {:d}".format(total_size))
    for key in sorted(my_dict):
        print("{}: {}".format(key, my_dict[key]))
    return None


if __name__ == "__main__":
    import sys
    try:
        codes = {}
        allowed_ = ["200", "301", "400", "401", "403", "404", "405", "500"]
        count = 0
        size = 0
        for line in sys.stdin:
            if count == 10:
                print_statistics(size, codes)
                count = 1
            else:
                count = count + 1
            line = line.split(" ")
            code = line[-2]
            if code in allowed_:
                if code not in codes:
                    codes[code] = 1
                else:
                    codes[code] += 1
            try:
                f_size = line[-1]
                size = size + int(f_size)
            except (ValueError, IndexError):
                pass
        print_statistics(size, codes)
    except KeyboardInterrupt:
        print_statistics(size, codes)
        raise
