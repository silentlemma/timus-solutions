"""Generate bounded polylines; prefix a shape with max_ for the largest size."""

import random
import sys

LIMIT = 100000
MAX_VERTICES = 100000
SMALL_VERTICES = 12
RANDOM_VERTICES = 2000
MAX_RATIONAL_GAP = 3
RATIONAL_GAPS = tuple(range(1, MAX_RATIONAL_GAP + 1))
SHAPES = {"random", "alternating", "uneven", "rational", "collinear", "zero", "cancellation"}


def coordinates(shape, count, rng):
    if shape == "cancellation":
        return list(range(LIMIT - count + 1, LIMIT + 1))
    if shape == "rational":
        result = [-LIMIT]
        for index in range(count - 1):
            result.append(result[-1] + RATIONAL_GAPS[index % len(RATIONAL_GAPS)])
        return result
    if shape == "uneven":
        sparse = max(1, count // 10)
        dense = count - sparse
        result = list(range(-LIMIT, -LIMIT + dense))
        result.extend(sorted(rng.sample(range(-LIMIT + dense, LIMIT), sparse - 1)))
        result.append(LIMIT)
        return result
    return sorted(rng.sample(range(-LIMIT, LIMIT + 1), count))


def generate(mode, seed):
    rng = random.Random(seed)
    largest = mode.startswith("max_")
    shape = mode[len("max_") :] if largest else mode
    if shape == "small":
        count = rng.randint(2, SMALL_VERTICES)
        shape = "random"
    elif shape in SHAPES:
        count = MAX_VERTICES if largest else rng.randint(2, RANDOM_VERTICES)
    else:
        raise ValueError("unknown mode: " + mode)
    xs = coordinates(shape, count, rng)
    if shape == "zero":
        ys = [0] * count
    elif shape == "collinear":
        slope = rng.choice((-1, 0, 1))
        constant = rng.randint(-LIMIT, LIMIT) if slope == 0 else 0
        ys = [slope * x + constant for x in xs]
    elif shape in {"alternating", "cancellation"}:
        offset = rng.randint(0, 10)
        phase = rng.randrange(2)
        ys = [(-1 if (index + phase) % 2 else 1) * (LIMIT - offset) for index in range(count)]
    else:
        ys = [rng.randint(-LIMIT, LIMIT) for _ in xs]
    return [(x, y) for x, y in zip(xs, ys)]


def main():
    points = generate(sys.argv[1], int(sys.argv[2]))
    lines = [str(len(points))]
    lines.extend("%d %d" % point for point in points)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
