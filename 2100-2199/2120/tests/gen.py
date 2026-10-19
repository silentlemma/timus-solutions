import random
import sys


MAX_VERTICES = 1_000_000
SMALL_MAX = 8
MEDIUM_MAX = 1_000
FRACTION_UNKNOWN_COUNT = 999_983
HALF = 2
UNKNOWN = -1


def random_degrees(size, rng):
    degrees = [1] * size
    for _ in range(size - 2):
        degrees[rng.randrange(size)] += 1
    return degrees


def hide_degrees(degrees, rng):
    for index in range(len(degrees)):
        if rng.randrange(HALF) == 0:
            degrees[index] = UNKNOWN
    return degrees


def fractional_case(rng, high):
    size = MAX_VERTICES
    unknown_count = FRACTION_UNKNOWN_COUNT
    fixed_count = size - unknown_count
    coefficient = size * (size - 2) % unknown_count
    remainder = unknown_count - 1 if high else 1
    wanted_sum = remainder * pow(coefficient, -1, unknown_count) % unknown_count
    total_sum = size * (size + 1) // 2
    fixed_sum = (total_sum - wanted_sum) % unknown_count
    start = rng.randrange(size // HALF)
    while True:
        labels = list(range(start + 1, start + fixed_count))
        last = (fixed_sum - sum(labels)) % unknown_count
        if last == 0:
            last = unknown_count
        if last not in labels:
            break
        start += 1
    degrees = [UNKNOWN] * size
    for label in labels + [last]:
        degrees[label - 1] = 1
    return degrees


def generate(mode, rng):
    if mode in ("small", "small_fixed", "small_sparse"):
        size = rng.randint(2, SMALL_MAX)
        degrees = random_degrees(size, rng)
        if mode == "small":
            return hide_degrees(degrees, rng)
        if mode == "small_sparse":
            unknown_count = rng.randint(1, min(2, size))
            for index in rng.sample(range(size), unknown_count):
                degrees[index] = UNKNOWN
        return degrees
    if mode == "medium":
        size = rng.randint(2, MEDIUM_MAX)
        return hide_degrees(random_degrees(size, rng), rng)
    if mode in ("fraction_low", "fraction_high"):
        return fractional_case(rng, mode == "fraction_high")

    size = MAX_VERTICES
    if mode == "unknown":
        return [UNKNOWN] * size
    if mode == "path":
        return [1] + [2] * (size - 2) + [1]
    if mode in ("star_first", "star_last"):
        degrees = [1] * size
        center = 0 if mode == "star_first" else size - 1
        degrees[center] = size - 1
        return degrees
    if mode == "one_unknown":
        degrees = [1] + [2] * (size - 2) + [1]
        degrees[rng.randrange(size)] = UNKNOWN
        return degrees
    if mode == "large_random":
        return hide_degrees(random_degrees(size, rng), rng)
    if mode == "large_hub":
        degrees = hide_degrees([1] * size, rng)
        degrees[rng.randrange(size)] = size - 1
        return degrees
    raise ValueError("unknown mode: " + mode)


def main():
    mode, seed = sys.argv[1:]
    degrees = generate(mode, random.Random(int(seed)))
    sys.stdout.write(str(len(degrees)) + "\n")
    sys.stdout.write(" ".join(map(str, degrees)) + "\n")


if __name__ == "__main__":
    main()
