"""Deterministic chimney inputs: python gen.py MODE SEED.

Modes 1 and 2 make small arbitrary and medium passable chimneys. Modes 3 and 4
make maximal ascending and descending rows. Modes 5, 6 and 7 make maximal
zigzags with short, full-height and maximal rectangle heights. Mode 8 makes
arbitrary maximal rows, mode 9 makes sawtooth rows, mode 10 maximizes the
answer, and mode 11 uses the maximal rectangle width.
"""

import random
import sys

MIN_WIDTH = 3
MAX_HEIGHT = 100_000
MAX_SIDE = 1_000_000_000
SMALL_HEIGHT = 40
SMALL_WIDTH = 60
MEDIUM_HEIGHT = 2_000
MEDIUM_MIN_WIDTH = 1_000_000
MAX_MARGIN = 10_000
MAX_EXTRA = 100
SAW_DIVISOR = 100
OFFSET_DIVISOR = 4

MODE_SMALL = 1
MODE_PASSABLE = 2
MODE_ASCENDING = 3
MODE_DESCENDING = 4
MODE_SHORT = 5
MODE_FULL = 6
MODE_TALL = 7
MODE_RANDOM = 8
MODE_SAWTOOTH = 9
MODE_MAX_ANSWER = 10
MODE_TOO_WIDE = 11


def arbitrary_rows(rng, height, width):
    rows = []
    for _ in range(height):
        left = rng.randint(1, width - 2)
        right = rng.randint(1, width - left - 1)
        rows.append((left, right))
    return rows


def passable_rows(rng, height, width, breadth):
    margin = rng.randint(1, MAX_MARGIN)
    extra = rng.randint(0, MAX_EXTRA)
    total = width - breadth - 2 * margin - extra
    middle = total // 2
    rows = []
    for index in range(height):
        if index < 2:
            shift = margin if index == 0 else -margin
        else:
            shift = rng.randint(-margin, margin)
        left = middle + shift
        rows.append((left, total - left))
    return rows


def make_case(mode, rng):
    if mode == MODE_SMALL:
        height = rng.randint(1, SMALL_HEIGHT)
        width = rng.randint(MIN_WIDTH, SMALL_WIDTH)
        tall = rng.choice((1, height, height + 1, MAX_SIDE, rng.randint(1, height)))
        breadth = rng.choice((2, width, MAX_SIDE, rng.randint(2, width + 1)))
        rows = arbitrary_rows(rng, height, width)
    elif mode == MODE_PASSABLE:
        height = rng.randint(2, MEDIUM_HEIGHT)
        width = rng.randint(MEDIUM_MIN_WIDTH, MAX_SIDE)
        tall = rng.randint(1, height)
        breadth = rng.randint(2, width // 2)
        rows = passable_rows(rng, height, width, breadth)
    elif mode in (MODE_ASCENDING, MODE_DESCENDING):
        height, width = MAX_HEIGHT, MAX_SIDE
        tall = height // 2
        offset = rng.randint(0, width // OFFSET_DIVISOR)
        breadth = width - offset - height - 1 - tall
        rows = [(offset + index + 1, height - index) for index in range(height)]
        if mode == MODE_DESCENDING:
            rows.reverse()
    elif mode in (MODE_SHORT, MODE_FULL, MODE_TALL):
        height, width = MAX_HEIGHT, MAX_SIDE
        tall = {MODE_SHORT: 1, MODE_FULL: height, MODE_TALL: MAX_SIDE}[mode]
        breadth = rng.randint(2, width // OFFSET_DIVISOR)
        rows = passable_rows(rng, height, width, breadth)
        if mode == MODE_SHORT:
            rows = [rows[index % 2] for index in range(height)]
    elif mode in (MODE_RANDOM, MODE_TOO_WIDE):
        height, width = MAX_HEIGHT, MAX_SIDE
        tall = rng.randint(1, height)
        breadth = MAX_SIDE if mode == MODE_TOO_WIDE else rng.randint(2, MAX_SIDE)
        rows = arbitrary_rows(rng, height, width)
    elif mode == MODE_SAWTOOTH:
        height, width = MAX_HEIGHT, MAX_SIDE
        tall = height // SAW_DIVISOR
        period = 2 * tall + 1
        offset = rng.randrange(period)
        breadth = width - 2 * period
        rows = []
        for index in range(height):
            step = (index + offset) % period
            rows.append((step + 1, period - step))
    elif mode == MODE_MAX_ANSWER:
        height, width = MAX_HEIGHT, MAX_SIDE
        tall, breadth = MAX_SIDE, 2
        rows = [(1, 1)] * height
    else:
        raise ValueError("unknown mode")
    return height, width, tall, breadth, rows


def main():
    mode, seed = map(int, sys.argv[1:])
    height, width, tall, breadth, rows = make_case(mode, random.Random(seed))
    lines = [f"{height} {width}", f"{tall} {breadth}"]
    lines.extend(f"{left} {right}" for left, right in rows)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
