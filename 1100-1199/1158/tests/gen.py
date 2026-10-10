"""Alphabet and forbidden words: a seed, N, M, P and a mode. Letters are
distinct bytes from 33 to 255, written as the Latin-1 characters with
those codes in UTF-8, as the tests are stored. Mode 0 draws random words, mode 1 builds
words from very few letters so that they overlap, mode 2 forbids single
letters among longer words, mode 3 takes the longest words allowed."""

import random
import sys

LOW, HIGH = 33, 255
LONGEST = 10


def main():
    seed, n, m, p, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    letters = "".join(map(chr, rng.sample(range(LOW, HIGH + 1), n)))
    top = min(m, LONGEST)
    words = []
    for _ in range(p):
        if mode == 1:
            pool = letters[:2]
            size = rng.randint(1, top)
        elif mode == 2:
            pool = letters
            size = 1 if rng.random() < 1 / 2 else rng.randint(1, top)
        else:
            pool = letters
            size = top if mode == 3 else rng.randint(1, top)
        words.append("".join(rng.choice(pool) for _ in range(size)))
    out = "%d %d %d\n%s\n%s" % (n, m, p, letters, "".join(w + "\n" for w in words))
    sys.stdout.buffer.write(out.encode("utf-8"))


if __name__ == "__main__":
    main()
