"""Random code words, each changed at most once; a seed, the word length and
the word count."""

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
    seed, n, count = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    lines = [str(n)]
    for _ in range(count):
        lines.append(distort(rng, "".join(map(str, code_word(rng, n)))))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
