"""Random fees; a seed, M floors, N rooms and the largest fee."""

import random
import sys


def main():
    seed, m, n, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = ["%d %d" % (m, n)]
    for _ in range(m):
        lines.append(" ".join(str(rng.randint(1, top)) for _ in range(n)))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
