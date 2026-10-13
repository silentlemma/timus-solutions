"""Generate an encrypted word: SEED MODE LENGTH (1 <= LENGTH <= 100).

Mode runs: random runs of 1..9 equal ciphertext letters from abcxyz,
with different letters in adjacent runs; exercises zero differences and jumps.
"""

import random
import sys


def main():
    seed, mode, length = sys.argv[1:]
    length = int(length)
    if mode != "runs" or not 1 <= length <= 100:
        raise SystemExit("usage: gen.py SEED runs LENGTH (1..100)")
    rng = random.Random(int(seed))
    word = ""
    while len(word) < length:
        choices = [letter for letter in "abcxyz" if not word or letter != word[-1]]
        word += rng.choice(choices) * rng.randint(1, 9)
    sys.stdout.buffer.write((word[:length] + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
