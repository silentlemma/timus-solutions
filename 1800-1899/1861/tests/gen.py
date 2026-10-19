"""A worn inscription and a name from a seed and a mode: mode 1 short
ones over two letters, 2 the longest inscription with a random name and
many "?", 3 the longest inscription of "?" with a name of one repeated
letter, 4 the longest inscription with a name with many periods, 5 the
longest inscription with copies of the name and a few letters worn
away, 6 the longest inscription with a name of the same length."""

import random
import string
import sys

MOST = 1000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    letters = string.ascii_letters
    if mode == 1:
        name = "".join(rng.choice("aB") for _ in range(rng.randint(1, 4)))
        text = "".join(rng.choice("aB??") for _ in range(rng.randint(len(name), 12)))
    elif mode == 3:
        name = rng.choice(letters) * rng.randint(1, MOST // 2)
        text = "?" * MOST
    elif mode == 4:
        block = "".join(rng.choice("ab") for _ in range(rng.randint(1, 5)))
        name = (block * 100)[:rng.randint(50, 300)]
        text = "".join(c if rng.random() < 0.2 else "?" for c in (block * MOST)[:MOST])
    elif mode == 5:
        name = "".join(rng.choice(letters) for _ in range(rng.randint(3, 20)))
        text = ""
        while len(text) < MOST:
            text += name[:rng.randint(1, len(name))] if rng.random() < 0.3 else name
        text = "".join("?" if rng.random() < 0.1 else c for c in text[:MOST])
    elif mode == 6:
        name = "".join(rng.choice(letters) for _ in range(MOST))
        text = "".join("?" if rng.random() < 0.5 else c for c in name)
    else:
        name = "".join(rng.choice("abc") for _ in range(rng.randint(1, 10)))
        text = "".join(rng.choice("abc???") for _ in range(MOST))
    print(text)
    print(name)


main()
