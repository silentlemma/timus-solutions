"""Random numbers: a seed, the number of digits, the base the digits are
drawn from and a target base. With a target the last digit is chosen so
that the number is divisible by the target minus one in the target base."""

import random
import sys

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def main():
    seed, length, base, target = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    digits = [rng.randrange(base) for _ in range(length)]
    if target:
        rest = sum(digits[:-1])
        digits[-1] = max(d for d in range(base) if (rest + d) % (target - 1) == 0)
    sys.stdout.write("".join(DIGITS[d] for d in digits) + "\n")


if __name__ == "__main__":
    main()
