"""Random containers: a seed, N, the largest amount and the shape (0 any
amounts, 1 amounts from two close values, 2 a multiplication table modulo
101 with rows and columns shuffled, 3 all amounts equal to the maximum,
4 only one trash type spread across all containers, 5 shuffled independent
random blocks of at most six containers and types)."""

import random
import sys

ANY, CLOSE, TABLE = 0, 1, 2
FULL, SINGLE, BLOCKS = 3, 4, 5
TABLE_MOD = 101
BLOCK_SIZE = 6


def main():
    seed, n, top, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    rows, cols = list(range(n)), list(range(n))
    rng.shuffle(rows)
    rng.shuffle(cols)
    single = rng.randrange(n) if shape == SINGLE else None
    lines = [str(n)]
    for i in range(n):
        if shape == CLOSE:
            row = [rng.choice([top - 1, top]) for _ in range(n)]
        elif shape == TABLE:
            row = [(rows[i] * cols[j]) % TABLE_MOD % (top + 1) for j in range(n)]
        elif shape == FULL:
            row = [top] * n
        elif shape == SINGLE:
            row = [rng.randint(1, top) if j == single else 0 for j in range(n)]
        elif shape == BLOCKS:
            row = [
                rng.randint(1, top) if rows[i] // BLOCK_SIZE == c // BLOCK_SIZE else 0
                for c in cols
            ]
        else:
            row = [rng.randint(0, top) for _ in range(n)]
        lines.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
