"""A random 4-connected set of black pixels; a seed, the pixel count and the
representation to print (1: the list of pixels, 2: the neighbour description)."""

import random
import sys

MAX_COORD = 10
STEPS = ((1, 0, "R"), (0, 1, "T"), (-1, 0, "L"), (0, -1, "B"))


def shape(rng, count):
    pixels = {(rng.randint(1, MAX_COORD), rng.randint(1, MAX_COORD))}
    while len(pixels) < count:
        x, y = rng.choice(sorted(pixels))
        dx, dy, _ = rng.choice(STEPS)
        if 1 <= x + dx <= MAX_COORD and 1 <= y + dy <= MAX_COORD:
            pixels.add((x + dx, y + dy))
    return pixels


def as_list(pixels):
    return [str(len(pixels))] + ["%d %d" % p for p in sorted(pixels)]


def as_description(pixels):
    start = min(pixels)
    queue, seen, lines = [start], {start}, []
    for x, y in queue:
        line = ""
        for dx, dy, letter in STEPS:
            p = (x + dx, y + dy)
            if p in pixels and p not in seen:
                seen.add(p)
                queue.append(p)
                line += letter
        lines.append(line + ",")
    lines[-1] = lines[-1][:-1] + "."
    return ["%d %d" % start] + lines


def main():
    seed, count, representation = (int(x) for x in sys.argv[1:4])
    pixels = shape(random.Random(seed), count)
    print("\n".join(as_list(pixels) if representation == 1 else as_description(pixels)))


if __name__ == "__main__":
    main()
