"""One test from a seed and a mode: the mode is the number of inns, so
that every number of inns can be listed; the seed is not used."""

import sys


def main():
    _, inns = (int(v) for v in sys.argv[1:3])
    print(inns)


main()
