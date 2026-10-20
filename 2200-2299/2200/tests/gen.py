import random
import sys

MIN_SIDE = 3
MAX_BOARDS = 50_000
MAX_COORD = 1_000_000_000
SMALL_SIDE = 7
SMALL_WIDTH = 12
SMALL_LIMIT = SMALL_WIDTH * SMALL_WIDTH
GRID_WIDTH = 250
STEP = MIN_SIDE + 1


def subdivide(count, rng):
    size = MAX_BOARDS * STEP
    boards = [(0, 0, size, size)]
    candidates = [0]
    while len(boards) < count:
        position = rng.randrange(len(candidates))
        index = candidates[position]
        candidates[position] = candidates[-1]
        candidates.pop()
        board = boards[index]
        gap = rng.randint(1, 2)
        axes = [axis for axis in (0, 1) if board[axis + 2] - board[axis] >= 2 * MIN_SIDE + gap]
        if not axes:
            continue
        axis = rng.choice(axes)
        cut = rng.randint(board[axis] + MIN_SIDE, board[axis + 2] - MIN_SIDE - gap)
        first, second = list(board), list(board)
        first[axis + 2] = cut
        second[axis] = cut + gap
        boards[index] = tuple(first)
        boards.append(tuple(second))
        candidates.extend((index, len(boards) - 1))
    return boards


def generate(mode, rng):
    if mode == "small":
        count = rng.randint(1, SMALL_LIMIT)
        shift_x = rng.randint(-SMALL_LIMIT, SMALL_LIMIT)
        shift_y = rng.randint(-SMALL_LIMIT, SMALL_LIMIT)
        boards = []
        for slot in rng.sample(range(SMALL_LIMIT), count):
            x = (slot % SMALL_WIDTH) * (SMALL_SIDE + 1) + shift_x
            y = (slot // SMALL_WIDTH) * (SMALL_SIDE + 1) + shift_y
            width = rng.choice((SMALL_SIDE, rng.randint(MIN_SIDE, SMALL_SIDE)))
            height = rng.choice((SMALL_SIDE, rng.randint(MIN_SIDE, SMALL_SIDE)))
            boards.append((x, y, x + width, y + height))
        return boards
    if mode in ("slices", "max_slices"):
        count = MAX_BOARDS if mode == "max_slices" else rng.randint(1, SMALL_LIMIT)
        return subdivide(count, rng)
    if mode == "hub":
        boards = [(0, 0, MIN_SIDE, (MAX_BOARDS - 1) * STEP)]
        for index in range(MAX_BOARDS - 1):
            x = STEP if rng.randrange(2) else -STEP
            y = index * STEP
            boards.append((x, y, x + MIN_SIDE, y + MIN_SIDE))
        return boards
    if mode not in ("chain", "grid", "disconnected", "extreme"):
        raise ValueError("unknown generator mode")
    boards = []
    spacing = MIN_SIDE + 2 if mode == "disconnected" else STEP
    for index in range(MAX_BOARDS):
        if mode == "extreme":
            half = MAX_BOARDS // 2
            x = -MAX_COORD + index * STEP
            y = -MAX_COORD
            if index >= half:
                x = MAX_COORD - (index - half + 1) * STEP
                y = MAX_COORD - MIN_SIDE
        else:
            columns = MAX_BOARDS if mode == "chain" else GRID_WIDTH
            x = (index % columns) * spacing
            y = (index // columns) * spacing
        boards.append((x, y, x + MIN_SIDE, y + MIN_SIDE))
    return boards


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    boards = generate(mode, rng)
    left, bottom, right, top = rng.choice(boards)
    x, y = left, bottom
    if mode == "small":
        x = rng.randrange(left, right)
        y = rng.randrange(bottom, top)
    rng.shuffle(boards)
    bound = max(2, max(abs(value) for board in boards for value in board))
    lines = [f"{len(boards)} {bound}", f"{x} {y}"]
    lines.extend(" ".join(map(str, board)) for board in boards)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
