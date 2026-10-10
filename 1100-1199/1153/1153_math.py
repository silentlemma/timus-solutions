from math import isqrt

# 8 S + 1 = (2 N + 1)^2 for S = N (N + 1) / 2
EIGHT = 8


def main():
    total = int(input())
    print((isqrt(EIGHT * total + 1) - 1) // 2)


main()
