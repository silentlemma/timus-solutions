import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, a = data[0], data[1 : 1 + data[0]]
    # n + 1 prefix sums modulo n take at most n values: two of them are
    # equal, and the numbers between them sum to a multiple of n
    first, total = {0: 0}, 0
    for i, x in enumerate(a, 1):
        total = (total + x) % n
        if total in first:
            part = a[first[total] : i]
            print("\n".join(map(str, [len(part)] + part)))
            return
        first[total] = i


main()
