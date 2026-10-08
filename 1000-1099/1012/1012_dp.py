import sys


def main():
    n, k = map(int, sys.stdin.read().split())
    # numbers of valid prefixes ending with a zero and with another digit,
    # where the first digit is not zero
    zero, other = 0, k - 1
    for _ in range(n - 1):
        zero, other = other, (zero + other) * (k - 1)
    print(zero + other)


main()
