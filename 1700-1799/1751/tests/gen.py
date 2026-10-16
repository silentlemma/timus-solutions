"""One test from a seed and a mode: mode 1 up to 6 hypotheses with random
links, mode 2 500 hypotheses with sparse links, mode 3 500 hypotheses in
one big cycle with extra links, mode 4 500 hypotheses in a long chain of
small cycles, mode 5 500 hypotheses with dense links."""

import random
import sys

FEW = 6
MOST = 500
TIME = 1000
LOW, HIGH = 0.0001, 0.9999
SPARSE = 3
DENSE = 60
SMALL_CYCLE = 4


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 1 else MOST
    deps = [set() for _ in range(n)]
    if mode == 1:
        for i in range(n):
            deps[i] = {j for j in range(n) if j != i and rng.random() < 0.3}
    elif mode in (2, 5):
        links = SPARSE if mode == 2 else DENSE
        for i in range(n):
            deps[i] = {rng.randrange(n) for _ in range(rng.randint(0, links))} - {i}
    elif mode == 3:
        for i in range(n):
            deps[i] = {(i + 1) % n} | {rng.randrange(n) for _ in range(SPARSE)}
            deps[i].discard(i)
    else:
        for i in range(n):
            start = i - i % SMALL_CYCLE
            deps[i] = {start + (i - start + 1) % SMALL_CYCLE}
            if start + SMALL_CYCLE < n:
                deps[i].add(start + SMALL_CYCLE)
            deps[i] = {d for d in deps[i] if d < n and d != i}
    print(n)
    for i in range(n):
        prob = round(rng.uniform(LOW, HIGH), 4)
        prob = min(max(prob, LOW), HIGH)
        listed = " ".join(str(d + 1) for d in sorted(deps[i]))
        line = "%d %.4f %d %s" % (rng.randint(1, TIME), prob, len(deps[i]), listed)
        print(line.rstrip())


main()
