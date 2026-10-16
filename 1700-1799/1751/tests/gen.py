"""One test from a seed and a mode: mode 1 up to 6 hypotheses with random
links, mode 2 500 hypotheses with sparse links, mode 3 500 hypotheses in
one big cycle with extra links, mode 4 500 hypotheses in a long chain of
small cycles, mode 5 500 hypotheses with dense links, mode 6 independent
hypotheses at maximum checking time, mode 7 a nearly certain deep chain,
mode 8 random layers sharing dependencies, mode 9 a complete acyclic graph,
mode 10 a complete directed graph, mode 11 a nearly certain expensive cycle.
Modes 6 through 11 also use 500 hypotheses."""

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
    elif mode == 4:
        for i in range(n):
            start = i - i % SMALL_CYCLE
            deps[i] = {start + (i - start + 1) % SMALL_CYCLE}
            if start + SMALL_CYCLE < n:
                deps[i].add(start + SMALL_CYCLE)
            deps[i] = {d for d in deps[i] if d < n and d != i}
    elif mode == 6:
        pass
    elif mode == 7:
        for i in range(n - 1):
            deps[i].add(i + 1)
    elif mode == 8:
        width = 25
        for i in range(width, n):
            start = (i // width - 1) * width
            deps[i] = set(rng.sample(range(start, start + width), 5)) | {0}
    elif mode == 9:
        for i in range(n):
            deps[i] = set(range(i))
    elif mode == 10:
        for i in range(n):
            deps[i] = set(range(n)) - {i}
    elif mode == 11:
        for i in range(n):
            deps[i] = {(i + 1) % n}
    else:
        raise ValueError("unknown mode")
    print(n)
    for i in range(n):
        prob = round(rng.uniform(LOW, HIGH), 4)
        prob = min(max(prob, LOW), HIGH)
        if mode in (7, 9, 11):
            prob = HIGH
        elif mode == 8:
            prob = rng.randint(9900, 9999) / 10000
        time = rng.randint(1, TIME)
        if mode in (6, 11):
            time = TIME
        listed = " ".join(str(d + 1) for d in sorted(deps[i]))
        line = "%d %.4f %d %s" % (time, prob, len(deps[i]), listed)
        print(line.rstrip())


main()
