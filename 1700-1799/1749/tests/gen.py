"""One deterministic test from a seed and a mode.

Modes: 1 short number repeated a few times; 2 random 100000-digit number;
3 a 1 followed by 99999 zeros; 4 random 100000 digits, power-of-ten modulus;
5 maximum p (100000 nines), one copy; 6 alternating 90, two copies modulo
2^29; 7 seeded zero-heavy 99999-digit number, three copies modulo 125.
Modes 2, 3 and 4 repeat up to 10^9 times.
"""

import random
import sys

DIGITS = 100000
LIMIT = 10 ** 9
SHORT = 9
FEW = 10
POWERS = 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        p = str(rng.randint(1, 10 ** rng.randint(1, SHORT)))
        k = rng.randint(1, FEW)
    elif mode == 3:
        p = "1" + "0" * (DIGITS - 1)
        k = rng.randint(1, LIMIT)
    elif mode == 5:
        p = "9" * DIGITS
        k = 1
    elif mode == 6:
        p = "90" * (DIGITS // 2)
        k = 2
    elif mode == 7:
        p = str(rng.randint(1, 9)) + "".join(
            rng.choice("000000000123456789") for _ in range(DIGITS - 2)
        )
        k = 3
    else:
        p = str(rng.randint(1, 9)) + "".join(rng.choice("0123456789") for _ in range(DIGITS - 1))
        k = rng.randint(1, LIMIT)
    if mode == 5:
        m = 999999937
    elif mode == 6:
        m = 2 ** 29
    elif mode == 7:
        m = 125
    else:
        m = 10 ** rng.randint(0, POWERS) if mode == 4 else rng.randint(1, LIMIT)
    print(p)
    print(k, m)


main()
