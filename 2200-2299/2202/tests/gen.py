import random
import sys


MAX_PAIRS = 100_000
MAX_COORD = 100_000_000
SIDE_COUNT = 4
SMALL_PAIRS = 32
SMALL_SIDE = 100
MIN_SIDE = 4

SMALL_BOUNDARY = 1
SMALL_MIXED = 2
MAX_NESTED = 3
MAX_ADJACENT = 4
MAX_CROSSING = 5
MAX_BIPARTITE = 6
MAX_PATH = 7
MAX_RANDOM = 8
MAX_FREE = 9
MAX_MIXED_BAD = 10


def boundary_point(position, width, height):
    if position < width:
        return position, 0
    position -= width
    if position < height:
        return width, position
    position -= height
    if position < width:
        return width - position, height
    position -= width
    return 0, height - position


def chord_pairs(word, width, height):
    perimeter = 2 * (width + height)
    first = {}
    pairs = []
    for index, label in enumerate(word):
        point = boundary_point(index * perimeter // len(word), width, height)
        if label in first:
            pairs.append((first.pop(label), point))
        else:
            first[label] = point
    return pairs


def shuffle_pairs(pairs, rng):
    rng.shuffle(pairs)
    return [(right, left) if rng.randrange(2) else (left, right) for left, right in pairs]


def free_pairs(count, rng, offset=0):
    pairs = []
    for index in range(count):
        left_id = offset + 2 * index + 1
        right_id = left_id + 1
        kind = rng.randrange(SIDE_COUNT)
        if kind == 0:
            pair = ((left_id, left_id), (right_id, right_id))
        elif kind == 1:
            pair = ((-left_id, -left_id), (-right_id, -right_id))
        elif kind == 2:
            pair = ((left_id, left_id), (right_id, 0))
        else:
            pair = ((-left_id, -left_id), (right_id, 0))
        pairs.append(pair)
    return pairs


def small_boundary(rng):
    count = rng.randint(1, SMALL_PAIRS)
    word = list(range(count)) * 2
    rng.shuffle(word)
    pairs = chord_pairs(word, MAX_COORD, MAX_COORD)
    count_free = rng.randrange(SMALL_PAIRS)
    pairs.extend(free_pairs(count_free, rng, offset=SMALL_PAIRS * 2))
    return MAX_COORD, MAX_COORD, pairs


def small_mixed(rng):
    width = rng.randint(MIN_SIDE, SMALL_SIDE)
    height = rng.randint(MIN_SIDE, SMALL_SIDE)
    count = rng.randint(1, SMALL_PAIRS)
    seen = set()

    def point():
        while True:
            kind = rng.randrange(SIDE_COUNT)
            if kind == 0:
                result = (rng.randrange(1, width), rng.randrange(1, height))
            elif kind == 1:
                result = boundary_point(rng.randrange(2 * (width + height)), width, height)
            else:
                result = (
                    rng.randint(-SMALL_SIDE, 2 * SMALL_SIDE),
                    rng.randint(-SMALL_SIDE, 2 * SMALL_SIDE),
                )
                if 0 <= result[0] <= width and 0 <= result[1] <= height:
                    continue
            if result not in seen:
                seen.add(result)
                return result

    return width, height, [(point(), point()) for _ in range(count)]


def large_chords(mode, rng):
    count = MAX_PAIRS
    labels = list(range(count))
    if mode == MAX_NESTED:
        word = labels + labels[::-1]
    elif mode == MAX_ADJACENT:
        word = [label for label in labels for _ in range(2)]
    elif mode == MAX_CROSSING:
        word = labels * 2
    elif mode == MAX_BIPARTITE:
        middle = count // 2
        first = labels[:middle]
        second = labels[middle:]
        word = first + second + first[::-1] + second[::-1]
    elif mode == MAX_PATH:
        word = [0]
        for label in range(1, count):
            word.extend((label, label - 1))
        word.append(count - 1)
    else:
        word = labels * 2
        rng.shuffle(word)
    return MAX_COORD, MAX_COORD, chord_pairs(word, MAX_COORD, MAX_COORD)


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == SMALL_BOUNDARY:
        width, height, pairs = small_boundary(rng)
    elif mode == SMALL_MIXED:
        width, height, pairs = small_mixed(rng)
    elif MAX_NESTED <= mode <= MAX_RANDOM:
        width, height, pairs = large_chords(mode, rng)
    elif mode in (MAX_FREE, MAX_MIXED_BAD):
        width = height = MAX_COORD
        pairs = free_pairs(MAX_PAIRS, rng)
        if mode == MAX_MIXED_BAD:
            pairs[-1] = ((MAX_COORD - 1, MAX_COORD - 1), (-MAX_COORD, MAX_COORD))
    else:
        raise ValueError("unknown mode")
    pairs = shuffle_pairs(pairs, rng)
    lines = [f"{len(pairs)} {width} {height}"]
    lines.extend(f"{left[0]} {left[1]} {right[0]} {right[1]}" for left, right in pairs)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
