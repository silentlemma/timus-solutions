import sys
from math import comb


def main():
    n, k = map(int, sys.stdin.read().split())
    # z zeros, no two adjacent, among the n - 1 places after the first digit:
    # C(n - z, z) ways; the other n - z digits are nonzero
    print(sum(comb(n - z, z) * (k - 1) ** (n - z) for z in range(n // 2 + 1)))


main()
