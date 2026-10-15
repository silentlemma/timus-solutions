"""One test from a seed and a mode: mode 1 small random boxes, mode 2 the
largest sizes, mode 3 more useful boxes than coverable coins, mode 4 few
boxes holding many coins, mode 5 wanted coins missing from every box."""

import random
import sys

MOST_N = 100
MOST_K = 50


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(1, 8), rng.randint(1, 6)
    else:
        n, k = rng.randint(MOST_N // 2, MOST_N), rng.randint(MOST_K // 2, MOST_K)
    coins = list(range(1, n + 1))
    m = rng.randint(1, n)
    wanted = rng.sample(coins, m)
    boxes = []
    for _ in range(k):
        if mode == 3:
            size = rng.randint(1, 3)
            pool = wanted[:max(1, m // 4)] + [c for c in coins if c not in wanted]
            box = rng.sample(pool, min(size, len(pool)))
        elif mode == 4:
            box = rng.sample(coins, rng.randint(n // 2, n))
        elif mode == 5:
            others = [c for c in coins if c not in wanted[:m // 2]] or coins
            box = rng.sample(others, rng.randint(1, min(len(others), 5)))
        else:
            box = rng.sample(coins, rng.randint(1, min(n, 10)))
        boxes.append(box)
    print(n, k)
    for box in boxes:
        print(len(box), *box)
    print(m, *wanted)


main()
