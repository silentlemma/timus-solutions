"""Deterministic numbers containing 1, 2, 3 and 4.

Modes:
  SEED COUNT LONGEST: legacy random lengths, sometimes with many zeros.
  dense SEED COUNT: exactly 20 digits, with no zeros in the extra digits.
  sparse SEED COUNT: exactly 20 digits, cycling through 1 to 15 zeros.
"""

import random
import sys

LONGEST = 20
BASE = "1234"


def main():
    if sys.argv[1] in ("dense", "sparse"):
        mode = sys.argv[1]
        seed, count = (int(x) for x in sys.argv[2:4])
        rng = random.Random(seed)
        out = [str(count)]
        for index in range(count):
            zeros = 0 if mode == "dense" else 1 + index % 15
            digits = list(BASE) + ["0"] * zeros
            digits += [rng.choice("123456789") for _ in range(LONGEST - len(digits))]
            rng.shuffle(digits)
            while digits[0] == "0":
                rng.shuffle(digits)
            out.append("".join(digits))
        sys.stdout.write("\n".join(out) + "\n")
        return

    seed, count, longest = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    out = [str(count)]
    for _ in range(count):
        extra = rng.randint(0, min(longest, LONGEST) - len(BASE))
        digits = list(BASE) + [
            rng.choice("0123456789" if rng.random() < 0.7 else "0") for _ in range(extra)
        ]
        rng.shuffle(digits)
        while digits[0] == "0":
            rng.shuffle(digits)
        out.append("".join(digits))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
