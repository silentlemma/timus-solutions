"""Validate a spanning tree and compare its price width to a validated expected tree."""

from pathlib import Path
import sys

MAX_VERTICES = 50000
MAX_WEIGHT = 10**9
EDGE_FIELDS = 3
HEADER_FIELDS = 2


def parse(data):
    fields = list(map(int, data.split()))
    n, m = fields[:HEADER_FIELDS]
    if not (2 <= n <= MAX_VERTICES and n - 1 <= m <= MAX_VERTICES):
        raise ValueError("invalid graph size")
    if len(fields) != HEADER_FIELDS + EDGE_FIELDS * m:
        raise ValueError("wrong number of road fields")
    rows = []
    for at in range(HEADER_FIELDS, len(fields), EDGE_FIELDS):
        u, v, weight = fields[at : at + EDGE_FIELDS]
        if not (1 <= u <= n and 1 <= v <= n and u != v and 1 <= weight <= MAX_WEIGHT):
            raise ValueError("invalid road")
        rows.append((u - 1, v - 1, weight))
    return n, rows


def score(n, rows, data):
    chosen = list(map(int, data.split()))
    if len(chosen) != n - 1 or len(set(chosen)) != n - 1:
        raise ValueError("need n-1 distinct road IDs")
    parent = list(range(n))
    size = [1] * n

    def root(vertex):
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    prices = []
    for identifier in chosen:
        if not 1 <= identifier <= len(rows):
            raise ValueError("road ID out of range")
        first, second, weight = rows[identifier - 1]
        first, second = root(first), root(second)
        if first == second:
            raise ValueError("selected roads contain a cycle")
        if size[first] < size[second]:
            first, second = second, first
        parent[second] = first
        size[first] += size[second]
        prices.append(weight)
    if size[root(0)] != n:
        raise ValueError("selected roads are disconnected")
    return max(prices) - min(prices)


def check(data, expected, actual):
    n, rows = parse(data)
    if score(n, rows, actual) != score(n, rows, expected):
        raise ValueError("price width differs from the validated optimum")
    return True


if __name__ == "__main__":
    try:
        check(*(Path(name).read_bytes() for name in sys.argv[1:]))
    except (ValueError, IndexError, TypeError) as error:
        print(error)
        raise SystemExit(1)
