import random
import sys


MAX_SIZE = 100000
MAX_BASE = 1000000
MAX_TIME = 1000000000
SMALL_VERTICES = 12
SMALL_EDGES = 24
SMALL_CLEANINGS = 40
MEDIUM_MIN = 100
MEDIUM_MAX = 500
MEDIUM_EDGE_FACTOR = 4
MEDIUM_CLEANINGS = 2000
SMALL_GAP = 30
SMALL_DURATION = 20
MEDIUM_GAP = 10000
MEDIUM_DURATION = 1000
HEAP_BRANCHES = MAX_SIZE // 2
TRIANGLE_VERTEX = 3
ARGUMENT_COUNT = 3
MODE_CHAIN = 3
MODE_HEAP = 4
MODE_REPEATED = 5
MODE_HIGH_DEGREE = 6
NEAR_CENTURY = 99
CENTURY = 100
AFTER_CENTURY = 101
BASE_CHOICES = (1, 2, 10, NEAR_CENTURY, CENTURY, AFTER_CENTURY, MAX_BASE)


def random_case(rng, medium):
    if medium:
        n = rng.randint(MEDIUM_MIN, MEDIUM_MAX)
        edge_limit = MEDIUM_EDGE_FACTOR * n
        cleaning_limit = MEDIUM_CLEANINGS
        gap_limit = MEDIUM_GAP
        duration_limit = MEDIUM_DURATION
    else:
        n = rng.randint(2, SMALL_VERTICES)
        edge_limit = min(SMALL_EDGES, n * (n - 1) // 2)
        cleaning_limit = SMALL_CLEANINGS
        gap_limit = SMALL_GAP
        duration_limit = SMALL_DURATION
    m = rng.randint(n - 1, edge_limit)
    pairs = set()
    roads = []
    for vertex in range(2, n + 1):
        other = rng.randrange(1, vertex)
        pairs.add((other, vertex))
        base = rng.choice(BASE_CHOICES) if not medium else rng.randint(1, MAX_BASE)
        roads.append((other, vertex, base))
    while len(roads) < m:
        first, second = sorted(rng.sample(range(1, n + 1), 2))
        if (first, second) in pairs:
            continue
        pairs.add((first, second))
        base = rng.choice(BASE_CHOICES) if not medium else rng.randint(1, MAX_BASE)
        roads.append((first, second, base))
    k = rng.randint(1, cleaning_limit)
    finishes = [-1] * m
    cleanings = []
    for _ in range(k):
        road = rng.randrange(m)
        start = finishes[road] + rng.randint(1, gap_limit)
        finish = start + rng.randint(1, duration_limit)
        finishes[road] = finish
        cleanings.append((road + 1, start, finish))
    rng.shuffle(cleanings)
    return n, roads, cleanings


def maximal_chain(rng):
    roads = [(vertex, vertex + 1, MAX_BASE) for vertex in range(1, MAX_SIZE)]
    roads.append((1, TRIANGLE_VERTEX, MAX_BASE))
    cleanings = [(road, 0, rng.randint(1, MAX_TIME)) for road in range(1, MAX_SIZE + 1)]
    rng.shuffle(cleanings)
    return MAX_SIZE, roads, cleanings


def heap_stress(rng):
    target = HEAP_BRANCHES + 2
    roads = [(1, vertex, 1) for vertex in range(2, target)]
    roads.extend((vertex, target, MAX_BASE - (vertex - 2)) for vertex in range(2, target))
    cleanings = [(road, MAX_TIME - 1, MAX_TIME) for road in range(1, MAX_SIZE + 1)]
    rng.shuffle(cleanings)
    return target, roads, cleanings


def repeated_cleaning(rng):
    step = MAX_TIME // MAX_SIZE
    cleanings = [(1, index * step, index * step + 1) for index in range(MAX_SIZE)]
    rng.shuffle(cleanings)
    return 2, [(1, 2, MAX_BASE)], cleanings


def high_degree(rng):
    roads = [(1, vertex, 1) for vertex in range(2, MAX_SIZE)]
    roads.append((1, MAX_SIZE, MAX_BASE))
    roads.append((2, MAX_SIZE, MAX_BASE))
    cleanings = [(road, 0, 1) for road in range(1, MAX_SIZE + 1)]
    rng.shuffle(cleanings)
    return MAX_SIZE, roads, cleanings


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = int(sys.argv[1])
    rng = random.Random(int(sys.argv[2]))
    modes = {
        1: lambda: random_case(rng, False),
        2: lambda: random_case(rng, True),
        MODE_CHAIN: lambda: maximal_chain(rng),
        MODE_HEAP: lambda: heap_stress(rng),
        MODE_REPEATED: lambda: repeated_cleaning(rng),
        MODE_HIGH_DEGREE: lambda: high_degree(rng),
    }
    if mode not in modes:
        raise SystemExit("unknown mode")
    n, roads, cleanings = modes[mode]()
    output = [f"{n} {len(roads)}"]
    output.extend(f"{first} {second} {base}" for first, second, base in roads)
    output.append(str(len(cleanings)))
    output.extend(f"{road} {start} {finish}" for road, start, finish in cleanings)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
