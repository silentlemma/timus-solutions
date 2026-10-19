"""One file from a seed and a mode, close to a megabyte for modes 2 to
6: mode 1 a short random text over a few characters, mode 2 one long
run of a single letter with an at in the middle, mode 3 random text
over two letters, a dot and an at, mode 4 short addresses a@a.a
repeated, mode 5 random printable text with lines, mode 6 a long
address made of many short dotted parts around one at."""

import random
import sys

LIMIT = 1000000
SMALL = 60
PRINTABLE = "".join(chr(c) for c in range(32, 127))


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        alphabet = rng.choice(["ab.@", "a.@ ", "abc.@\n", "a@.", "ab@..x"])
        text = "".join(rng.choice(alphabet) for _ in range(rng.randint(1, SMALL)))
    elif mode == 2:
        half = LIMIT // 2 - 1
        text = "a" * half + "@" + "a" * half
    elif mode == 3:
        text = "".join(rng.choice("aaab.@") for _ in range(LIMIT - 1))
    elif mode == 4:
        text = "a@a.a " * (LIMIT // 6)
    elif mode == 5:
        weights = [1] * len(PRINTABLE) + [20] * 3
        pool = PRINTABLE + "x.@"
        lines = []
        size = 0
        while size < LIMIT - 200:
            line = "".join(rng.choices(pool, weights, k=rng.randint(1, 120)))
            lines.append(line)
            size += len(line) + 1
        text = "\n".join(lines)
    else:
        parts = []
        size = 0
        while size < LIMIT // 2 - 10:
            part = "".join(rng.choice("ab") for _ in range(rng.randint(1, 3)))
            parts.append(part)
            size += len(part) + 1
        user = ".".join(parts)
        text = user + "@" + user
    sys.stdout.buffer.write(text.encode())


main()
