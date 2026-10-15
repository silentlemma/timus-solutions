"""One test from a seed and a mode: obstacles and an exit at random places
(mode 1 a short line, mode 2 up to 100 obstacles over the whole range,
mode 3 the exit between the nearest obstacles, so it can be reached),
kept to the promise that both walks end."""

import random
import sys

LIMIT = 1000
MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    span = 10 if mode == 1 else LIMIT
    if mode == 3:
        x = rng.choice([-1, 1]) * rng.randint(1, LIMIT - 1)
        lo, hi = min(0, x), max(0, x)
        outside = [v for v in range(-LIMIT, LIMIT + 1) if v < lo or v > hi]
        walls = rng.sample(outside, rng.randint(0, MOST - 2))
        walls += [rng.randint(-LIMIT, lo - 1), rng.randint(hi + 1, LIMIT)]
        walls = list(set(walls))
        rng.shuffle(walls)
        print(len(walls), x)
        print(*walls)
        return
    while True:
        x = rng.choice([v for v in range(-span, span + 1) if v])
        n = rng.randint(0, min(MOST, 2 * span - 1))
        walls = rng.sample([v for v in range(-span, span + 1) if v not in (0, x)], n)
        # both directions must meet the exit or an obstacle
        ahead = x > 0 or any(w > 0 for w in walls)
        behind = x < 0 or any(w < 0 for w in walls)
        if ahead and behind:
            break
    print(n, x)
    print(*walls)


main()
