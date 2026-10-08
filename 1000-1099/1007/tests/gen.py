"""Deterministic input modes:

SEED N COUNT: random code words, each changed at most once (original mode).
prefix N COUNT: even N; alternate sparse and dense words with an opposite
leading bit inserted, forcing a repair at the first position on every word.
"""

import random
import sys

DIGITS = "01"


def code_word(rng, n):
    """A random word whose positions of ones (from 1) sum to 0 modulo n + 1."""
    while True:
        bits = [0] + [rng.randint(0, 1) for _ in range(n - 1)]
        rest = sum(i + 1 for i, b in enumerate(bits) if b) % (n + 1)
        need = (n + 1 - rest) % (n + 1)
        if need == 0:
            return bits
        if bits[need - 1] == 0:
            bits[need - 1] = 1
            return bits
        if bits[rest - 1] == 1:
            bits[rest - 1] = 0
            return bits


def distort(rng, word):
    kind = rng.randint(0, 3)
    zeros = [i for i, c in enumerate(word) if c == "0"]
    if kind == 1 and zeros:
        i = rng.choice(zeros)
        return word[:i] + "1" + word[i + 1 :]
    if kind == 2:
        i = rng.randrange(len(word))
        return word[:i] + word[i + 1 :]
    if kind == 3:
        i = rng.randint(0, len(word))
        return word[:i] + rng.choice(DIGITS) + word[i:]
    return word


def main():
    if sys.argv[1] == "prefix":
        n, count = map(int, sys.argv[2:4])
        assert 4 <= n <= 1000 and n % 2 == 0
        assert 1 <= count <= 2001
        # Both words have weight divisible by n + 1 when n is even.
        sparse = "1" + "0" * (n - 2) + "1"
        dense = "0" + "1" * (n - 2) + "0"
        words = ("0" + sparse, "1" + dense)
        print("\n".join([str(n)] + [words[i % 2] for i in range(count)]))
        return
    seed, n, count = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    lines = [str(n)]
    for _ in range(count):
        lines.append(distort(rng, "".join(map(str, code_word(rng, n)))))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
