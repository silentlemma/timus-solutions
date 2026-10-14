"""One test from a seed and a mode: a random prison (each inner door open
with some chance), two scouts at random cells, random moves reported
truthfully. Mode 1 a small prison and few reports, mode 2 the most cells
and 10^5 reports, mode 3 like mode 1 with one report flipped, mode 4 a
corridor of 150 cells, mode 5 the most reports with one flipped late."""

import random
import sys

MOST_CELLS = 150
MOST_REPORTS = 10**5
STEP = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        w, h = MOST_CELLS, 1
    elif mode in (2, 5):
        w = rng.choice([10, 15, 30, 50])
        h = MOST_CELLS // w
    else:
        w, h = rng.randint(1, 6), rng.randint(1, 6)
        if w * h < 2:
            w = 2
    k = MOST_REPORTS if mode in (2, 5) else rng.randint(1, 3000 if mode == 4 else 300)
    chance = rng.uniform(0.3, 1.0)
    doors = {}  # (cell, direction) -> open; edges at the border stay walls

    def is_open(r, c, d):
        dr, dc = STEP[d]
        r2, c2 = r + dr, c + dc
        if not (0 <= r2 < h and 0 <= c2 < w):
            return False
        key = tuple(sorted([(r, c), (r2, c2)]))
        if key not in doors:
            doors[key] = rng.random() < chance
        return doors[key]

    pos = [(rng.randrange(h), rng.randrange(w)) for _ in range(2)]
    flip = rng.randint(1, k) if mode == 3 else (rng.randint(k // 2, k) if mode == 5 else 0)
    print(w, h, k)
    out = []
    for step in range(1, k + 1):
        who = (step - 1) % 2
        r, c = pos[who]
        d = rng.choice("NSEW")
        ok = is_open(r, c, d)
        if ok:
            pos[who] = (r + STEP[d][0], c + STEP[d][1])
        if step == flip:
            ok = not ok
        out.append(d + ("+" if ok else "-"))
    print("\n".join(out))


main()
