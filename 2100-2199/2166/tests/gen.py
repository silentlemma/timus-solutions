import argparse
import math
import random
import sys
from fractions import Fraction


LIMIT = 1000
MAX_COUNT = 100000
MEDIUM_COUNT = 1000
SMALL_COUNT = 40
SMALL_LIMIT = 5
CENTER_LIMIT = 100
NARROW_HEIGHT = 250
SIDES = 4
LEFT = 0
RIGHT = 1
BOTTOM = 2
TOP = 3
MODES = (
    "small",
    "medium",
    "max",
    "near",
    "parallel",
    "pencil",
    "concurrent",
    "boundary",
    "ordered",
    "reversed",
)


def direction(line):
    x1, y1, x2, y2 = line
    dx, dy = x2 - x1, y2 - y1
    divisor = math.gcd(dx, dy)
    dx, dy = dx // divisor, dy // divisor
    if dx < 0 or dx == 0 and dy < 0:
        dx, dy = -dx, -dy
    return dx, dy


def random_lines(rng, count, limit=LIMIT):
    lines = []
    used = set()
    while len(lines) < count:
        line = tuple(rng.randint(-limit, limit) for _ in range(SIDES))
        if line[:2] == line[2:]:
            continue
        slope = direction(line)
        if slope not in used:
            used.add(slope)
            lines.append(line)
    return lines


def pencil(rng, count, center):
    cx, cy = center
    limit = LIMIT - max(abs(cx), abs(cy))
    lines = []
    used = set()
    while len(lines) < count:
        dx, dy = rng.randint(-limit, limit), rng.randint(-limit, limit)
        if dx == 0 and dy == 0:
            continue
        line = (cx, cy, cx + dx, cy + dy)
        slope = direction(line)
        if slope not in used:
            used.add(slope)
            lines.append(line)
    return lines


def nearly_parallel(rng, count):
    lines = [
        (-LIMIT, -LIMIT, LIMIT, -LIMIT + 1),
        (-LIMIT, LIMIT - 1, LIMIT - 1, LIMIT),
    ]
    used = {direction(line) for line in lines}
    while len(lines) < count:
        dx = rng.randint(LIMIT + 1, 2 * LIMIT)
        dy = rng.randint(1, NARROW_HEIGHT)
        divisor = math.gcd(dx, dy)
        slope = dx // divisor, dy // divisor
        if slope in used:
            continue
        used.add(slope)
        x = rng.randint(-LIMIT, LIMIT - dx)
        y = rng.randint(-LIMIT, LIMIT - dy)
        lines.append((x, y, x + dx, y + dy))
    return lines


def boundary_point(rng):
    side = rng.randrange(SIDES)
    value = rng.randint(-LIMIT, LIMIT)
    if side == LEFT:
        return -LIMIT, value
    if side == RIGHT:
        return LIMIT, value
    if side == BOTTOM:
        return value, -LIMIT
    return value, LIMIT


def boundary(rng, count):
    lines = []
    used = set()
    while len(lines) < count:
        first, second = boundary_point(rng), boundary_point(rng)
        if first == second:
            continue
        line = first + second
        slope = direction(line)
        if slope not in used:
            used.add(slope)
            lines.append(line)
    return lines


def angular_key(line):
    dx, dy = direction(line)
    return (dx == 0, Fraction(dy, dx) if dx else 0)


def transform(lines, rng):
    turn = rng.randrange(SIDES)
    reflect = rng.getrandbits(1)
    result = []
    for line in lines:
        points = []
        for x, y in (line[:2], line[2:]):
            if reflect:
                x = -x
            if turn == RIGHT:
                x, y = -y, x
            elif turn == BOTTOM:
                x, y = -x, -y
            elif turn == TOP:
                x, y = y, -x
            points.extend((x, y))
        if rng.getrandbits(1):
            points = points[2:] + points[:2]
        result.append(tuple(points))
    return result


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        count = rng.randint(2, SMALL_COUNT)
        limit = rng.randint(SMALL_LIMIT, LIMIT)
        lines = random_lines(rng, count, limit)
    elif mode == "medium":
        lines = random_lines(rng, MEDIUM_COUNT)
    elif mode in ("near", "parallel"):
        count = rng.randint(2, SMALL_COUNT) if mode == "near" else MAX_COUNT
        lines = nearly_parallel(rng, count)
    elif mode == "pencil":
        center = tuple(rng.randint(-CENTER_LIMIT, CENTER_LIMIT) for _ in range(2))
        lines = pencil(rng, rng.randint(2, SMALL_COUNT), center)
    elif mode == "concurrent":
        lines = pencil(rng, MAX_COUNT, (0, 0))
    elif mode == "boundary":
        lines = boundary(rng, MAX_COUNT)
    else:
        lines = random_lines(rng, MAX_COUNT)
    lines = transform(lines, rng)
    if mode in ("ordered", "reversed"):
        lines.sort(key=angular_key, reverse=mode == "reversed")
    else:
        rng.shuffle(lines)
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=MODES)
    parser.add_argument("seed", type=int)
    args = parser.parse_args()
    lines = generate(args.mode, args.seed)
    sys.stdout.write(str(len(lines)) + "\n")
    sys.stdout.write("".join(" ".join(map(str, line)) + "\n" for line in lines))


if __name__ == "__main__":
    main()
