"""Generate deterministic schedules with strictly increasing entry times."""

import random
import sys

MAX_COUNT = 100
MAX_DURATION = 100
MIN_START = 360
MAX_START = 1200
MIN_FULL_DURATION = (MAX_COUNT + 2) // 2


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == 1:
        duration = rng.randint(1, MAX_DURATION)
        start = rng.randint(MIN_START, MAX_START)
        count = rng.randint(1, min(MAX_COUNT, 2 * duration - 1))
        others = sorted(
            rng.sample(range(start - duration + 1, start + duration), count)
        )
    elif mode == 2:
        duration, start = 1, MIN_START
        others = [start]
    elif mode == 3:
        duration, start = MAX_DURATION, MAX_START
        lower, upper = start - duration + 1, start + duration - 1
        others = sorted(
            [lower, upper] + rng.sample(range(lower + 1, upper), MAX_COUNT - 2)
        )
    elif mode == 4:
        duration, start = MAX_DURATION, MIN_START
        others = [start - duration + 1, start + duration - 1]
    elif mode == 5:
        duration, start = MAX_DURATION, MAX_START
        others = list(range(start - duration + 2, start + duration, 2))
    elif mode == 6:
        duration, start = MAX_DURATION, MAX_START
        others = list(range(start - duration + 1, start + duration - 1, 2))
    elif mode == 7:
        duration, start = MIN_FULL_DURATION, MIN_START
        others = [
            time
            for time in range(start - duration + 1, start + duration)
            if time != start
        ]
    else:
        raise ValueError("unknown mode")
    return duration, start, others


def render(duration, start, others):
    return f"{len(others)} {duration} {start}\n" + " ".join(map(str, others)) + "\n"


if __name__ == "__main__":
    print(render(*generate(int(sys.argv[1]), int(sys.argv[2]))), end="")
