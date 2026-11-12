from collections import defaultdict
from math import factorial
from sys import stdin

ISLANDS = range(3)
HOME = 0


def main():
    n = int(stdin.buffer.read())
    # The first city is fixed on the home island.
    ways = {((1, 0, 0), HOME): 1}
    for _ in range(len(ISLANDS) * n - 1):
        next_ways = defaultdict(int)
        for (used, last), count in ways.items():
            for island in ISLANDS:
                if island == last or used[island] == n:
                    continue
                following = list(used)
                following[island] += 1
                next_ways[tuple(following), island] += count
        ways = next_ways

    patterns = sum(count for (_, last), count in ways.items() if last != HOME)
    print(patterns * factorial(n - 1) * factorial(n) ** 2 // 2)


main()
