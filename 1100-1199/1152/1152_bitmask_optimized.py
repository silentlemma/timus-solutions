import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, monsters = data[0], data[1:]
    volleys = [1 << ((i - 1) % n) | 1 << i | 1 << ((i + 1) % n) for i in range(n)]
    memo = {0: 0}

    # include the living sum in each cached cost, computing it once per mask.
    def damage(mask):
        if mask in memo:
            return memo[mask]
        best = None
        for volley in volleys:
            rest = mask & ~volley
            if rest != mask:
                cost = damage(rest)
                if best is None or cost < best:
                    best = cost
        living = sum(value for i, value in enumerate(monsters) if mask >> i & 1)
        memo[mask] = best + living
        return best + living

    print(damage((1 << n) - 1) - sum(monsters))


main()
