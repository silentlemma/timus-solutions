import sys


def reaches_all(edges):
    seen = pending = 1
    while pending:
        bit = pending & -pending
        pending ^= bit
        fresh = edges[bit.bit_length() - 1] & ~seen
        seen |= fresh
        pending |= fresh
    return seen == (1 << len(edges)) - 1


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    forward, reverse = [0] * n, [0] * n
    for i in range(n):
        for j in range(n):
            if next(data):
                forward[i] |= 1 << j
                reverse[j] |= 1 << i
    # The positive entries of matrix powers describe directed walks.
    print("Yes" if reaches_all(forward) and reaches_all(reverse) else "No")


main()
