"""A walk of about n segments that never leaves the hexagon of radius 100
around the centre: a seed, n and a mode. Mode 0 is random; the other modes
go back to the centre along X and Z and then mode 1 stops there, mode 2
goes 100 along Y, where Y saves steps, and mode 3 goes to (50, -50), where
it does not."""

import random
import sys

RADIUS = 100
LONGEST = 30
STEP = {"X": (1, 0), "Y": (1, 1), "Z": (0, 1)}
FINISH = {1: [], 2: [("Y", RADIUS)], 3: [("X", RADIUS // 2), ("Z", -RADIUS // 2)]}


def distance(p, q):
    return max(abs(p), abs(q)) if p * q >= 0 else abs(p) + abs(q)


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    segs, p, q = [], 0, 0
    while len(segs) < n - (len(FINISH.get(mode, [])) + 2) * (mode > 0):
        d = rng.choice("XYZ")
        length = rng.choice((-1, 1)) * rng.randint(1, LONGEST)
        dx, dy = STEP[d]
        np, nq = p + dx * length, q + dy * length
        if distance(np, nq) <= RADIUS:
            segs.append((d, length))
            p, q = np, nq
    if mode:
        segs += [s for s in (("X", -p), ("Z", -q)) if s[1]] + FINISH[mode]
    lines = [str(len(segs))] + ["%s %d" % s for s in segs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
