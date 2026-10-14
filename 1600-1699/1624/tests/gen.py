"""One test from a seed and a mode: a random prison (each inner door open
with some chance), two scouts at random cells, random moves reported
truthfully. Mode 1 a small prison and few reports, mode 2 the most cells
and 10^5 reports, mode 3 like mode 1 with one report flipped, mode 4 a
corridor of 150 cells, mode 5 the most reports with one flipped late.
Mode 6 a vertical corridor localized only on the last of 10^5 reports;
mode 7 a 10 by 15 prison, a shared snake walk then seeded random moves;
mode 8 two cells, early localization and a mistake on report 10^5."""

import random
import sys

MOST_CELLS = 150
MOST_REPORTS = 10**5
STEP = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1)}


def structured(rng, mode):
    if mode == 6:
        reports = [rng.choice("EW") + "-" for _ in range(MOST_REPORTS - 298)]
        reports.extend(["N+", "N+"] * 149)
        print(1, MOST_CELLS, MOST_REPORTS)
    elif mode == 8:
        reports = ["E+", "E+"]
        columns = [1, 1]
        for step in range(2, MOST_REPORTS):
            who = step % 2
            d = rng.choice("NSEW")
            ok = (d == "E" and columns[who] == 0) or (d == "W" and columns[who] == 1)
            if ok:
                columns[who] = 1 - columns[who]
            if step == MOST_REPORTS - 1:
                ok = not ok
            reports.append(d + ("+" if ok else "-"))
        print(2, 1, MOST_REPORTS)
    else:
        w, h = 10, 15
        # The snake doors are open; all other internal edges are seeded.
        path = []
        for r in range(h):
            columns = range(w) if r % 2 == 0 else range(w - 1, -1, -1)
            path.extend((r, c) for c in columns)
        doors = {tuple(sorted((a, b))) for a, b in zip(path, path[1:])}
        for r in range(h):
            for c in range(w):
                for dr, dc in [(1, 0), (0, 1)]:
                    q = (r + dr, c + dc)
                    if q[0] < h and q[1] < w and rng.random() < 0.4:
                        doors.add(tuple(sorted(((r, c), q))))
        reports = []
        for a, b in zip(path, path[1:]):
            delta = (b[0] - a[0], b[1] - a[1])
            d = next(d for d, change in STEP.items() if change == delta)
            reports.extend([d + "+", d + "+"])
        positions = [path[-1], path[-1]]
        while len(reports) < MOST_REPORTS:
            who = len(reports) % 2
            p = positions[who]
            d = rng.choice("NSEW")
            dr, dc = STEP[d]
            q = (p[0] + dr, p[1] + dc)
            ok = tuple(sorted((p, q))) in doors
            if ok:
                positions[who] = q
            reports.append(d + ("+" if ok else "-"))
        print(w, h, MOST_REPORTS)
    print("\n".join(reports))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7, 8):
        structured(rng, mode)
        return
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
