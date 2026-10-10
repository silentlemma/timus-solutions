import math
import sys

SIDE = 100


def main():
    tok = iter(map(int, sys.stdin.read().split()))
    n, m = next(tok), next(tok)
    blocks = sorted({(next(tok), next(tok)) for _ in range(next(tok))})
    # a route can use a chain of diagonal blocks increasing in both
    # coordinates; each one replaces two sides by one diagonal
    chain = [1] * len(blocks)
    for i, (x, y) in enumerate(blocks):
        for j in range(i):
            if blocks[j][0] < x and blocks[j][1] < y:
                chain[i] = max(chain[i], chain[j] + 1)
    best = max(chain, default=0)
    print(round(SIDE * (n + m - 2 * best) + SIDE * math.sqrt(2) * best))


main()
