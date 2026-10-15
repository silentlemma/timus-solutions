"""One test from a seed and a mode: mode 1 a random word of up to 50
letters over a few letters, mode 2 50 letters over the whole alphabet,
mode 3 one letter repeated, mode 4 a shuffled 49-letter word with
counts 17, 16, 16 over three randomly chosen letters."""

import random
import string
import sys

LONGEST = 50
FEW = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 4:
        letters = rng.sample(string.ascii_lowercase, FEW)
        word = list(letters[0] * 17 + letters[1] * 16 + letters[2] * 16)
        rng.shuffle(word)
        print("".join(word))
        return
    if mode == 1:
        letters = string.ascii_lowercase[:FEW]
        size = rng.randint(1, LONGEST)
    else:
        letters = string.ascii_lowercase
        size = LONGEST
    if mode == 3:
        letters = rng.choice(letters)
    print("".join(rng.choice(letters) for _ in range(size)))


main()
