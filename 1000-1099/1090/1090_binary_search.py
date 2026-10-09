import bisect
import sys


def main():
    tok = list(map(int, sys.stdin.buffer.read().split()))
    n, k = tok[0], tok[1]
    best, best_row = -1, 0
    for r in range(k):
        # each recruit jumps once for every earlier recruit with a larger
        # number: the earlier numbers are kept sorted to count them
        seen = []
        jumps = 0
        for i, x in enumerate(tok[2 + r * n : 2 + (r + 1) * n]):
            pos = bisect.bisect(seen, x)
            jumps += i - pos
            seen.insert(pos, x)
        if jumps > best:
            best, best_row = jumps, r + 1
    print(best_row)


main()
