"""One test from a seed and a mode: mode 1 takes 1000 random pairs of
letters, mode 2 1000 pairs over the letters a and b, mode 3 a few pairs,
mode 4 a letter that starts no pair."""

import random
import sys

LARGEST = 1000
FEW = 10
LETTERS = "abcdefghijklmnopqrstuvwxyz"


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    letters = "ab" if mode == 2 else LETTERS
    n = rng.randint(1, FEW) if mode == 3 else LARGEST
    words = ["".join(rng.choice(letters) for _ in range(2)) for _ in range(n)]
    letter = rng.choice(letters)
    if mode == 4:
        unused = [c for c in LETTERS if all(w[0] != c for w in words)]
        letter = rng.choice(unused) if unused else letter
        words = [w for w in words if w[0] != letter] or ["zz" if letter != "z" else "aa"]
    print(len(words))
    print("\n".join(words))
    print(letter)


main()
