"""A bookcase: a seed, the niche width and height, N and a mode. Shelves
get distinct heights, random planks and pegs with the middle of the plank
between them. Mode 0 makes the tome small, mode 1 wide, mode 2 tall, so
that many shelves stand in its way. One shelf is made long enough for the
tome, so a solution always exists."""

import random
import sys


def main():
    seed, width, height, n, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    n = min(n, height - 1)
    tome_w = rng.randint(1, max(1, width // (4 if mode == 0 else 2)))
    if mode == 1:
        tome_w = rng.randint(width // 2, width)
    tome_h = rng.randint(1, max(1, height // (4 if mode != 2 else 1)))
    heights = rng.sample(range(1, height), n)
    low = min(heights)
    tome_h = min(tome_h, height - low)
    lines = ["%d %d %d %d" % (width, height, tome_w, tome_h), str(n)]
    for y in heights:
        length = rng.randint(1, width)
        if y == low:
            length = max(length, tome_w)
        left = rng.randint(0, width - length)
        x1 = rng.randint(0, length // 2)
        x2 = rng.randint((length + 1) // 2, length)
        if x1 == x2:
            if x2 < length:
                x2 += 1
            else:
                x1 -= 1
        if x1 < 0:
            # a plank of length 1 or less cannot have two pegs, make it longer
            length, x1, x2 = 2, 0, 2
            left = min(left, width - length)
        lines.append("%d %d %d %d %d" % (y, left, length, x1, x2))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
