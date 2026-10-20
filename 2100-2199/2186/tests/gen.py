import math
import random
import sys

MODE_SMALL = 1
MODE_MEDIUM = 2
MODE_MAX_BROAD = 3
MODE_MAX_CLUSTER = 4
MODE_MAX_SHOTS = 5
MODE_TANGENT = 6
MODE_MAX_TANGENT_PAIRS = 7
ARGUMENT_COUNT = 3
SMALL_GUNS = 24
SMALL_QUERIES = 40
MEDIUM_GUNS = 300
MEDIUM_QUERIES = 500
MAX_SIZE = 100000
MAX_SHOTS = 10
COORD_LIMIT = 10**9
PROB_SCALE = 10**5
PROB_DIGITS = 5
RANDOM_COORD = 200
TARGET_NEAR = 1000
TARGET_FAR = 2000
RANDOM_RADIUS = 500
SIDE_COUNT = 4
CLUSTER_AXIS = 10**6
WIDE_RADIUS = 7 * 10**8
NARROW_RADIUS = 10**8
TANGENT_AXIS = 4 * 10**8
TANGENT_HEIGHT = 3 * 10**8
TANGENT_RADIUS = 6 * 10**8
TANGENT_GUNS = 40
PAIR_BASE = 1000
PAIR_START = 10 * PAIR_BASE
PAIR_SCALE = 25
PAIR_COSINE = 7
PAIR_SINE = 24
IMPORTANT_PROBS = (0, 1, PROB_SCALE // 2, PROB_SCALE - 1, PROB_SCALE)


def random_guns(rng, count):
    guns = []
    used = set()
    while len(guns) < count:
        x = rng.randint(-RANDOM_COORD, RANDOM_COORD)
        y = rng.randint(-RANDOM_COORD, RANDOM_COORD)
        divisor = math.gcd(x, y)
        if divisor == 0:
            continue
        direction = (x // divisor, y // divisor)
        if direction not in used:
            used.add(direction)
            guns.append((x, y))
    return guns


def broad_guns(count):
    side = count // SIDE_COUNT
    guns = []
    for index in range(side):
        offset = 2 * index - side
        guns.extend(((side, offset), (-offset, side), (-side, -offset), (offset, -side)))
    return guns


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == MODE_SMALL or mode == MODE_MEDIUM:
        max_guns = SMALL_GUNS if mode == MODE_SMALL else MEDIUM_GUNS
        queries = SMALL_QUERIES if mode == MODE_SMALL else MEDIUM_QUERIES
        count = rng.randint(1, max_guns)
        guns = random_guns(rng, count)
        a = rng.randint(TARGET_NEAR, TARGET_FAR) * rng.choice((-1, 1))
        b = rng.randint(-TARGET_FAR, TARGET_FAR)
        target = (a, b, rng.randint(1, RANDOM_RADIUS))
        shots = rng.randint(1, MAX_SHOTS)
    elif mode == MODE_MAX_BROAD:
        count = queries = MAX_SIZE
        guns = broad_guns(count)
        target = (COORD_LIMIT, 0, WIDE_RADIUS)
        shots = rng.randint(1, MAX_SHOTS)
    elif mode == MODE_MAX_CLUSTER or mode == MODE_MAX_SHOTS:
        count = queries = MAX_SIZE
        guns = [(CLUSTER_AXIS, index - count // 2) for index in range(count)]
        target = (-COORD_LIMIT, 0, NARROW_RADIUS)
        shots = MAX_SHOTS if mode == MODE_MAX_SHOTS else 1
    elif mode == MODE_TANGENT:
        count = rng.randint(2, TANGENT_GUNS)
        queries = SMALL_QUERIES
        guns = [(TANGENT_AXIS, TANGENT_HEIGHT + index - count // 2) for index in range(count)]
        target = (COORD_LIMIT, 0, TANGENT_RADIUS)
        shots = rng.randint(1, MAX_SHOTS)
    elif mode == MODE_MAX_TANGENT_PAIRS:
        count = queries = MAX_SIZE
        guns = []
        for value in range(PAIR_START, PAIR_START + count // 2):
            guns.append((PAIR_SCALE * value, PAIR_SCALE * PAIR_BASE))
            guns.append(
                (
                    PAIR_COSINE * value - PAIR_SINE * PAIR_BASE,
                    PAIR_SINE * value + PAIR_COSINE * PAIR_BASE,
                )
            )
        target = (COORD_LIMIT, 0, TANGENT_RADIUS)
        shots = 1
    else:
        raise ValueError("unknown mode")

    # Every generated gun ends before it can reach the target circle.
    rng.shuffle(guns)
    probabilities = list(IMPORTANT_PROBS)
    if mode == MODE_MAX_SHOTS:
        probabilities.extend(range(PROB_SCALE - MAX_SHOTS, PROB_SCALE + 1))
    probabilities.extend(rng.randint(0, PROB_SCALE) for _ in range(queries - len(probabilities)))
    rng.shuffle(probabilities)
    lines = [f"{count} {shots} {queries}"]
    lines.extend(f"{x} {y}" for x, y in guns)
    lines.append(" ".join(map(str, target)))
    lines.extend(
        f"{value // PROB_SCALE}.{value % PROB_SCALE:0{PROB_DIGITS}d}" for value in probabilities
    )
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    sys.stdout.write(generate(int(sys.argv[1]), int(sys.argv[2])))


if __name__ == "__main__":
    main()
