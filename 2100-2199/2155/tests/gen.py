import random
import sys


MAX_SIZE = 250
MAX_COST = 999_999
SMALL_SIZE = 8
MEDIUM_MIN = 20
MEDIUM_MAX = 60
ARGUMENT_COUNT = 3
DRONE_START = 3
WINDS = "UDLR"
DELTAS = {(-1, 0): "U", (1, 0): "D", (0, -1): "L", (0, 1): "R"}


def random_case(rng, height, width, weight_mode="random"):
    count = height * width
    person, drone = rng.sample(range(count), 2)
    if weight_mode == "unit":
        weights = [[1] * width for _ in range(height)]
    elif weight_mode == "maximum":
        weights = [[MAX_COST] * width for _ in range(height)]
    elif weight_mode == "extremes":
        weights = [[rng.choice((1, MAX_COST)) for _ in range(width)] for _ in range(height)]
    else:
        limit = 10 if weight_mode == "small" else MAX_COST
        weights = [[rng.randint(1, limit) for _ in range(width)] for _ in range(height)]
    winds = [[rng.choice(WINDS) for _ in range(width)] for _ in range(height)]
    return [height, width, person, drone, weights, winds]


def set_path(winds, path, cycle=False):
    for current, following in zip(path, path[1:]):
        row, column = current
        next_row, next_column = following
        winds[row][column] = DELTAS[(next_row - row, next_column - column)]
    row, column = path[-1]
    if cycle:
        next_row, next_column = path[0]
        winds[row][column] = DELTAS[(next_row - row, next_column - column)]
    else:
        winds[row][column] = "D"


def snake_path(height, width):
    path = []
    for row in range(height):
        columns = range(width) if row % 2 == 0 else range(width - 1, -1, -1)
        path.extend((row, column) for column in columns)
    return path


def full_cycle(height, width):
    path = [(0, column) for column in range(width)]
    for row in range(1, height):
        columns = range(width - 1, 0, -1) if row % 2 else range(1, width)
        path.extend((row, column) for column in columns)
    path.extend((row, 0) for row in range(height - 1, 0, -1))
    return path


def random_dimensions(rng, low, high):
    height, width = rng.randint(low, high), rng.randint(low, high)
    if height * width == 1:
        width = 2
    return height, width


def generate(mode, rng):
    if mode == "small":
        height, width = random_dimensions(rng, 1, SMALL_SIZE)
        weight_mode = rng.choice(("unit", "small", "random", "maximum", "extremes"))
        return random_case(rng, height, width, weight_mode)

    if mode == "medium":
        height, width = random_dimensions(rng, MEDIUM_MIN, MEDIUM_MAX)
        return random_case(rng, height, width)

    if mode in ("row", "column"):
        height, width = (1, MAX_SIZE) if mode == "row" else (MAX_SIZE, 1)
        case = random_case(rng, height, width, "extremes")
        choices = "LR" if mode == "row" else "UD"
        case[-1] = [[rng.choice(choices) for _ in range(width)] for _ in range(height)]
        return case

    if mode == "exit":
        height, width = random_dimensions(rng, 2, MEDIUM_MAX)
        case = random_case(rng, height, width, "small")
        case[-1] = [[rng.choice("RD") for _ in range(width)] for _ in range(height)]
        return case

    if mode in ("two", "four"):
        height, width = random_dimensions(rng, 2, MEDIUM_MAX)
        case = random_case(rng, height, width)
        row = rng.randrange(height - 1)
        column = rng.randrange(width - 1)
        path = [(row, column), (row, column + 1)]
        if mode == "four":
            path.extend(((row + 1, column + 1), (row + 1, column)))
        set_path(case[-1], path, True)
        drone_row, drone_column = rng.choice(path)
        case[DRONE_START] = drone_row * width + drone_column
        while case[2] == case[DRONE_START]:
            case[2] = rng.randrange(height * width)
        return case

    if mode in ("tail", "snake", "maxexit"):
        if mode == "maxexit":
            height, width = MAX_SIZE, MAX_SIZE
            weight_mode = "maximum"
        else:
            height, width = random_dimensions(rng, 2, MEDIUM_MAX)
            weight_mode = rng.choice(("unit", "small", "random", "maximum"))
        case = random_case(rng, height, width, weight_mode)
        path = snake_path(height, width)
        set_path(case[-1], path)
        if mode == "tail":
            row, column = path[-1]
            previous_row, previous_column = path[-2]
            case[-1][row][column] = DELTAS[(previous_row - row, previous_column - column)]
            case[DRONE_START] = 0
            case[2] = rng.randrange(1, height * width)
        elif mode == "maxexit":
            case[2], case[DRONE_START] = 0, 1
        return case

    if mode in ("cycle", "maxcycle"):
        height = MAX_SIZE if mode == "maxcycle" else 2 * rng.randint(1, MEDIUM_MAX // 2)
        width = MAX_SIZE if mode == "maxcycle" else rng.randint(2, MEDIUM_MAX)
        weight_mode = rng.choice(("unit", "small", "random", "maximum"))
        case = random_case(rng, height, width, weight_mode)
        set_path(case[-1], full_cycle(height, width), True)
        return case

    if mode in ("hard", "late", "extremes"):
        weight_mode = {"hard": "random", "late": "maximum", "extremes": "extremes"}[mode]
        case = random_case(rng, MAX_SIZE, MAX_SIZE, weight_mode)
        if mode != "extremes":
            path = [(MAX_SIZE - 1, MAX_SIZE - 1), (MAX_SIZE - 1, MAX_SIZE - 2)]
            set_path(case[-1], path, True)
            case[2], case[DRONE_START] = 0, MAX_SIZE * MAX_SIZE - 1
        return case

    raise ValueError("unknown generator mode: " + mode)


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode, seed = sys.argv[1:]
    height, width, person, drone, weights, winds = generate(mode, random.Random(int(seed)))
    lines = [str(height) + " " + str(width)]
    lines.append(str(person // width + 1) + " " + str(person % width + 1))
    lines.append(str(drone // width + 1) + " " + str(drone % width + 1))
    lines.extend(" ".join(map(str, row)) for row in weights)
    lines.extend("".join(row) for row in winds)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
