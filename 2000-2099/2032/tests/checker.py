"""Check arbitrary lattice embeddings; disprove -1 with Gaussian circle enumeration."""

from functools import lru_cache
from itertools import product
from math import isqrt
from pathlib import Path
import re
import sys

BOUND = 100_000_000
COORDINATES = 6
CACHE_SIZE = 128


def multiply(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


@lru_cache(maxsize=CACHE_SIZE)
def gaussian_circle(radius):
    """All norm-radius^2 Gaussian integers by independent prime splitting."""
    remaining = radius
    factors = []
    for candidate in range(2, isqrt(radius) + 1):
        exponent = 0
        while remaining % candidate == 0:
            remaining //= candidate
            exponent += 1
        if exponent:
            factors.append((candidate, exponent))
    if remaining > 1:
        factors.append((remaining, 1))
    scale = 1
    split = []
    for prime, exponent in factors:
        if prime == 2 or prime % 4 == 3:
            scale *= prime**exponent
        else:
            for x in range(1, isqrt(prime) + 1):
                y = isqrt(prime - x * x)
                if x * x + y * y == prime:
                    split.append(((x, y), exponent))
                    break
            else:
                raise AssertionError(("split prime representation missing", prime))
    points = {(scale, 0)}
    for factor, exponent in split:
        conjugate = factor[0], -factor[1]
        positive, negative = [(1, 0)], [(1, 0)]
        for _ in range(2 * exponent):
            positive.append(multiply(positive[-1], factor))
            negative.append(multiply(negative[-1], conjugate))
        choices = {
            multiply(positive[k], negative[2 * exponent - k]) for k in range(2 * exponent + 1)
        }
        points = {multiply(a, b) for a, b in product(points, choices)}
    all_points = {
        multiply(point, unit) for point, unit in product(points, ((1, 0), (0, 1), (-1, 0), (0, -1)))
    }
    assert all(x * x + y * y == radius * radius for x, y in all_points)
    return tuple(sorted(all_points))


def exists(sides):
    radius, length, opposite = sorted(sides)
    first = [(x, y) for x, y in gaussian_circle(radius) if x >= 0 and y >= 0]
    second = gaussian_circle(length)
    return any(
        (u - x) ** 2 + (v - y) ** 2 == opposite * opposite for x, y in first for u, v in second
    )


def validate(sides, raw):
    try:
        tokens = raw.decode("ascii").split()
    except UnicodeDecodeError:
        return False
    if tokens == ["-1"]:
        return not exists(sides)
    if len(tokens) != COORDINATES or any(re.fullmatch(r"[+-]?[0-9]+", t) is None for t in tokens):
        return False
    try:
        values = list(map(int, tokens))
    except ValueError:
        return False
    if any(abs(value) > BOUND for value in values):
        return False
    points = list(zip(values[::2], values[1::2]))
    distances = sorted(
        (points[a][0] - points[b][0]) ** 2 + (points[a][1] - points[b][1]) ** 2
        for a, b in ((0, 1), (0, 2), (1, 2))
    )
    return distances == sorted(side * side for side in sides)


def main():
    sides = list(map(int, Path(sys.argv[1]).read_text(encoding="ascii").split()))
    if not validate(sides, Path(sys.argv[3]).read_bytes()):
        print("Invalid integer embedding or false impossibility claim")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
