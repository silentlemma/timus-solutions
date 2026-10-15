"""One test from a seed and a mode: mode 1 a short word, mode 2 a long
random word, mode 3 a long word with many borders (a short pattern
repeated), mode 4 a long word over one letter or all 26."""

import random
import sys

LONGEST = 30000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 26)
    letters = [chr(ord("a") + i) for i in range(n)]
    if mode == 1:
        word = "".join(rng.choice(letters) for _ in range(rng.randint(1, 10)))
    elif mode == 2:
        word = "".join(rng.choice(letters) for _ in range(LONGEST))
    elif mode == 3:
        piece = "".join(rng.choice(letters) for _ in range(rng.randint(1, 5)))
        word = (piece * LONGEST)[:rng.randint(LONGEST // 2, LONGEST)]
    else:
        n = rng.choice((1, 26))
        word = ("a" if n == 1 else "z") * LONGEST
    print(n)
    print(word)


main()
