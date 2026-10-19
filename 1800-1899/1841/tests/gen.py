"""One mountain from a seed and a mode: mode 1 a few short segments,
mode 2 the most segments zigzagging widely with the most cableways,
mode 3 the most segments zigzagging narrowly, so cableways land many
segments later, mode 4 like mode 2 with cheap cableways.
Mode 5 uses the maximum walking cost with no cableways; mode 6 puts all
cableways on one segment; mode 7 has one shared-vertex cableway landing
at the top after many narrow bends; mode 8 is a small random mountain
with mixed rates and shared-vertex starts. For modes 5-8 an optional third
argument sets the size: segments for 5, 7, 8, cableways for 6. Defaults
are 100000 for modes 5-7 and 60 for mode 8 (which allows 2-200 segments;
mode 7 needs at least 3). Every cableway has a later meeting with the path."""

import random
import sys

LIMIT = 10 ** 6
MOST = 100000
SMALL = 6


def structured(seed, mode):
    rng = random.Random(seed)
    size = int(sys.argv[3]) if len(sys.argv) > 3 else (60 if mode == 8 else MOST)
    if not 1 <= size <= MOST:
        raise ValueError("size must be between 1 and 100000")
    if mode == 5:
        xs = [-LIMIT if i % 2 == 0 else LIMIT for i in range(size + 1)]
        rows = [(LIMIT, []) for _ in range(size)]
    elif mode == 6:
        xs = [-LIMIT, LIMIT, -LIMIT]
        picks = sorted(rng.sample(range(-LIMIT, LIMIT), size))
        rows = [(1, [(x, rng.randint(1, LIMIT)) for x in picks]), (1, [])]
    elif mode == 7:
        if size < 3:
            raise ValueError("mode 7 needs at least 3 segments")
        xs = [0, LIMIT] + [-1 if i % 2 == 0 else 1 for i in range(size - 2)]
        xs.append(LIMIT)
        rows = [(rng.randint(1, LIMIT), []) for _ in range(size)]
        # Listed at the upper segment's first vertex, owned by the lower one.
        rows[1][1].append((LIMIT, 1))
    elif mode == 8:
        if not 2 <= size <= 200:
            raise ValueError("mode 8 needs between 2 and 200 segments")
        xs = []
        while len(xs) < size - 1:
            x = rng.randint(-12, 12)
            if not xs or x != xs[-1]:
                xs.append(x)
        xs += [-13, 13]
        rows = []
        used = set()
        for i, (a, b) in enumerate(zip(xs, xs[1:])):
            candidates = []
            if i + 1 < size:
                for x in range(min(a, b), max(a, b) + 1):
                    owner = i - 1 if i and x == a else i
                    if x != -13 and (owner, x) not in used:
                        candidates.append(x)
            picks = rng.sample(candidates, rng.randint(0, min(5, len(candidates))))
            picks.sort(key=lambda x: abs(x - a))
            pairs = []
            for x in picks:
                owner = i - 1 if i and x == a else i
                used.add((owner, x))
                pairs.append((x, rng.choice((1, rng.randint(1, LIMIT)))))
            rows.append((rng.choice((1, LIMIT, rng.randint(2, LIMIT - 1))), pairs))
    else:
        raise ValueError("unknown mode")
    print(len(rows))
    print(*xs)
    for rate, pairs in rows:
        print(rate, len(pairs), *(value for pair in pairs for value in pair))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    if mode >= 5:
        structured(seed, mode)
        return
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
