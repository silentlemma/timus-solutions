import random
import sys


MAX_N = 200000
MAX_Q = 1000000
SMALL_N = 40
MEDIUM_N = 80
SMALL_Q = 300
SHORT_SPAN = 32
OUTPUT_CHUNK = 4096
QUERY_PATTERN = 8
PATTERN_PREFIX = 3
PATTERN_SUFFIX = 4
PATTERN_SHORT = 5
MODE_RANDOM_SMALL = 1
MODE_PATH_SMALL = 2
MODE_STAR_SMALL = 3
MODE_BALANCED_SMALL = 4
MODE_BROOM_SMALL = 5
MODE_PATH_MAX = 6
MODE_STAR_MAX = 7
MODE_BALANCED_MAX = 8
MODE_RANDOM_MAX = 9
MODE_BROOM_MAX = 10
MODE_SINGLETON_MAX = 11
MODE_PATH_EMPTY = 12
MODE_BALANCED_SHORT = 13
MODE_PATH_ORDERED_MAX = 14


def make_edges(n, shape, shuffled, rng):
    labels = list(range(1, n + 1))
    if shuffled:
        rng.shuffle(labels)
    edges = []
    handle = max(1, n // 2)
    for vertex in range(1, n):
        if shape == "path":
            parent = vertex - 1
        elif shape == "star":
            parent = 0
        elif shape == "balanced":
            parent = (vertex - 1) // 2
        elif shape == "broom":
            parent = vertex - 1 if vertex < handle else handle - 1
        else:
            parent = rng.randrange(vertex)
        first, second = labels[parent], labels[vertex]
        if rng.randrange(2):
            first, second = second, first
        edges.append((first, second))
    rng.shuffle(edges)
    return edges


def make_query(n, index, style, rng):
    pattern = index % QUERY_PATTERN
    left = rng.randint(1, n)
    if style == "short":
        return left, min(n, left + rng.randrange(SHORT_SPAN))
    if pattern == 0:
        return 1, n
    if pattern == 1:
        return left, left
    if pattern == 2:
        return left, min(n, left + 1)
    if pattern == PATTERN_PREFIX:
        return 1, left
    if pattern == PATTERN_SUFFIX:
        return left, n
    if pattern == PATTERN_SHORT:
        return left, min(n, left + rng.randrange(SHORT_SPAN))
    right = rng.randint(1, n)
    return min(left, right), max(left, right)


def write_pairs(pairs):
    chunk = []
    for first, second in pairs:
        chunk.append(f"{first} {second}\n")
        if len(chunk) == OUTPUT_CHUNK:
            sys.stdout.write("".join(chunk))
            chunk.clear()
    sys.stdout.write("".join(chunk))


def main():
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    shapes = {
        MODE_RANDOM_SMALL: "random",
        MODE_PATH_SMALL: "path",
        MODE_STAR_SMALL: "star",
        MODE_BALANCED_SMALL: "balanced",
        MODE_BROOM_SMALL: "broom",
        MODE_PATH_MAX: "path",
        MODE_STAR_MAX: "star",
        MODE_BALANCED_MAX: "balanced",
        MODE_RANDOM_MAX: "random",
        MODE_BROOM_MAX: "broom",
        MODE_SINGLETON_MAX: "star",
        MODE_PATH_EMPTY: "path",
        MODE_BALANCED_SHORT: "balanced",
        MODE_PATH_ORDERED_MAX: "path",
    }
    if mode not in shapes:
        raise SystemExit("unknown mode")
    exhaustive = mode in (MODE_RANDOM_SMALL, MODE_PATH_SMALL, MODE_BALANCED_SMALL)
    if mode == MODE_RANDOM_SMALL:
        n = rng.randint(1, SMALL_N)
    elif mode <= MODE_BROOM_SMALL:
        n = rng.randint(1, MEDIUM_N)
    elif mode == MODE_SINGLETON_MAX:
        n = 1
    else:
        n = MAX_N
    if exhaustive:
        queries = [(left, right) for left in range(1, n + 1) for right in range(left, n + 1)]
        rng.shuffle(queries)
        q = len(queries)
    elif mode <= MODE_BROOM_SMALL:
        q = rng.randint(0, SMALL_Q)
    elif mode == MODE_PATH_EMPTY:
        q = 0
    else:
        q = MAX_Q
    ordered = mode in (MODE_BALANCED_SHORT, MODE_PATH_ORDERED_MAX)
    shuffled = not ordered
    edges = make_edges(n, shapes[mode], shuffled, rng)
    sys.stdout.write(f"{n}\n")
    write_pairs(edges)
    sys.stdout.write(f"{q}\n")
    if exhaustive:
        write_pairs(queries)
    else:
        style = "short" if ordered else "mixed"
        write_pairs(make_query(n, index, style, rng) for index in range(q))


if __name__ == "__main__":
    main()
