"""Shots and walls, up to 50 000 events: a seed and a mode. Mode 1 builds 25 000
random walls before 25 000 random shots, mode 2 mixes them, mode 3 builds
squares around the origin from the outside in, mode 4 shoots along 200
directions only, at different speeds, mode 5 builds walls whose ends lie
on shot directions, mode 6 uses short walls far from the origin, mode 7
interleaves three walls with 49 997 random shots, and mode 8 builds 49 999
random walls before a single final shot. All modes take a seed and a mode."""

import random
import sys

TOP = 10000
LINES = 49999
MAX_EVENTS = 50000


def wall(rng, top):
    while True:
        x1, y1, x2, y2 = (rng.randint(-top, top) for _ in range(4))
        if x1 * y2 - y1 * x2 != 0:
            return "wall %d %d %d %d" % (x1, y1, x2, y2)


def shot(rng, top):
    while True:
        x, y = rng.randint(-top, top), rng.randint(-top, top)
        if x or y:
            return "shot %d %d" % (x, y)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = []
    if mode == 1:
        lines = [wall(rng, TOP) for _ in range(LINES // 2)]
        lines += [shot(rng, TOP) for _ in range(LINES - len(lines))]
    elif mode == 2:
        lines = [wall(rng, TOP) if rng.random() < 0.5 else shot(rng, TOP) for _ in range(LINES)]
    elif mode == 3:
        r = TOP
        while len(lines) < LINES and r > 1:
            corners = [(r, 0), (0, r), (-r, 0), (0, -r)]
            for i in range(4):
                (x1, y1), (x2, y2) = corners[i], corners[(i + 1) % 4]
                lines.append("wall %d %d %d %d" % (x1, y1, x2, y2))
                lines.append(shot(rng, TOP))
            r -= rng.randint(1, 3)
        lines = lines[:LINES]
    elif mode == 4:
        part = TOP // 3
        dirs = [(rng.randint(-part, part), rng.randint(-part, part)) for _ in range(200)]
        dirs = [d for d in dirs if d != (0, 0)]
        for _ in range(LINES):
            if rng.random() < 0.5:
                lines.append(wall(rng, TOP))
            else:
                x, y = rng.choice(dirs)
                k = rng.randint(1, 3)
                lines.append("shot %d %d" % (k * x, k * y))
    elif mode == 5:
        dirs = [(rng.randint(-100, 100), rng.randint(-100, 100)) for _ in range(500)]
        dirs = [d for d in dirs if d != (0, 0)]
        while len(lines) < LINES:
            (x1, y1), (x2, y2) = rng.sample(dirs, 2)
            if x1 * y2 - y1 * x2 == 0:
                continue
            k1, k2 = rng.randint(1, 100), rng.randint(1, 100)
            lines.append("wall %d %d %d %d" % (k1 * x1, k1 * y1, k2 * x2, k2 * y2))
            x, y = rng.choice(dirs)
            lines.append("shot %d %d" % (x, y))
        lines = lines[:LINES]
    elif mode == 7:
        positions = {0: TOP, MAX_EVENTS // 3: TOP // 2, 2 * MAX_EVENTS // 3: 1}
        for i in range(MAX_EVENTS):
            if i in positions:
                x = positions[i]
                lines.append("wall %d %d %d %d" % (x, -TOP, x, TOP))
            else:
                lines.append(shot(rng, TOP))
    elif mode == 8:
        lines = [wall(rng, TOP) for _ in range(MAX_EVENTS - 1)]
        lines.append("shot 1 -1")
    else:
        while len(lines) < LINES:
            cx, cy = rng.randint(-TOP + 50, TOP - 50), rng.randint(-TOP + 50, TOP - 50)
            if abs(cx) < TOP // 2 and abs(cy) < TOP // 2:
                continue
            x1, y1 = cx + rng.randint(-50, 50), cy + rng.randint(-50, 50)
            x2, y2 = cx + rng.randint(-50, 50), cy + rng.randint(-50, 50)
            if x1 * y2 - y1 * x2 != 0:
                lines.append("wall %d %d %d %d" % (x1, y1, x2, y2))
            lines.append("shot %d %d" % (cx + rng.randint(-60, 60), cy + rng.randint(-60, 60)))
        lines = lines[:LINES]
    print("\n".join(lines))
    print("end")


main()
