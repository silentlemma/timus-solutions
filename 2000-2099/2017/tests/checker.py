"""Check any smallest nonempty group whose testimonies and complement are consistent."""

from pathlib import Path
import re
import sys


def read_case(text):
    tokens = iter(text.split())
    n = int(next(tokens))
    locations, seen = [], []
    for _ in range(n):
        locations.append(next(tokens))
        seen.append([int(next(tokens)) - 1 for _ in range(int(next(tokens)))])
    if next(tokens, None) is not None:
        raise ValueError("extra input")
    return locations, seen


def minimum_size(locations, seen):
    n = len(locations)
    statements = [set(row) | {i} for i, row in enumerate(seen)]
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if locations[i] != locations[j] and not statements[i].isdisjoint(statements[j]):
                graph[i].append(j)
                graph[j].append(i)
    colors = [-1] * n
    total = 0
    for root in range(n):
        if colors[root] >= 0:
            continue
        colors[root] = 0
        counts = [0, 0]
        stack = [root]
        while stack:
            vertex = stack.pop()
            counts[colors[vertex]] += 1
            for target in graph[vertex]:
                if colors[target] < 0:
                    colors[target] = colors[vertex] ^ 1
                    stack.append(target)
                elif colors[target] == colors[vertex]:
                    raise ValueError("no consistent partition")
        total += min(counts)
    return max(1, total)


def validate(text, locations, seen, minimum=None):
    tokens = text.split()
    if not tokens or any(re.fullmatch(r"[0-9]+", token) is None for token in tokens):
        return False
    count, *ids = map(int, tokens)
    n = len(locations)
    if not 1 <= count <= n or len(ids) != count or len(set(ids)) != count:
        return False
    if any(not 1 <= person <= n for person in ids):
        return False
    chosen = {person - 1 for person in ids}
    assignments = [{}, {}]
    for witness, location in enumerate(locations):
        known = assignments[witness in chosen]
        for person in [witness] + seen[witness]:
            if person in known and known[person] != location:
                return False
            known[person] = location
    return count == (minimum_size(locations, seen) if minimum is None else minimum)


if __name__ == "__main__":
    try:
        data = read_case(Path(sys.argv[1]).read_text())
        passed = validate(Path(sys.argv[3]).read_text(), *data)
    except (OSError, ValueError, IndexError, StopIteration):
        passed = False
    if not passed:
        print("Expected a smallest nonempty group, with consistent testimonies on both sides.")
    raise SystemExit(0 if passed else 1)
