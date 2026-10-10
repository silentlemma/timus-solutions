import sys
from math import inf


def main():
    it = (t for t in sys.stdin.read().split() if t != "*")
    levels = int(next(it))
    # the cheapest cost of reaching each planet of the current level
    cost = [0]
    for _ in range(levels):
        nxt = []
        for _ in range(int(next(it))):
            best = inf
            while (src := int(next(it))) != 0:
                price = int(next(it))
                best = min(best, cost[src - 1] + price)
            nxt.append(best)
        cost = nxt
    print(min(cost))


main()
