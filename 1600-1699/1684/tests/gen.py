"""One test from a seed and a mode: mode 1 short words over two letters,
mode 2 the longest words with the last one cut from prefixes (No),
mode 3 the same with one letter changed (mostly Yes), mode 4 periodic
words, mode 5 random long words over the whole alphabet."""

import random
import string
import sys

LONGEST = 75000


def from_prefixes(rng, word, length, longest):
    out = []
    size = 0
    while size < length:
        piece = word[:rng.randint(1, min(longest, len(word)))]
        out.append(piece)
        size += len(piece)
    return "".join(out)[:length]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        word = "".join(rng.choice("ab") for _ in range(rng.randint(1, 8)))
        last = from_prefixes(rng, word, rng.randint(1, 12), 8)
        if rng.random() < 0.5:
            last = "".join(rng.choice("ab") for _ in range(rng.randint(1, 12)))
    elif mode in (2, 3):
        word = "".join(rng.choice("abc") for _ in range(LONGEST))
        last = from_prefixes(rng, word, LONGEST, rng.choice((3, 50, 5000)))
        if mode == 3:
            i = rng.randrange(LONGEST)
            last = last[:i] + rng.choice("abc") + last[i + 1:]
    elif mode == 4:
        period = "".join(rng.choice("ab") for _ in range(rng.randint(1, 5)))
        word = (period * LONGEST)[:rng.randint(LONGEST // 2, LONGEST)]
        last = (period * LONGEST)[rng.randint(0, 4):][:LONGEST]
    else:
        word = "".join(rng.choice(string.ascii_lowercase) for _ in range(LONGEST))
        last = "".join(rng.choice(string.ascii_lowercase) for _ in range(LONGEST))
    print(word)
    print(last)


main()
