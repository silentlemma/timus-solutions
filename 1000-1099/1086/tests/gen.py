"""Arguments: seed, query count, largest n, order.

Orders: 0 = uniform random indices from 1 to the largest n;
1 = every n descending to 1 (ignores the count);
2 = random indices among the last 1000 allowed indices (or all if fewer);
3 = repeated ascending cycles from 1 to the largest n until count queries.
"""

import random
import sys

RANDOM, ALL, TAIL, CYCLE = 0, 1, 2, 3


def main():
    seed, k, top, order = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if order == ALL:
        queries = list(range(top, 0, -1))
    elif order == TAIL:
        queries = [rng.randint(max(1, top - 999), top) for _ in range(k)]
    elif order == CYCLE:
        queries = [i % top + 1 for i in range(k)]
    else:
        queries = [rng.randint(1, top) for _ in range(k)]
    sys.stdout.write("\n".join(map(str, [len(queries)] + queries)) + "\n")


if __name__ == "__main__":
    main()
