import sys
from itertools import accumulate


def main():
    line = sys.stdin.readline().strip()
    # the balance after each prefix; a shift that starts right after a prefix
    # of the lowest balance never goes below zero, any other shift does
    prefix = list(accumulate(1 if c == "(" else -1 for c in line))
    print(prefix.count(min(prefix)) if prefix[-1] == 0 else 0)


main()
