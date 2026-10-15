import sys
from math import isqrt

SMALL = 100  # below this the first candidates are simply tried in turn


def ceil_sqrt(v):
    root = isqrt(v)
    return root if root * root == v else root + 1


def fits(n, k):
    return n // k == n // (k + 1)


def least(n):
    # the shares agree exactly when n mod k >= n div k, which needs k > s,
    # s = isqrt(n); with k = s + x and e = n - s^2 the quotient is s - x or
    # s - x + 1, and each case gives the least x in closed form
    if n < SMALL:
        k = 1
        while not fits(n, k):
            k += 1
        return k
    s = isqrt(n)
    e = n - s * s
    xs = []
    gap = s - e
    if gap >= 1:
        # quotient s - x: the least x with x^2 + x >= gap (then x^2 - x < gap)
        x = isqrt(gap)
        while x * x + x < gap:
            x += 1
        while x > 1 and (x - 1) * (x - 1) + (x - 1) >= gap:
            x -= 1
        xs.append(x)
    # quotient s - x + 1: x^2 >= 2s - e + 1 > (x - 1)^2
    xs.append(ceil_sqrt(2 * s - e + 1))
    found = [s + x + d for x in xs for d in (-1, 0, 1) if x + d >= 1 and fits(n, s + x + d)]
    return min(found)


def main():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    print("\n".join(str(least(int(w))) for w in data[1:1 + t]))


main()
