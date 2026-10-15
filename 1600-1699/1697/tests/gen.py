"""One test from a seed and a mode: mode 1 small coordinates (many shots
graze edges and corners), mode 2 the full range of coordinates, mode 3
the sniper on the ground, mode 4 many low buildings, mode 5 A = B,
mode 6 all shots in one vertical plane that holds walls of buildings."""

import random
import sys

LIMIT = 100
MOST = 100
NEAR = 3  # the widest base side next to the plane of the shots
HALF = 0.5


def touches(box, other):
    """Whether two closed boxes share a point (bases overlap or touch)."""
    return not (box[2] < other[0] or other[2] < box[0] or box[3] < other[1] or other[3] < box[1])


def on_or_in(box, x, y, z):
    return box[0] <= x <= box[2] and box[1] <= y <= box[3] and 0 <= z <= box[4]


def segment_hits(box, ax, ay, bx, by):
    """Whether the ground segment AB shares a point with the closed base."""
    steps = 400
    for i in range(steps + 1):
        x = ax + (bx - ax) * i / steps
        y = ay + (by - ay) * i / steps
        if box[0] - 1e-9 <= x <= box[2] + 1e-9 and box[1] - 1e-9 <= y <= box[3] + 1e-9:
            return True
    return False


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    top = 6 if mode in (1, 3, 5, 6) else LIMIT
    count = {1: rng.randint(0, 4), 2: rng.randint(0, 30), 3: rng.randint(0, 4),
             4: MOST, 5: rng.randint(0, 4), 6: rng.randint(1, 4)}[mode]
    wall = rng.randint(-top + 1, top - 1)
    along_x = rng.random() < HALF
    while True:
        sx, sy = rng.randint(-top, top), rng.randint(-top, top)
        sz = 0 if mode == 3 else rng.randint(0, top)
        ax, ay = rng.randint(-top, top), rng.randint(-top, top)
        bx, by = (ax, ay) if mode == 5 else (rng.randint(-top, top), rng.randint(-top, top))
        if mode == 6 and along_x:
            sx = ax = bx = wall
        elif mode == 6:
            sy = ay = by = wall
        boxes = []
        for _ in range(count * 20):
            if len(boxes) == count:
                break
            lx, ly = rng.randint(-top, top - 1), rng.randint(-top, top - 1)
            span = 2 if mode == 4 else top
            rx = min(top, lx + rng.randint(1, span))
            ry = min(top, ly + rng.randint(1, span))
            if mode == 6:
                # a side of the base on the plane of the shots
                side = rng.randint(1, NEAR)
                low, high = (wall, wall + side) if rng.random() < HALF else (wall - side, wall)
                if along_x:
                    lx, rx = low, high
                else:
                    ly, ry = low, high
            h = rng.randint(1, 3 if mode == 4 else top)
            box = (lx, ly, rx, ry, h)
            if any(touches(box, o) for o in boxes) or on_or_in(box, sx, sy, sz):
                continue
            if segment_hits(box, ax, ay, bx, by):
                continue
            boxes.append(box)
        if len(boxes) == count or mode == 4:
            break
    print(sx, sy, sz)
    print(ax, ay, bx, by)
    print(len(boxes))
    for box in boxes:
        print(*box)


main()
