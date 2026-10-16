"""One race from a seed and a mode: mode 1 a random field, mode 2 the
largest field, mode 3 the largest field with runs a few seconds apart,
so the finishing order mixes a lot, mode 4 the largest field where each
skier runs a little faster than the one before."""

import random
import string
import sys

LIMIT = 100
NAME = 20
GAP = 300
SLOWEST = 59 * 600 + 599


def fmt(run):
    return f"{run // 600:02d}:{run % 600 // 10:02d}.{run % 10}"


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, LIMIT) if mode == 1 else LIMIT
    names = set()
    while len(names) < n:
        size = rng.randint(1, NAME)
        tail = "".join(rng.choice(string.ascii_lowercase) for _ in range(size - 1))
        names.add(rng.choice(string.ascii_uppercase) + tail)
    names = list(names)
    rng.shuffle(names)
    while True:
        if mode == 3:
            base = rng.randint(20000, 25000)
            runs = [base + rng.randint(-600, 600) for _ in range(n)]
        elif mode == 4:
            runs = [rng.randint(30000, SLOWEST)]
            while len(runs) < n:
                runs.append(runs[-1] - rng.randint(1, GAP - 1))
        else:
            runs = [rng.randint(0, SLOWEST) for _ in range(n)]
        finishes = {i * GAP + r for i, r in enumerate(runs)}
        if len(set(runs)) == n and len(finishes) == n and min(runs) >= 0:
            break
    print(n)
    for name, run in zip(names, runs):
        print(name, fmt(run))


main()
