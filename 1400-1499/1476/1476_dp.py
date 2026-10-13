import sys
from math import comb


def main():
    m, n, k = (int(x) for x in sys.stdin.read().split())
    # step[c][d]: ways to follow a column with c ones by one with d ones,
    # turning at most k zeros into ones
    step = [[0] * (m + 1) for _ in range(m + 1)]
    for c in range(m + 1):
        for t in range(min(k, m - c) + 1):
            for s in range(c + 1):
                step[c][s + t] += comb(m - c, t) * comb(c, s)
    # ways[c]: fillings of the columns so far whose last column has c ones
    ways = [comb(m, c) for c in range(m + 1)]
    for _ in range(n - 1):
        ways = [sum(ways[c] * step[c][d] for c in range(m + 1)) for d in range(m + 1)]
    print(sum(ways))


main()
