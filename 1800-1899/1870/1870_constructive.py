import sys
from math import gcd

# 2 * 3: both must be invertible modulo n
BAD = 6


def main():
    n = int(sys.stdin.read())
    if gcd(n, BAD) != 1:
        print("No")
        return
    # queen i on row 2i: rows 2i, diagonals 3i and anti-diagonals i are all
    # different modulo n
    print("Yes")
    print(" ".join(str(2 * i % n + 1) for i in range(n)))


main()
