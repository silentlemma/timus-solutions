"""A random text: a seed, the length (with the final line break) and the
percentage of letters that are capital. Words, numbers, punctuation and
whitespace (spaces, tabs, line breaks) are mixed at random."""

import random
import string
import sys

PUNCTUATION = ".,;:-!?"
SPACES = "  \t\n"


def main():
    seed, length, upper_pct = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    parts = []
    size = 0
    while size < length:
        kind = rng.randrange(10)
        if kind < 5:
            part = "".join(
                rng.choice(string.ascii_uppercase)
                if rng.randrange(100) < upper_pct
                else rng.choice(string.ascii_lowercase)
                for _ in range(rng.randint(1, 8))
            )
        elif kind < 6:
            part = str(rng.randint(0, 999))
        elif kind < 8:
            part = rng.choice(PUNCTUATION)
        else:
            part = rng.choice(SPACES)
        parts.append(part)
        size += len(part)
    text = "".join(parts)[: length - 1]
    sys.stdout.write(text + "\n")


if __name__ == "__main__":
    main()
