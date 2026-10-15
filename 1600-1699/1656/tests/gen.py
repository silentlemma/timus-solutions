"""One test from a seed and a mode: n x n heights, mode 1 any odd size
with heights over the whole range, mode 2 the largest square with only a
few distinct heights, mode 3 all heights distinct."""

import random
import sys

LOW, HIGH = 170, 200


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.choice([3, 5, 7, 9]) if mode != 2 else 9
    if mode == 2:
        pool = rng.sample(range(LOW, HIGH + 1), 3)
        heights = [rng.choice(pool) for _ in range(n * n)]
    elif mode == 3:
        n = 5  # 25 distinct heights fit into 170..200
        heights = rng.sample(range(LOW, HIGH + 1), n * n)
    else:
        heights = [rng.randint(LOW, HIGH) for _ in range(n * n)]
    print(n)
    print("\n".join(map(str, heights)))


main()
