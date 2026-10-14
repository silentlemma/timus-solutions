"""One test from a seed and a mode: mode 1 takes 50 random letters, mode 2
50 letters from a small alphabet, mode 3 a few letters, mode 4 50 letters
cycling through the alphabet, mode 5 letters far apart, like a and z."""

import random
import string
import sys

LONGEST = 50
FEW = 6


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 3 else LONGEST
    if mode == 2:
        letters = rng.sample(string.ascii_lowercase, rng.randint(2, 5))
    elif mode == 5:
        letters = "aznm"
    else:
        letters = string.ascii_lowercase
    if mode == 4:
        start, step = rng.randrange(len(letters)), rng.randint(1, 3)
        text = "".join(letters[(start + i * step) % len(letters)] for i in range(n))
    else:
        text = "".join(rng.choice(letters) for _ in range(n))
    print(text)


main()
