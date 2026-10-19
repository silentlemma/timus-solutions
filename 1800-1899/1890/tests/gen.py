"""Generate from seed and mode: 1 small random, 2 maximal random tree,
3 path, 4 star, 5 successful updates, 6 equality with large sums,
7 alternating initial salaries, 8 salaries exceeding signed 32-bit range."""

import random
import sys

MAX_SIZE = 50_000
MAX_VALUE = 1_000_000_000
SMALL_SIZE = 24
SMALL_QUERIES = 100
SMALL_VALUE = 20
PATH_MODE = 3
STAR_MODE = 4
SUCCESS_MODE = 5
EQUALITY_MODE = 6
ALTERNATING_MODE = 7
OVERFLOW_MODE = 8
SMALL_MODE = 1
RANDOM_MODE = 2


def generate(seed, mode):
    rng = random.Random(seed)
    n = rng.randint(1, SMALL_SIZE) if mode == SMALL_MODE else MAX_SIZE
    q = rng.randint(1, SMALL_QUERIES) if mode == SMALL_MODE else MAX_SIZE
    parent = [0]
    for vertex in range(1, n):
        if mode == PATH_MODE:
            parent.append(vertex - 1)
        elif mode == STAR_MODE:
            parent.append(0)
        else:
            parent.append(rng.randrange(vertex))
    if mode == EQUALITY_MODE:
        salary = [MAX_VALUE] * n
    elif mode == ALTERNATING_MODE:
        salary = [MAX_VALUE * (vertex % 2) for vertex in range(n)]
    elif mode == OVERFLOW_MODE:
        salary = [MAX_VALUE] + [0] * (n - 1)
    elif mode in (PATH_MODE, STAR_MODE, SUCCESS_MODE):
        salary = [0] * n
    else:
        limit = SMALL_VALUE if mode == SMALL_MODE else MAX_VALUE
        salary = [rng.randint(0, limit) for _ in range(n)]
    current = salary.copy()
    members = [[vertex] for vertex in range(n)] if mode == SMALL_MODE else []
    if mode == SMALL_MODE:
        for vertex in range(n - 1, 0, -1):
            members[parent[vertex]].extend(members[vertex])
    queries = []
    if mode == OVERFLOW_MODE:
        queries = [
            ("department", 0, MAX_VALUE, MAX_VALUE // 2),
            ("department", 0, MAX_VALUE, MAX_VALUE),
        ]
    for _ in range(q - len(queries)):
        vertex = rng.randrange(n)
        kind = rng.choice(("employee", "department"))
        if mode == SMALL_MODE:
            affected = [vertex] if kind == "employee" else members[vertex]
            total = sum(current[member] for member in affected)
            average = total // len(affected)
            threshold = max(1, min(MAX_VALUE, average + rng.choice((-1, 0, 1, 2))))
            amount = rng.choice((1, 2, SMALL_VALUE, MAX_VALUE))
            if total < threshold * len(affected):
                for member in affected:
                    current[member] += amount
        elif mode in (PATH_MODE, STAR_MODE, SUCCESS_MODE):
            threshold, amount = MAX_VALUE, 1
            if mode != STAR_MODE:
                kind = "department"
        elif mode in (EQUALITY_MODE, OVERFLOW_MODE):
            threshold, amount = MAX_VALUE, MAX_VALUE
        else:
            threshold, amount = rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)
        queries.append((kind, vertex, threshold, amount))
    return parent, salary, queries


def render(parent, salary, queries):
    lines = [f"{len(parent)} {len(queries)} {salary[0]}"]
    lines.extend(f"{parent[vertex]} {salary[vertex]}" for vertex in range(1, len(parent)))
    lines.extend(" ".join(map(str, query)) for query in queries)
    return "\n".join(lines) + "\n"


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode not in range(SMALL_MODE, OVERFLOW_MODE + 1):
        raise ValueError("mode must be from 1 to 8")
    sys.stdout.write(render(*generate(seed, mode)))


if __name__ == "__main__":
    main()
