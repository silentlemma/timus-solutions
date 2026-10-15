import sys
from collections import Counter
from functools import lru_cache
from math import factorial

RANKS = "23456789TJQKA"
HEADER_LINES = 3  # sizes, own cards, shown cards


def partitions(total, parts):
    """The partitions of total into at most parts positive parts, each in
    decreasing order."""
    out = []

    def build(rest, top, cur):
        if rest == 0:
            out.append(tuple(cur))
            return
        if len(cur) == parts:
            return
        for x in range(min(rest, top), 0, -1):
            cur.append(x)
            build(rest - x, x, cur)
            cur.pop()

    build(total, total, [])
    return out


def main():
    lines = sys.stdin.read().split("\n")
    n, m, k = (int(w) for w in lines[0].split())
    own = Counter(RANKS.index(c) for c in lines[1].strip())
    shown = Counter(RANKS.index(c) for c in lines[2].strip())
    rest = " ".join(lines[HEADER_LINES:]).split()
    count = int(rest[0])
    combos, pos = [], 1
    for _ in range(count):
        size = int(rest[pos])
        combos.append(tuple(sorted((int(w) for w in rest[pos + 1:pos + 1 + size]), reverse=True)))
        pos += 1 + size

    @lru_cache(maxsize=None)
    def best(hand):
        """The most valuable combination a hand with these sorted rank
        counts holds, or -1: (v1, ..., vL) fits when the i-th largest count
        is at least the i-th largest v."""
        for c in range(count - 1, -1, -1):
            need = combos[c]
            if len(need) <= len(hand) and all(h >= v for h, v in zip(hand, need)):
                return c
        return -1

    rank_count = len(RANKS)
    split = {(s, g): partitions(s, g) for s in range(m + 1) for g in range(1, rank_count + 1)}

    @lru_cache(maxsize=None)
    def rival(common):
        """For common rank counts (sorted, zeros included), the chance that
        a rival's best combination is below c, for every c. The rival's m
        cards go over the ranks; ranks with equal common counts are
        interchangeable, so each group takes a partition of its share,
        times the ways to place it on the group's ranks."""
        states = {((), 0): 1.0}  # (sorted nonzero counts, cards used): weight
        for v, g in Counter(common).items():
            nxt = {}
            for (shape, used), w in states.items():
                for s in range(m - used + 1):
                    for p in split[(s, g)]:
                        ways = factorial(g) / factorial(g - len(p))
                        for mult in Counter(p).values():
                            ways /= factorial(mult)
                        for x in p:
                            ways /= factorial(x)
                        added = [v + x for x in p] + [v] * (g - len(p) if v else 0)
                        key = (tuple(sorted(shape + tuple(added), reverse=True)), used + s)
                        nxt[key] = nxt.get(key, 0.0) + w * ways
            states = nxt
        scale = factorial(m) / rank_count ** m
        dist = [0.0] * (count + 1)  # dist[c + 1]: chance of best combination c
        for (shape, used), w in states.items():
            if used == m:
                dist[best(shape) + 1] += w * scale
        below = [0.0] * (count + 1)  # below[c + 1]: chance the best is under c
        for c in range(count):
            below[c + 1] = below[c] + dist[c]
        return below

    # the hidden common cards: every way to spread them over the ranks
    hidden = k - sum(shown.values())
    answer = 0.0
    scale = factorial(hidden) / rank_count ** hidden

    def spread(r, left, weight, common):
        nonlocal answer
        if r == rank_count - 1:
            common[r] = shown[r] + left
            weight /= factorial(left)
            mine = best(tuple(sorted((common[i] + own[i] for i in range(rank_count)
                                      if common[i] + own[i]), reverse=True)))
            if mine >= 0:
                beat = rival(tuple(sorted(common, reverse=True)))[mine + 1]
                answer += weight * scale * beat ** (n - 1)
            return
        for x in range(left + 1):
            common[r] = shown[r] + x
            spread(r + 1, left - x, weight / factorial(x), common)

    spread(0, hidden, 1.0, [0] * rank_count)
    print("%.10f" % answer)


main()
