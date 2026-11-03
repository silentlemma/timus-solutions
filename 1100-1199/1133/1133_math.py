import sys


def main():
    i, current, j, later, n = map(int, sys.stdin.read().split())
    if i > j:
        i, current, j, later = j, later, i, current
    previous, coefficient = 0, 1
    for _ in range(j - i):
        previous, coefficient = coefficient, previous + coefficient
    # F(j) = F(j-i-1)*F(i) + F(j-i)*F(i+1); division is exact.
    following = (later - (coefficient - previous) * current) // previous
    while i < n:
        current, following = following, current + following
        i += 1
    while i > n:
        current, following = following - current, current
        i -= 1
    print(current)


main()
