"""A digit string: a seed, its length, a mode and a number of digits.
Mode 0 gives random digits, mode 1 a piece of consecutive numbers of the
given length starting at a random one, mode 2 the same around a power of
ten, mode 3 one digit repeated, mode 4 a random block of the given length
repeated."""

import random
import sys

DIGITS = "0123456789"


def run_from(x, offset, n):
    out = []
    size = 0
    while size < offset + n:
        out.append(str(x))
        size += len(out[-1])
        x += 1
    return "".join(out)[offset : offset + n]


def main():
    seed, n, mode, d = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 1:
        x = rng.randrange(10 ** (d - 1), 10**d)
        a = run_from(x, rng.randrange(d), n)
    elif mode == 2:
        x = 10**d - rng.randint(1, max(1, n // d))
        a = run_from(x, rng.randrange(d), n)
    elif mode == 3:
        a = rng.choice(DIGITS) * n
    elif mode == 4:
        block = "".join(rng.choice(DIGITS) for _ in range(d))
        a = (block * n)[:n]
    else:
        a = "".join(rng.choice(DIGITS) for _ in range(n))
    sys.stdout.write(a + "\n")


if __name__ == "__main__":
    main()
