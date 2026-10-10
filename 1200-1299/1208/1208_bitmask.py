import sys
from functools import lru_cache

SIZE = 3


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    teams = [set(data[1 + SIZE * i : 1 + SIZE * (i + 1)]) for i in range(k)]
    # clash[i]: the teams sharing a member with team i, i itself included
    clash = [sum(1 << j for j in range(k) if teams[i] & teams[j]) for i in range(k)]

    @lru_cache(maxsize=None)
    def best(mask):
        if mask == 0:
            return 0
        low = mask & -mask
        i = low.bit_length() - 1
        # the lowest team left is either skipped or taken with its clashes out
        return max(best(mask ^ low), 1 + best(mask & ~clash[i]))

    print(best((1 << k) - 1))


main()
