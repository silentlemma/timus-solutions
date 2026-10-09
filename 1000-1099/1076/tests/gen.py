"""Random containers: a seed, N, the largest amount and the shape (0 any
amounts, 1 amounts from two close values, 2 a multiplication table modulo
101 with rows and columns shuffled)."""

import random
import sys

ANY, CLOSE, TABLE = 0, 1, 2
TABLE_MOD = 101


def main():
    seed, n, top, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    rows, cols = list(range(n)), list(range(n))
    rng.shuffle(rows)
    rng.shuffle(cols)
    lines = [str(n)]
    for i in range(n):
        if shape == CLOSE:
            row = [rng.choice([top - 1, top]) for _ in range(n)]
        elif shape == TABLE:
            row = [(rows[i] * cols[j]) % TABLE_MOD % (top + 1) for j in range(n)]
        else:
            row = [rng.randint(0, top) for _ in range(n)]
        lines.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
