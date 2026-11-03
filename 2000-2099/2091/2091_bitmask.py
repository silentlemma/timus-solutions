import sys

GROUPS = 4


def main():
    tokens = iter(sys.stdin.buffer.read().split())
    n, m = int(next(tokens)), int(next(tokens))
    masks = [0] * m
    for row in range(n):
        bit = 1 << row
        for column in range(m):
            if next(tokens) == b"1":
                masks[column] |= bit
    counts = [mask.bit_count() for mask in masks]
    best, first, second = n + 1, 0, 1
    for a in range(m):
        for b in range(a + 1, m):
            # Both is the intersection; the other groups follow by subtraction.
            both = (masks[a] & masks[b]).bit_count()
            score = max(both, counts[a] - both, counts[b] - both, n - counts[a] - counts[b] + both)
            if score < best:
                best, first, second = score, a, b
            if best == (n + GROUPS - 1) // GROUPS:
                print(best)
                print(first + 1, second + 1)
                return
    print(best)
    print(first + 1, second + 1)


main()
