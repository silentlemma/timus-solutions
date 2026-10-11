"""A number of things: a seed and a number of digits."""

import random
import sys


def main():
    seed, digits = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    sys.stdout.write(
        str(rng.randint(1, 9)) + "".join(str(rng.randint(0, 9)) for _ in range(digits - 1)) + "\n"
    )


if __name__ == "__main__":
    main()
