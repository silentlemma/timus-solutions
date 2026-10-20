import random
import sys


MAX_SIDE = 1000
MAX_STAMPS = 100000
MAX_REPAINTED = 100
SMALL_SIDE = 10
SMALL_STAMPS = 200
SPARSE_BLACK = MAX_REPAINTED - 1
TILE_SIDE = 10


def emit(height, width, threshold, stamp, positions):
    output = sys.stdout
    output.write(f"{height} {width} {threshold}\n")
    output.write(f"{len(stamp)} {len(stamp[0])}\n")
    output.write("\n".join(stamp) + "\n")
    output.write(f"{len(positions)}\n")
    output.write("".join(f"{row} {column}\n" for row, column in positions))


def small(rng):
    height = rng.randint(1, SMALL_SIDE)
    width = rng.randint(1, SMALL_SIDE)
    stamp_height = rng.randint(1, height)
    stamp_width = rng.randint(1, width)
    threshold = rng.randint(1, MAX_REPAINTED)
    density = rng.randint(0, SMALL_SIDE)
    stamp = [
        "".join("#" if rng.randrange(SMALL_SIDE) < density else "." for _ in range(stamp_width))
        for _ in range(stamp_height)
    ]
    positions = [
        (rng.randint(1, height - stamp_height + 1), rng.randint(1, width - stamp_width + 1))
        for _ in range(rng.randint(1, SMALL_STAMPS))
    ]
    emit(height, width, threshold, stamp, positions)


def transparent(rng):
    stamp = ["." * MAX_SIDE] * MAX_SIDE
    emit(MAX_SIDE, MAX_SIDE, 1, stamp, [(1, 1)] * MAX_STAMPS)


def dense(rng):
    stamp = ["#" * MAX_SIDE] * MAX_SIDE
    emit(MAX_SIDE, MAX_SIDE, MAX_REPAINTED, stamp, [(1, 1)] * MAX_STAMPS)


def sparse(rng):
    cells = rng.sample(range(MAX_SIDE * MAX_SIDE), SPARSE_BLACK)
    stamp = [bytearray(b"." * MAX_SIDE) for _ in range(MAX_SIDE)]
    for cell in cells:
        stamp[cell // MAX_SIDE][cell % MAX_SIDE] = ord("#")
    rows = [row.decode() for row in stamp]
    emit(MAX_SIDE, MAX_SIDE, MAX_REPAINTED, rows, [(1, 1)] * MAX_STAMPS)


def single(rng):
    cells = rng.sample(range(MAX_SIDE * MAX_SIDE), MAX_STAMPS)
    positions = [(cell // MAX_SIDE + 1, cell % MAX_SIDE + 1) for cell in cells]
    emit(MAX_SIDE, MAX_SIDE, 1, ["#"], positions)


def tiles(rng):
    positions = [
        (row + 1, column + 1)
        for row in range(0, MAX_SIDE, TILE_SIDE)
        for column in range(0, MAX_SIDE, TILE_SIDE)
    ]
    rng.shuffle(positions)
    positions.extend([positions[0]] * (MAX_STAMPS - len(positions)))
    stamp = ["#" * TILE_SIDE] * TILE_SIDE
    emit(MAX_SIDE, MAX_SIDE, MAX_REPAINTED, stamp, positions)


def cover(rng):
    positions = [
        (row + 1, column + 1)
        for row in range(MAX_SIDE)
        for column in range(0, MAX_SIDE, TILE_SIDE)
    ]
    rng.shuffle(positions)
    emit(MAX_SIDE, MAX_SIDE, 1, ["#" * TILE_SIDE], positions)


def repeated(rng, late):
    row = rng.randint(1, MAX_SIDE)
    column = rng.randint(1, MAX_SIDE - SPARSE_BLACK)
    positions = [(row, column)] * MAX_STAMPS
    if late:
        positions[-2:] = [(row, column + 1)] * 2
    emit(MAX_SIDE, MAX_SIDE, MAX_REPAINTED, ["#" * SPARSE_BLACK], positions)


def threshold(rng):
    width = rng.randint(1, MAX_REPAINTED)
    height = rng.randint(1, SMALL_SIDE)
    threshold = rng.choice([1, width, min(MAX_REPAINTED, width + 1), MAX_REPAINTED])
    positions = [(rng.randint(1, height), 1) for _ in range(SMALL_STAMPS)]
    emit(height, width, threshold, ["#" * width], positions)


def main():
    mode, seed = sys.argv[1:]
    rng = random.Random(int(seed))
    generators = {
        "small": small,
        "transparent": transparent,
        "dense": dense,
        "sparse": sparse,
        "single": single,
        "tiles": tiles,
        "cover": cover,
        "threshold": threshold,
    }
    if mode == "long":
        repeated(rng, False)
    elif mode == "late":
        repeated(rng, True)
    else:
        generators[mode](rng)


if __name__ == "__main__":
    main()
