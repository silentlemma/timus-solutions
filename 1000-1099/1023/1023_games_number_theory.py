from math import isqrt

SMALLEST = 3


def main():
    k = int(input())
    # the second player wins exactly when L + 1 divides K: find the smallest
    # divisor of K that is at least 3
    for d in range(SMALLEST, isqrt(k) + 1):
        if k % d == 0:
            print(d - 1)
            return
    # no such divisor up to sqrt(K): above it the candidates are K / 2 and K
    d = k // 2 if k % 2 == 0 and k // 2 >= SMALLEST else k
    print(d - 1)


main()
