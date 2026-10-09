import sys
from functools import reduce
from math import gcd


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    # cutting a shorter piece off a longer one keeps the gcd of all lengths,
    # so the last piece is always the gcd and the answer is never ambiguous
    print(reduce(gcd, data[1 : n + 1]))


main()
