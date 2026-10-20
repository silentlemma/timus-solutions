import argparse
import random


MAX_SIZE = 1000
MAX_VALUE = 1_000_000_000
SMALL_SIZE = 10
SMALL_TOTAL = 20
WORD_BITS = 32
MODES = (
    "small",
    "random",
    "large",
    "max",
    "sparse",
    "unequal",
    "unequal_large",
    "unequal_wrap",
    "row",
    "column",
    "lower",
    "zero",
    "last",
)


def partition(total, size, rng):
    values = []
    for remaining_slots in range(size - 1, -1, -1):
        lower = max(0, total - remaining_slots * MAX_VALUE)
        upper = min(MAX_VALUE, total)
        value = rng.randint(lower, upper)
        values.append(value)
        total -= value
    rng.shuffle(values)
    return values


def balanced(n, m, rng, total=None):
    if total is None:
        total = rng.randint(0, min(n, m) * MAX_VALUE)
    return partition(total, n, rng), partition(total, m, rng)


def generate(mode, rng):
    n = rng.randint(1, MAX_SIZE)
    m = rng.randint(1, MAX_SIZE)
    if mode == "small":
        n = rng.randint(1, SMALL_SIZE)
        m = rng.randint(1, SMALL_SIZE)
        rows, columns = balanced(n, m, rng, rng.randint(0, SMALL_TOTAL))
    elif mode in ("random", "unequal"):
        rows, columns = balanced(n, m, rng)
        if mode == "unequal":
            index = rng.randrange(n)
            rows[index] += 1 if rows[index] < MAX_VALUE else -1
    elif mode in ("large", "last"):
        n = m = MAX_SIZE
        rows, columns = balanced(n, m, rng)
    elif mode in ("max", "unequal_large", "unequal_wrap"):
        n = m = MAX_SIZE
        rows = [MAX_VALUE] * n
        columns = [MAX_VALUE] * m
        if mode == "unequal_large":
            columns[rng.randrange(m)] -= 1
        elif mode == "unequal_wrap":
            remaining = 1 << WORD_BITS
            for index in range(m):
                change = min(remaining, columns[index])
                columns[index] -= change
                remaining -= change
                if remaining == 0:
                    break
            rng.shuffle(columns)
    elif mode == "sparse":
        n = m = MAX_SIZE
        total = rng.randint(0, MAX_VALUE)
        active_rows = rng.randint(1, SMALL_SIZE)
        active_columns = rng.randint(1, SMALL_SIZE)
        rows = partition(total, active_rows, rng) + [0] * (n - active_rows)
        columns = partition(total, active_columns, rng) + [0] * (m - active_columns)
        rng.shuffle(rows)
        rng.shuffle(columns)
    elif mode == "row":
        n = 1
        m = MAX_SIZE
        rows, columns = balanced(n, m, rng)
    elif mode == "column":
        n = MAX_SIZE
        m = 1
        rows, columns = balanced(n, m, rng)
    elif mode == "lower":
        n = m = 2
        row = rng.randint(MAX_VALUE // 2 + 1, MAX_VALUE)
        column = rng.randint(MAX_VALUE // 2 + 1, MAX_VALUE)
        rows = [row, MAX_VALUE - row]
        columns = [column, MAX_VALUE - column]
    else:
        n = m = MAX_SIZE
        rows = [0] * n
        columns = [0] * m
    a = rng.randrange(n)
    b = rng.randrange(m)
    if mode == "lower":
        a = b = 0
    elif mode == "last":
        a = n - 1
        b = m - 1
    elif mode == "sparse" and total > 0 and rng.randrange(2):
        a = next(index for index, value in enumerate(rows) if value)
        b = next(index for index, value in enumerate(columns) if value)
    return n, m, a + 1, b + 1, rows, columns


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("mode", choices=MODES)
    parser.add_argument("seed", type=int)
    args = parser.parse_args()
    n, m, a, b, rows, columns = generate(args.mode, random.Random(args.seed))
    print(n, m)
    print(a, b)
    print(*rows)
    print(*columns)


if __name__ == "__main__":
    main()
