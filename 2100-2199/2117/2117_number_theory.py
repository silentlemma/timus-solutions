from math import isqrt

BOUND = 10 ** 6  # the cube root of the largest C


def main():
    c = int(input())
    if c == 0:
        print(1)  # only 0 + 0
        return
    # sqrt A + sqrt B = sqrt C exactly when C = s^2 q with q square-free and
    # A = a^2 q, B = b^2 q, a + b = s; so the answer counts the pairs a <= b
    root = 1
    d = 2
    while d <= BOUND and d * d <= c:
        while c % (d * d) == 0:
            c //= d * d
            root *= d
        if c % d == 0:
            c //= d
        d += 1
    # what is left has only prime factors above the bound, at most two of them,
    # so it holds a square factor only when it is a square itself
    if c > 1 and isqrt(c) ** 2 == c:
        root *= isqrt(c)
    print(root // 2 + 1)


main()
