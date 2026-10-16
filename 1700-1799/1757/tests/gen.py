"""One test from a seed and a mode: mode 1 up to 6 small bars, mode 2
1000 bars of any weight and fineness, mode 3 1000 heavy bars and an
order for almost all of their weight at a reachable fineness, mode 4 like mode 2 with the
fineness asked at the very edge of what is possible, mode 5 like mode 2
with the fineness just outside it, mode 6 maximum-weight bars whose whole
store has fineness 500, mode 7 paired bars excluding fineness 500 with one gram left unused,
mode 8 shuffled unit-weight bars at an exact richest feasible endpoint."""

import random
import sys

FEW = 6
MOST = 1000
HEAVY = 990
SCALE = 1000
HALF = 0.5


def edge(mass, purity, need, richest):
    """The fineness of the richest or poorest mix of the needed weight,
    rounded so that it stays reachable."""
    left, gold = need, 0
    for i in sorted(range(len(mass)), key=lambda i: purity[i], reverse=richest):
        part = min(mass[i], left)
        gold += part * purity[i]
        left -= part
    return gold // need if richest else -(-gold // need)


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7):
        purity = []
        for _ in range(MOST // 2):
            p = rng.randint(0, SCALE)
            if mode == 7 and p == SCALE // 2:
                p -= 1
            purity.extend((p, SCALE - p))
        rng.shuffle(purity)
        print(MOST, MOST * MOST - (mode == 7), SCALE // 2)
        for p in purity:
            print(MOST, p)
        return
    if mode == 8:
        purity = list(range(SCALE))
        rng.shuffle(purity)
        print(MOST, MOST - 1, SCALE // 2)
        for p in purity:
            print(1, p)
        return
    n = rng.randint(1, FEW) if mode == 1 else MOST
    low_mass = HEAVY if mode == 3 else 1
    mass = [rng.randint(low_mass, MOST) for _ in range(n)]
    purity = [rng.randint(0, SCALE) for _ in range(n)]
    total = sum(mass)
    if mode == 3:
        need = total - rng.randint(0, MOST)
    else:
        need = rng.randint(1, min(total + 1, SCALE * SCALE))
    need = max(1, min(need, SCALE * SCALE))
    fineness = rng.randint(0, SCALE)
    if mode == 3 and need <= total:
        low, high = edge(mass, purity, need, False), edge(mass, purity, need, True)
        fineness = rng.randint(low, high) if low <= high else fineness
    if mode >= 4 and need <= total:
        richest = rng.random() < HALF
        fineness = edge(mass, purity, need, richest)
        if mode == 5:
            fineness += 1 if richest else -1
        fineness = max(0, min(SCALE, fineness))
    print(n, need, fineness)
    for i in range(n):
        print(mass[i], purity[i])


main()
