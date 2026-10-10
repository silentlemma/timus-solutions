import sys
from functools import lru_cache


def main():
    tok = list(map(int, sys.stdin.read().split()))
    n, monsters = tok[0], tok[1 : 1 + tok[0]]
    # a volley at i clears balconies i - 1, i and i + 1 around the circle
    volleys = [1 << (i - 1) % n | 1 << i | 1 << (i + 1) % n for i in range(n)]

    def alive(mask):
        return sum(monsters[i] for i in range(n) if mask >> i & 1)

    @lru_cache(maxsize=None)
    def damage(mask):
        # the least damage still to come with these balconies occupied; the
        # monsters left after each volley fire once
        if not mask:
            return 0
        best = None
        for v in volleys:
            if mask & v:
                rest = mask & ~v
                cost = alive(rest) + damage(rest)
                if best is None or cost < best:
                    best = cost
        return best

    print(damage((1 << n) - 1))


main()
