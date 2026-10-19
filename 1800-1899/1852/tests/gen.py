"""A sequence of turns from a seed and a mode: mode 1 a few random
turns, 2 the longest random sequence, 3 the longest sequence of two
alternating faces, 4 the longest sequence of one face turned both ways,
5 a long random sequence of opposite faces only, 6 a random sequence
with long runs of one letter."""

import random
import sys

MOST = 100000
LETTERS = "UDLRFBudlrfb"


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        word = "".join(rng.choice(LETTERS) for _ in range(rng.randint(1, 12)))
    elif mode == 2:
        word = "".join(rng.choice(LETTERS) for _ in range(MOST))
    elif mode == 3:
        a, b = rng.sample(LETTERS, 2)
        word = (a + b) * (MOST // 2)
    elif mode == 4:
        face = rng.choice("UDLRFB")
        word = "".join(rng.choice((face, face.lower())) for _ in range(MOST))
    elif mode == 5:
        word = "".join(rng.choice("UDud") for _ in range(MOST - 1))
    else:
        parts, size = [], 0
        while size < MOST:
            run = rng.choice(LETTERS) * rng.randint(1, 7)
            parts.append(run)
            size += len(run)
        word = "".join(parts)[:MOST]
    print(word)


main()
