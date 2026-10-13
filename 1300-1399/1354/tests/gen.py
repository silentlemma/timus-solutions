"""A word of up to 10 000 letters: a seed and a mode. Mode 1 gives random
letters, mode 2 a long palindrome after a short random start, mode 3 one
letter repeated, mode 4 blocks of one letter split by single others."""

import random
import sys

LIMIT = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        word = "".join(rng.choice("abAB") for _ in range(LIMIT))
    elif mode == 2:
        half = "".join(rng.choice("xyX") for _ in range(LIMIT // 2 - 10))
        start = "".join(rng.choice("xyX") for _ in range(rng.randint(1, 19)))
        word = start + half + half[::-1]
    elif mode == 3:
        word = rng.choice("aZ") * LIMIT
    else:
        block = rng.randint(50, 200)
        word = ""
        while len(word) + block + 1 <= LIMIT:
            word += "a" * block + rng.choice("bc")
    print(word)


main()
