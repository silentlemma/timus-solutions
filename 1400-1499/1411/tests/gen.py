"""Generate grid dimensions: random SEED [MAX_SIDE] samples both sides uniformly.

MAX_SIDE defaults to 50 and must be between 1 and 50.
"""

import random
import sys


def main():
    if len(sys.argv) not in (3, 4) or sys.argv[1] != "random":
        raise SystemExit("usage: gen.py random SEED [MAX_SIDE]")
    seed = int(sys.argv[2])
    limit = int(sys.argv[3]) if len(sys.argv) == 4 else 50
    if not 1 <= limit <= 50:
        raise SystemExit("MAX_SIDE must be between 1 and 50")
    rng = random.Random(seed)
    print(rng.randint(1, limit), rng.randint(1, limit))


if __name__ == "__main__":
    main()
