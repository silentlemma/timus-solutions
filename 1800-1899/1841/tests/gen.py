"""One mountain from a seed and a mode: mode 1 a few short segments,
mode 2 the most segments zigzagging widely with the most cableways,
mode 3 the most segments zigzagging narrowly, so cableways land many
segments later, mode 4 like mode 2 with cheap cableways. The last
segment always crosses the whole width, so every cableway lands."""

import random
import sys

LIMIT = 10 ** 6
MOST = 100000
SMALL = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else MOST
    width = 10 if mode == 1 else LIMIT
    xs = []
    while len(xs) < n - 1:
        if mode == 3:
            x = rng.randint(-width // 100, width // 100) * 37 + rng.randint(-5, 5)
        else:
            x = rng.randint(-width + 1, width)
        if not xs or x != xs[-1]:
            xs.append(x)
    if xs[-1] == -width:
        xs[-1] += 1
    xs += [-width, width]
    n = len(xs) - 1
    budget = rng.randint(1, 12) if mode == 1 else MOST
    top = 30 if mode == 1 else LIMIT
    lines = []
    for i in range(n):
        a, b = xs[i], xs[i + 1]
        count = 0 if i >= n - 1 else min(budget, rng.randint(0, 3))
        lo, hi = min(a, b), max(a, b)
        picks = set()
        for _ in range(count):
            x = rng.randint(lo, hi)
            # skip the first vertex (it belongs to the segment before) and
            # the far left edge, which the last segment starts from
            if x != a and x != -width:
                picks.add(x)
        budget -= len(picks)
        picks = sorted(picks, key=lambda x: abs(x - a))
        cost = lambda: rng.randint(1, 10) if mode == 4 else rng.randint(1, top)
        pairs = [v for x in picks for v in (x, cost())]
        lines.append(" ".join(map(str, [rng.randint(1, top), len(picks)] + pairs)))
    print(n)
    print(*xs)
    print("\n".join(lines))


main()
