"""Random numbers that contain 1, 2, 3 and 4: a seed, how many and the
longest length; some have many zeros."""

import random
import sys

LONGEST = 20
BASE = "1234"


def main():
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
