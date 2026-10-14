"""One test from a seed and a mode: a slogan of up to 1000 characters.
Mode 1 mixes words and punctuation, mode 2 is all z and !, the dearest
characters, mode 3 is short."""

import random
import string
import sys

LONGEST = 1000
SHORT = 20


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        text = "".join(rng.choice("z!") for _ in range(LONGEST))
    else:
        size = LONGEST if mode == 1 else rng.randint(1, SHORT)
        parts = []
        while sum(map(len, parts)) < size:
            word = "".join(rng.choice(string.ascii_lowercase) for _ in range(rng.randint(1, 9)))
            parts.append(word + rng.choice(["", "", ",", ".", "!"]) + " ")
        text = "".join(parts)[:size].rstrip() or "a"
    print(text)


main()
