"""A random database and queries; a seed, N, the largest value and K."""

import random
import sys

SEPARATOR = "###"


def main():
    seed, n, top, k = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [str(n)] + [str(rng.randint(1, top)) for _ in range(n)]
    lines += [SEPARATOR, str(k)] + [str(rng.randint(1, n)) for _ in range(k)]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
