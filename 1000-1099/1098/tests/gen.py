"""A random question: a seed, its size in characters, the longest line and
the last character to leave (0 any, 1 a question mark, 2 a space)."""

import random
import sys

STEP = 1999
TEXT = "abcdefghijklmnopqrstuvwxyz ABCDEFGHIJ,.!?-"
FORCED = {1: "?", 2: " "}


def main():
    seed, size, width, last = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    chars = [rng.choice(TEXT) for _ in range(size)]
    if last in FORCED:
        survivor = 0
        for m in range(2, size + 1):
            survivor = (survivor + STEP) % m
        chars[survivor] = FORCED[last]
    lines, pos = [], 0
    while pos < size:
        n = rng.randint(1, width)
        lines.append("".join(chars[pos : pos + n]))
        pos += n
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
