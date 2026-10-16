"""One test from a seed and a mode: a random number and its Gray code
with some digits rubbed out; mode 1 up to 12 digits, mode 2 100 000
digits with only digits of k rubbed out, so the answer is unique,
mode 3 100 000 digits with both rubbed out at the same places, mode 4
100 000 digits with one digit of the code changed, mode 5 100 000 digits
with only the last k digit and all but the first code digit known,
mode 6 100 000 digits with a highly ambiguous prefix and a final conflict.
Modes 5 and 6 accept an optional length for small cross-checks."""

import random
import sys

FEW = 12
MOST = 100000
HALF = 0.5


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else MOST
        if not 2 <= n <= MOST:
            raise ValueError("modes 5 and 6 require 2 to 100000 digits")
        if mode == 5:
            k = "?" * (n - 1) + rng.choice("01")
            x = "?" + "".join(rng.choice("01") for _ in range(n - 1))
        else:
            k = "?" * (n - 2) + "00"
            x = "".join(rng.choice("01??") for _ in range(n - 1)) + "1"
        print(k)
        print(x)
        return
    n = rng.randint(1, FEW) if mode == 1 else MOST
    value = rng.getrandbits(n)
    k = list(format(value, "0%db" % n))
    x = list(format(value ^ (value >> 1), "0%db" % n))
    rubbed = rng.random()
    for i in range(n):
        if mode in (1, 2) and rng.random() < rubbed:
            k[i] = "?"
        if mode == 1 and rng.random() < rubbed:
            x[i] = "?"
        if mode == 3 and rng.random() < HALF:
            k[i] = x[i] = "?"
    if mode == 4:
        i = rng.randrange(n)
        x[i] = "1" if x[i] == "0" else "0"
    print("".join(k))
    print("".join(x))


main()
