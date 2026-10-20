"""Knights from "MODE SEED": mode 1 a few knights with small numbers, mode
2 10^5 random knights, mode 3 10^5 knights where one rich knight can just
win, mode 4 10^5 knights where the rich knight is one coin short, mode 5
increasing shields with no coins and the last knight winning. Mode 5 takes
an optional N after SEED (default 10^5, range 1..10^5)."""

import random
import sys

MAX_N = 10 ** 5
MAX_V = 10 ** 9
SMALL_N = 4
SMALL_V = 4
WEAK = 10 ** 6


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, SMALL_N)
        knights = [[rng.randint(0, SMALL_V) for _ in range(3)] for _ in range(n)]
    elif mode == 2:
        n = MAX_N
        knights = [[rng.randint(0, MAX_V) for _ in range(3)] for _ in range(n)]
    elif mode == 5:
        n = int(sys.argv[3]) if len(sys.argv) > 3 else MAX_N
        if not 1 <= n <= MAX_N:
            raise ValueError("N must be between 1 and 10^5")
        knights = [[n - 1, shield, 0] for shield in range(1, n + 1)]
    else:
        n = MAX_N
        knights = [[rng.randint(0, WEAK) for _ in range(3)] for _ in range(n)]
        best_attack = max(a + g for a, d, g in knights)
        best_shield = max(d + g for a, d, g in knights)
        a, d = rng.randint(0, WEAK), rng.randint(0, WEAK)
        need = max(0, best_attack + 1 - d) + max(0, best_shield - a)
        g = need if mode == 3 else max(0, need - 1)
        knights[rng.randrange(n)] = [a, d, g]
    print(n)
    print("\n".join(" ".join(map(str, k)) for k in knights))


main()
