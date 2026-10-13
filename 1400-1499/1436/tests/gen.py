"""Modes: random SEED picks a slanted segment on one side of the road;
narrow SEED picks a segment below the road with horizontal span one.
Both modes use coordinates in [-1000, 1000] and distinct endpoints.
"""

import random
import sys


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    if mode == "random":
        x1, x2 = rng.sample(range(-1000, 1001), 2)
        y1, y2 = rng.sample(range(1, 1001), 2)
        sign = rng.choice((-1, 1))
        y1, y2 = sign * y1, sign * y2
    elif mode == "narrow":
        x1 = rng.randint(-1000, 999)
        x2 = x1 + 1
        y1, y2 = (-y for y in rng.sample(range(1, 1001), 2))
    else:
        raise ValueError("expected: random SEED or narrow SEED")
    text = "\n".join(map(str, (x1, y1, x2, y2))) + "\n"
    sys.stdout.buffer.write(text.encode("ascii"))


if __name__ == "__main__":
    main()
