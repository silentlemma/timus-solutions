import random
import sys


MAX_VERTICES = 10**5
MAX_EDGES = 2 * MAX_VERTICES
MAX_CUPS = MAX_VERTICES
MAX_VALUE = 10**9
SMALL_VERTICES = 24
SMALL_CUPS = 12
SMALL_VALUE = 40
MEDIUM_VERTICES = 80
MEDIUM_CUPS = 40
MEDIUM_VALUE = 120
ODD_VERTICES = 60
TRIANGLE_SIZE = 3
DENSE_CORE = 10**3
ARGUMENT_COUNT = 3


def edge(first, second):
    return (first, second) if first < second else (second, first)


def random_graph(rng, count, edge_count, bipartite=False, odd=False):
    edges = set()
    if bipartite:
        edges.update((vertex, vertex + 1) for vertex in range(1, count))
        left = list(range(1, count + 1, 2))
        right = list(range(2, count + 1, 2))
        while len(edges) < edge_count:
            edges.add(edge(rng.choice(left), rng.choice(right)))
    else:
        vertices = list(range(1, count + 1))
        rng.shuffle(vertices)
        for index in range(1, count):
            edges.add(edge(vertices[index], vertices[rng.randrange(index)]))
        if odd:
            edges.update(((1, 2), (1, TRIANGLE_SIZE), (2, TRIANGLE_SIZE)))
        while len(edges) < edge_count:
            first = rng.randint(1, count)
            second = rng.randint(1, count)
            if first != second:
                edges.add(edge(first, second))
    return sorted(edges)


def random_values(rng, count, limit):
    pattern = rng.choice(("mixed", "unit", "two", "even", "odd", "low", "equal"))
    low_limit = min(10, limit)
    if pattern == "unit":
        return [1] * count
    if pattern == "two":
        return [2] * count
    if pattern == "even":
        return [2 * rng.randint(1, low_limit // 2) for _ in range(count)]
    if pattern == "odd":
        return [2 * rng.randrange((low_limit + 1) // 2) + 1 for _ in range(count)]
    if pattern == "low":
        return [rng.randint(1, low_limit) for _ in range(count)]
    if pattern == "equal":
        return [rng.randint(1, limit)] * count
    return [rng.randint(1, limit) for _ in range(count)]


def small_case(rng, mode):
    limit = SMALL_VERTICES if mode == "random" else MEDIUM_VERTICES
    lower = TRIANGLE_SIZE if mode in ("odd", "small_tail") else 2
    if mode == "odd":
        limit = ODD_VERTICES
    count = rng.randint(lower, limit)
    cup_limit = SMALL_CUPS if mode in ("random", "odd") else MEDIUM_CUPS
    value_limit = SMALL_VALUE if mode in ("random", "odd") else MEDIUM_VALUE
    cup_count = rng.randint(1, 2 if rng.randrange(2) == 0 else cup_limit)
    if mode in ("small_path", "small_tail"):
        edges = [(vertex, vertex + 1) for vertex in range(1, count)]
        if mode == "small_tail":
            edges.append((count - 2, count))
        return count, edges, random_values(rng, cup_count, 10)
    edge_limit = count * (count - 1) // 2
    if mode == "tree":
        edge_count = count - 1
    elif mode == "bipartite":
        edge_limit = (count // 2) * ((count + 1) // 2)
        edge_count = rng.randint(count - 1, edge_limit)
    else:
        edge_count = rng.randint(count - 1, edge_limit)
    edges = random_graph(rng, count, edge_count, mode == "bipartite", mode == "odd")
    values = random_values(rng, cup_count, value_limit)
    return count, edges, values


def large_case(rng, mode):
    count = MAX_VERTICES
    edges = [(vertex, vertex + 1) for vertex in range(1, count)]
    values = [1] * MAX_CUPS
    if mode == "even":
        values = [2] * MAX_CUPS
    elif mode == "lollipop":
        edges.append((count - 2, count))
    elif mode == "star":
        edges = [(1, vertex) for vertex in range(2, count + 1)]
        values = [MAX_VALUE - rng.randrange(2) for _ in range(MAX_CUPS)]
    elif mode == "max_bipartite":
        edges = random_graph(rng, count, MAX_EDGES, bipartite=True)
        values = [MAX_VALUE] * MAX_CUPS
    elif mode == "max_random":
        edges = random_graph(rng, count, MAX_EDGES)
        values = [rng.randint(1, MAX_VALUE) for _ in range(MAX_CUPS)]
        values[0] = MAX_VALUE
    elif mode == "max_tail":
        unique = set(edges)
        first_core = count - DENSE_CORE + 1
        while len(unique) < MAX_EDGES:
            first = rng.randint(first_core, count)
            second = rng.randint(first_core, count)
            if first != second:
                unique.add(edge(first, second))
        edges = sorted(unique)
    return count, edges, values


def main():
    small_modes = ("random", "tree", "bipartite", "odd", "small_path", "small_tail")
    large_modes = (
        "path",
        "even",
        "lollipop",
        "star",
        "max_bipartite",
        "max_random",
        "max_tail",
    )
    if len(sys.argv) != ARGUMENT_COUNT or sys.argv[1] not in small_modes + large_modes:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    if mode in small_modes:
        count, edges, values = small_case(rng, mode)
    else:
        count, edges, values = large_case(rng, mode)
    output = [f"{count} {len(edges)} {len(values)}"]
    output.extend(f"{first} {second}" for first, second in edges)
    output.append(" ".join(map(str, values)))
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
