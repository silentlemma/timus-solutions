import random
import sys


MAX_COUNT = 100000
MAX_DAY = 1000000000
SMALL_MAX_COUNT = 8
SMALL_DAY = 80
MEDIUM_MIN_COUNT = 20
MEDIUM_MAX_COUNT = 600
MEDIUM_DAY = 100000
EXAM_ENDPOINTS = 4
CHAIN_STEP = 3
FREE_STEP = 10
ARGUMENT_COUNT = 3
MODE_LARGE_RANDOM = 3
MODE_CHAIN = 4
MODE_FREE = 5
MODE_LONG_TRIP = 6
MODE_MANY_TRIPS = 7
MODE_FULL_RANGE = 8


def random_intervals(rng, count, endpoints, last_day):
    days = sorted(rng.sample(range(1, last_day + 1), count * endpoints))
    return [tuple(days[index : index + endpoints]) for index in range(0, len(days), endpoints)]


def random_case(rng, min_count, max_count, last_day):
    exam_count = rng.randint(min_count, max_count)
    trip_count = rng.randint(min_count, max_count)
    exams = random_intervals(rng, exam_count, EXAM_ENDPOINTS, last_day)
    trips = random_intervals(rng, trip_count, 2, last_day)
    return exams, trips


def chain_exams(offset):
    exams = []
    for index in range(MAX_COUNT):
        first = offset + CHAIN_STEP * index + 1
        second = first + 1
        exams.append((first, first, second, second))
    return exams


def generate(mode, rng):
    if mode == 1:
        return random_case(rng, 1, SMALL_MAX_COUNT, SMALL_DAY)
    if mode == 2:
        return random_case(rng, MEDIUM_MIN_COUNT, MEDIUM_MAX_COUNT, MEDIUM_DAY)
    if mode == MODE_LARGE_RANDOM:
        return random_case(rng, MAX_COUNT, MAX_COUNT, MAX_DAY)
    if mode == MODE_CHAIN:
        offset = rng.randrange(MAX_COUNT)
        exams = chain_exams(offset)
        trips = []
        for index in range(MAX_COUNT):
            left = offset + CHAIN_STEP * index + 2
            trips.append((left, left + 2))
        return exams, trips
    if mode == MODE_FREE:
        exams = []
        trips = []
        for index in range(MAX_COUNT):
            first = FREE_STEP * index + 1
            first_end = first + 1
            second = first_end + 2
            exams.append((first, first_end, second, second + 1))
            trips.append((first_end + 1, first_end + 1))
        return exams, trips
    if mode == MODE_LONG_TRIP:
        return chain_exams(rng.randrange(MAX_COUNT)), [(1, MAX_DAY)]
    if mode == MODE_MANY_TRIPS:
        split = rng.randint(1, MAX_COUNT - 1)
        exams = [(1, split, split + 1, MAX_COUNT)]
        trips = [(day, day) for day in range(1, MAX_COUNT + 1)]
        return exams, trips
    if mode == MODE_FULL_RANGE:
        exams = []
        trips = []
        parity = rng.randrange(2)
        last_index = 2 * MAX_COUNT - 1
        for index in range(MAX_COUNT):
            first = 1 + 2 * index * (MAX_DAY - 1) // last_index
            second = 1 + (2 * index + 1) * (MAX_DAY - 1) // last_index
            exams.append((first, first, second, second))
            if index % 2 == parity:
                trips.extend(((first, first), (second, second)))
        return exams, trips
    raise ValueError("mode must be from 1 to 8")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = int(sys.argv[1])
    rng = random.Random(int(sys.argv[2]))
    exams, trips = generate(mode, rng)
    lines = [f"{len(exams)} {len(trips)}"]
    lines.extend(" ".join(map(str, exam)) for exam in exams)
    lines.extend(" ".join(map(str, trip)) for trip in trips)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
