"""Check distinct in-range dates and the optimal objective from the trusted answer."""

import sys
from pathlib import Path


class Bad(Exception):
    pass


def read_pairs(path, queries, label):
    try:
        tokens = Path(path).read_text(encoding="utf-8").split()
        if len(tokens) != 2 * len(queries):
            raise Bad(label + ": expected two dates per query")
        numbers = list(map(int, tokens))
    except (ValueError, OSError) as error:
        raise Bad(label + ": cannot read integer dates") from error
    pairs = list(zip(numbers[::2], numbers[1::2]))
    for query, ((left, right), (first, second)) in enumerate(zip(queries, pairs), 1):
        if first == second or not (left <= first <= right and left <= second <= right):
            raise Bad(f"{label}: query {query}: dates must be distinct and inside the interval")
    return pairs


def check(source, expected, output):
    data = list(map(int, Path(source).read_text(encoding="utf-8").split()))
    n, q = data[:2]
    values = data[2 : n + 2]
    queries = list(zip(data[n + 2 :: 2], data[n + 2 + 1 :: 2]))
    if len(queries) != q:
        raise Bad("invalid query count in input")
    wanted = read_pairs(expected, queries, "expected output")
    got = read_pairs(output, queries, "output")
    for query, ((first, second), (best_first, best_second)) in enumerate(zip(got, wanted), 1):
        score = abs(values[first - 1] + values[second - 1])
        optimum = abs(values[best_first - 1] + values[best_second - 1])
        if score != optimum:
            raise Bad(f"query {query}: objective {score}, expected {optimum}")


def main():
    try:
        check(*sys.argv[1:])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
