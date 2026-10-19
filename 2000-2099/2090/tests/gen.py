import random
import sys


LIMIT = 10**6
SMALL_LIMIT = 2 * 10
MODE_SMALL = 1
MODE_RANDOM = 2
MODE_MAXIMAL = 3
MODE_CLEARANCE = 4
MODE_BOUNDARY = 5
MODE_OFFSET = 6
MODE_SKEW = 7
MODE_TINY = 8
ARGUMENT_COUNT = 2
PHASE_COUNT = 4
FIELD_COUNT = 8


def random_case(rng, limit):
    speed = rng.randint(1, limit)
    distance = rng.randint(1, limit)
    green_first = rng.randint(1, limit)
    yellow_first = rng.randint(1, limit)
    green_second = rng.randint(1, limit)
    yellow_second = rng.randint(1, limit)
    width_first = rng.randint(1, min(limit, speed * yellow_first))
    width_second = rng.randint(1, min(limit, speed * yellow_second))
    return (
        speed,
        distance,
        width_first,
        width_second,
        green_first,
        yellow_first,
        green_second,
        yellow_second,
    )


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL:
        return random_case(rng, SMALL_LIMIT)
    if mode == MODE_RANDOM:
        return random_case(rng, LIMIT)
    if mode == MODE_MAXIMAL:
        if seed == 0:
            return (LIMIT,) * FIELD_COUNT
        return (
            LIMIT,
            LIMIT,
            rng.randint(1, LIMIT),
            rng.randint(1, LIMIT),
            LIMIT,
            LIMIT,
            LIMIT,
            LIMIT,
        )
    if mode == MODE_CLEARANCE:
        speed = rng.choice((1, 10, LIMIT, rng.randint(1, LIMIT)))
        yellow_first = rng.randint(1, LIMIT // speed)
        yellow_second = rng.randint(1, LIMIT // speed)
        return (
            speed,
            rng.randint(1, LIMIT),
            speed * yellow_first,
            speed * yellow_second,
            rng.randint(1, LIMIT),
            yellow_first,
            rng.randint(1, LIMIT),
            yellow_second,
        )
    if mode == MODE_BOUNDARY:
        speed = rng.randint(1, LIMIT // 2)
        green_first = rng.randint(1, (LIMIT - 1) // speed)
        width_second = max(1, speed * green_first + rng.choice((-1, 0, 1)))
        yellow_first = rng.randint(1, LIMIT)
        minimum_yellow = (width_second + speed - 1) // speed
        return (
            speed,
            rng.randint(1, LIMIT),
            rng.randint(1, min(LIMIT, speed * yellow_first)),
            width_second,
            green_first,
            yellow_first,
            rng.randint(1, LIMIT),
            rng.randint(minimum_yellow, LIMIT),
        )
    if mode == MODE_OFFSET:
        speed = rng.randint(1, 10)
        yellow_first = rng.randint(1, 10)
        yellow_second = rng.randint(1, 10)
        return (
            speed,
            rng.randint(LIMIT // 2, LIMIT),
            rng.randint(1, speed * yellow_first),
            rng.randint(1, speed * yellow_second),
            rng.randint(1, 10),
            yellow_first,
            rng.randint(1, 10),
            yellow_second,
        )
    if mode == MODE_SKEW:
        phases = [rng.randint(1, 10) for _ in range(PHASE_COUNT)]
        phases[rng.randrange(len(phases))] = LIMIT
        green_first, yellow_first, green_second, yellow_second = phases
        speed = rng.choice((1, 10, LIMIT))
        return (
            speed,
            rng.randint(1, LIMIT),
            rng.randint(1, min(LIMIT, speed * yellow_first)),
            rng.randint(1, min(LIMIT, speed * yellow_second)),
            green_first,
            yellow_first,
            green_second,
            yellow_second,
        )
    if mode == MODE_TINY:
        phases = [rng.randint(LIMIT // 2, LIMIT) for _ in range(PHASE_COUNT)]
        return (LIMIT, rng.randint(1, LIMIT), LIMIT, rng.randint(1, 10), *phases)
    raise ValueError("unknown generator mode")


def main():
    arguments = sys.argv[1:]
    if len(arguments) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = map(int, arguments)
    case = generate(mode, seed)
    speed, distance, width_first, width_second, *phases = case
    print(speed)
    print(distance, width_first, width_second)
    print(*phases)


if __name__ == "__main__":
    main()
