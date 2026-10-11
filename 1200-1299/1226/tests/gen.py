"""Random printable text: a seed, the number of lines and the longest
line."""

import random
import string
import sys

SYMBOLS = string.ascii_letters * 4 + string.digits + string.punctuation + " " * 10


def main():
    seed, lines, longest = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    out = [
        "".join(rng.choice(SYMBOLS) for _ in range(rng.randint(0, longest))) for _ in range(lines)
    ]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
