"""Check the permutation, Hamiltonian adjacency, and optimal prime-column count."""

from math import isqrt
from pathlib import Path
import sys

SMALL_ODD_SIDE = 3


def prime_table(limit):
    return [
        value >= 2 and all(value % divisor for divisor in range(2, isqrt(value) + 1))
        for value in range(limit + 1)
    ]


def optimum(n):
    if n == 1:
        return 0
    if n == SMALL_ODD_SIDE:
        return 2
    return (n + 1) // 2 + 1


def validate(n, tokens, prime=None):
    if len(tokens) != n * n:
        raise ValueError("Wrong number of cells")
    values = [int(token) for token in tokens]
    positions = [-1] * (n * n + 1)
    for cell, value in enumerate(values):
        if not 1 <= value <= n * n or positions[value] != -1:
            raise ValueError("Labels must be a permutation")
        positions[value] = cell
    for label in range(2, n * n + 1):
        first, second = positions[label - 1], positions[label]
        distance = abs(first // n - second // n) + abs(first % n - second % n)
        if distance != 1:
            raise ValueError("Consecutive labels must share a side")
    prime = prime_table(n * n) if prime is None else prime
    columns = [0] * n
    for cell, value in enumerate(values):
        columns[cell % n] += prime[value]
    if max(columns) != optimum(n):
        raise ValueError("Prime-column count is not optimal")
    return columns


def main():
    try:
        n = int(Path(sys.argv[1]).read_text())
        validate(n, Path(sys.argv[3]).read_text().split())
    except (ValueError, OSError) as error:
        print(error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
