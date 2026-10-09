"""Random observers covering the span: a seed, the number of observers and a
mode. Mode 0 lays a chain of overlapping observers and scatters short ones,
mode 1 builds a chain where each observer overlaps its neighbours almost
entirely, mode 2 uses small integer times with many touching ends."""

import math
import random
import sys

SCALE = 100
RANGE = 10**6
STRETCH = 0.95
LOOSE = 0.5
STEP = 3
SPAN = 4


def chain(rng, start, end, count, overlap):
    """count observers covering [start, end], neighbours sharing up to
    overlap of each observer."""
    cuts = sorted(rng.uniform(start, end) for _ in range(count - 1))
    cuts = [start] + cuts + [end]
    out = []
    for k in range(count):
        a, b = cuts[k], cuts[k + 1]
        width = b - a
        out.append((max(start, a - overlap * width * rng.random()), b))
    return out


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        t0, t1 = 0, rng.randint(1, n)
        obs = []
        cur = t0
        while cur < t1:
            nxt = rng.randint(cur + 1, min(t1, cur + STEP))
            obs.append((max(t0, cur - rng.randint(0, 1)), nxt))
            cur = nxt
        while len(obs) < n:
            a = rng.randint(t0, t1 - 1)
            obs.append((a, rng.randint(a + 1, min(t1, a + SPAN))))
        obs = obs[:n]
        rng.shuffle(obs)
        lines = ["%d %d" % (t0, t1), str(len(obs))] + ["%d %d" % o for o in obs]
        sys.stdout.write("\n".join(lines) + "\n")
        return
    t0 = rng.randint(-RANGE, RANGE) / SCALE
    t1 = t0 + rng.randint(1, RANGE) / SCALE
    if mode == 1:
        back = chain(rng, t0, t1, max(1, n // 2), 0.0)
        obs = []
        for k, (a, b) in enumerate(back):
            # stretch each observer almost to the end of the next one
            nxt = back[k + 1][1] if k + 1 < len(back) else b
            obs.append((a, b + (nxt - b) * STRETCH))
    else:
        obs = chain(rng, t0, t1, max(1, n // 3), LOOSE)
    reach = (t1 - t0) * SPAN / n
    while len(obs) < n:
        a = rng.uniform(t0, t1)
        obs.append((a, rng.uniform(a, min(t1, a + reach))))
    rng.shuffle(obs)
    # round outwards to the grid, so the chain still covers the span
    fmt = []
    for a, b in obs:
        lo = max(round(t0 * SCALE), math.floor(a * SCALE))
        hi = min(round(t1 * SCALE), math.ceil(b * SCALE))
        if hi <= lo:
            lo, hi = (lo - 1, lo) if hi == round(t1 * SCALE) else (lo, lo + 1)
        fmt.append((lo / SCALE, hi / SCALE))
    lines = ["%.2f %.2f" % (t0, t1), str(len(fmt))] + ["%.2f %.2f" % o for o in fmt]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
