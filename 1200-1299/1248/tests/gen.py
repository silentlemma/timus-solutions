"""Numbers to add: a seed, N and a mode. Each has a 19-digit mantissa.
Mode 1 spreads exponents over the whole range; mode 2 keeps them within
three of each other, so many carries meet; mode 3 adds tiny numbers to
one large one, so they only reach the digits past the 19th. Mode 4 repeats
the minimum input value. Mode 5 uses random complementary pairs whose
exact sums are powers of ten across the exponent range (N must be even)."""

import random
import sys

DIGITS = 19
LOW, HIGH = -100, 99


def number(rng, exp):
    mantissa = str(rng.randint(1, 9)) + "".join(str(rng.randint(0, 9)) for _ in range(DIGITS - 1))
    return "%s.%se%d" % (mantissa[0], mantissa[1:], exp)


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        nums = [number(rng, rng.randint(LOW, HIGH)) for _ in range(n)]
    elif mode == 2:
        base = rng.randint(LOW, HIGH - 3)
        nums = [number(rng, base + rng.randint(0, 3)) for _ in range(n)]
    elif mode == 4:
        nums = ["1.000000000000000000e-100"] * n
    elif mode == 5:
        if n % 2:
            raise ValueError("mode 5 requires an even N")
        nums = []
        for i in range(n // 2):
            exp = LOW + i % (HIGH - LOW + 1)
            part = rng.randint(10 ** (DIGITS - 1), 9 * 10 ** (DIGITS - 1))
            for coefficient in (part, 10**DIGITS - part):
                mantissa = str(coefficient)
                nums.append("%s.%se%d" % (mantissa[0], mantissa[1:], exp))
    else:
        big = rng.randint(0, HIGH)
        nums = [number(rng, big)] + [
            number(rng, big - DIGITS - rng.randint(0, 3)) for _ in range(n - 1)
        ]
    rng.shuffle(nums)
    sys.stdout.write("\n".join([str(n)] + nums) + "\n")


if __name__ == "__main__":
    main()
