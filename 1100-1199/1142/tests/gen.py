"""Generate queries followed by -1: SEED MODE COUNT.

Modes:
  random: COUNT independent uniformly random queries from 2 to 10.
  runs: COUNT queries in constant runs of 32 to 256 values (the final run
    may be shorter), with different values in adjacent runs.
"""

import random
import sys


def main():
    seed, mode, count = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    if count < 1:
        raise SystemExit("COUNT must be positive")
    rng = random.Random(seed)
    if mode == "random":
        queries = [rng.randint(2, 10) for _ in range(count)]
    elif mode == "runs":
        queries = []
        previous = None
        while len(queries) < count:
            value = rng.choice([n for n in range(2, 11) if n != previous])
            length = min(rng.randint(32, 256), count - len(queries))
            queries.extend([value] * length)
            previous = value
    else:
        raise SystemExit("unknown mode: " + mode)
    sys.stdout.buffer.write(("\n".join(map(str, queries)) + "\n-1\n").encode("ascii"))


if __name__ == "__main__":
    main()
