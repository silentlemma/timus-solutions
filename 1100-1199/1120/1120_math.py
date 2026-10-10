import math
import sys


def main():
    s = int(sys.stdin.read())
    # s = n*a + n(n-1)/2 with a >= 1 needs n(n+1)/2 <= s; try the longest first
    n = math.isqrt(2 * s)
    while n * (n + 1) // 2 > s:
        n -= 1
    while (s - n * (n - 1) // 2) % n:
        n -= 1
    print((s - n * (n - 1) // 2) // n, n)


main()
