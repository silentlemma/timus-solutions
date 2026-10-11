import sys
from bisect import bisect_left
from itertools import permutations

TOP = 101  # card values are 1..100


def main():
    nums = map(int, sys.stdin.read().split())
    n = next(nums)
    cards = [(next(nums), next(nums)) for _ in range(n)]
    blue = sorted({s for _, s in cards if s % 2})
    yellow = sorted({s for _, s in cards if s % 2 == 0})
    # who starts: the larger colour group, or either when they are equal
    starts = [(blue, yellow), (yellow, blue)]
    if len(blue) != len(yellow):
        starts = [starts[0] if len(blue) > len(yellow) else starts[1]]
    best = 0
    for first, second in starts:
        for a in permutations(first):
            for b in permutations(second):
                order = [None] * (len(a) + len(b))
                order[0::2], order[1::2] = a, b
                place = {s: i for i, s in enumerate(order)}
                for sign in (1, -1):
                    # cards that stay form an increasing run of target ranks
                    tails = []
                    for value, suit in cards:
                        rank = place[suit] * TOP + sign * value
                        k = bisect_left(tails, rank)
                        tails[k : k + 1] = [rank]
                    best = max(best, len(tails))
    print(n - best)


main()
