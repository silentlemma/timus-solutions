"""Generate from seed and mode: 1 small random, 2 maximal random,
3 maximal dense with long waits, 4 priority boundaries, 5 landing chains,
6 sparse maximum lists, 7 asymmetric maximum lists."""

import random
import sys

SECONDS_PER_MINUTE = 60
SECONDS_PER_HOUR = SECONDS_PER_MINUTE * SECONDS_PER_MINUTE
FIRST_HOUR = 6
LAST_HOUR = 10
FIRST_TIME = FIRST_HOUR * SECONDS_PER_HOUR
LAST_TIME = LAST_HOUR * SECONDS_PER_HOUR
MIN_INTERVAL = 30
MAX_INTERVAL = 500
INTERVAL_COUNT = 4
ASYMMETRIC_INTERVAL = 50
BOUNDARY_VARIANTS = 3
MAX_COUNT = 50
SMALL_COUNT = 6
SMALL_SPAN = 300
SMALL_MODE = 1
RANDOM_MODE = 2
DENSE_MODE = 3
BOUNDARY_MODE = 4
CHAIN_MODE = 5
SPARSE_MODE = 6
ASYMMETRIC_MODE = 7


def generate(seed, mode):
    rng = random.Random(seed)
    same_take = rng.randint(MIN_INTERVAL, MAX_INTERVAL)
    same_land = rng.randint(MIN_INTERVAL, MAX_INTERVAL)
    minimum_cross = max(same_take, same_land)
    intervals = (
        same_take,
        rng.randint(minimum_cross, MAX_INTERVAL),
        rng.randint(minimum_cross, MAX_INTERVAL),
        same_land,
    )
    if mode == SMALL_MODE:
        n, m = rng.randint(1, SMALL_COUNT), rng.randint(1, SMALL_COUNT)
        departures = sorted(rng.sample(range(FIRST_TIME, FIRST_TIME + SMALL_SPAN), n))
        landings = sorted(rng.sample(range(FIRST_TIME, FIRST_TIME + SMALL_SPAN), m))
    elif mode == DENSE_MODE:
        intervals = (MAX_INTERVAL,) * INTERVAL_COUNT
        departures = list(range(LAST_TIME - MAX_COUNT + 1, LAST_TIME + 1))
        landings = departures.copy()
    elif mode == BOUNDARY_MODE:
        intervals = (MIN_INTERVAL, MAX_INTERVAL, MAX_INTERVAL, MIN_INTERVAL)
        departures = [FIRST_TIME, FIRST_TIME + MIN_INTERVAL]
        landings = [FIRST_TIME + MIN_INTERVAL + seed % BOUNDARY_VARIANTS - 1]
    elif mode == CHAIN_MODE:
        intervals = (MIN_INTERVAL, MAX_INTERVAL, MAX_INTERVAL, MIN_INTERVAL)
        departures = [FIRST_TIME, FIRST_TIME + 1]
        landings = [FIRST_TIME + 1] + sorted(
            rng.sample(range(FIRST_TIME + 2, FIRST_TIME + SMALL_SPAN), SMALL_COUNT - 1)
        )
    else:
        if mode == SPARSE_MODE:
            intervals = (MIN_INTERVAL,) * INTERVAL_COUNT
        elif mode == ASYMMETRIC_MODE:
            intervals = (
                MIN_INTERVAL,
                MAX_INTERVAL,
                MAX_INTERVAL - 1,
                ASYMMETRIC_INTERVAL,
            )
        departures = sorted(rng.sample(range(FIRST_TIME, LAST_TIME + 1), MAX_COUNT))
        landings = sorted(rng.sample(range(FIRST_TIME, LAST_TIME + 1), MAX_COUNT))
    return intervals, departures, landings


def format_time(seconds):
    hour, remainder = divmod(seconds, SECONDS_PER_HOUR)
    minute, second = divmod(remainder, SECONDS_PER_MINUTE)
    return f"{hour:02d}:{minute:02d}:{second:02d}"


def render(intervals, departures, landings):
    lines = [" ".join(map(str, intervals)), str(len(departures))]
    lines.extend(map(format_time, departures))
    lines.append(str(len(landings)))
    lines.extend(map(format_time, landings))
    return "\n".join(lines) + "\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(SMALL_MODE, ASYMMETRIC_MODE + 1):
        raise ValueError("mode must be from 1 to 7")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
