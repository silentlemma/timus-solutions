"""Checker: every input edge must occur in exactly one adjacent pair."""

import sys

TRIPLE_SIZE = 3
ARGUMENT_COUNT = 3
IMPOSSIBLE = -1


class Bad(Exception):
    pass


def find(parent, vertex):
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex


def has_odd_component(edges, largest):
    parent = list(range(largest + 1))
    size = [1] * (largest + 1)
    for a, b in edges:
        a = find(parent, a)
        b = find(parent, b)
        if a != b:
            if size[a] < size[b]:
                a, b = b, a
            parent[b] = a
            size[a] += size[b]
    odd = set()
    for a, _ in edges:
        root = find(parent, a)
        if root in odd:
            odd.remove(root)
        else:
            odd.add(root)
    return bool(odd)


def check(source, expected, output):
    with open(source, encoding="utf-8") as stream:
        data = list(map(int, stream.read().split()))
    edges = set()
    for index in range(0, len(data), 2):
        a, b = data[index : index + 2]
        edges.add((min(a, b), max(a, b)))
    impossible = has_odd_component(edges, max(data))
    with open(output, encoding="utf-8") as stream:
        try:
            answer = list(map(int, stream.read().split()))
        except ValueError as error:
            raise Bad("output contains a noninteger token") from error
    if not answer:
        raise Bad("empty output")
    if answer[0] == IMPOSSIBLE:
        if len(answer) != 1:
            raise Bad("unexpected tokens after -1")
        if not impossible:
            raise Bad("a decomposition exists")
        return
    pair_count = len(edges) // 2
    if answer[0] != pair_count:
        raise Bad("incorrect number of adjacent pairs")
    if len(answer) != 1 + TRIPLE_SIZE * pair_count:
        raise Bad("incorrect number of output tokens")
    for index in range(1, len(answer), TRIPLE_SIZE):
        a, b, c = answer[index : index + TRIPLE_SIZE]
        for first, second in ((a, b), (b, c)):
            edge = (min(first, second), max(first, second))
            if edge not in edges:
                raise Bad("an edge is absent from the input or used more than once")
            edges.remove(edge)
    if edges:
        raise Bad("some input edges are unused")


def main():
    try:
        if len(sys.argv) != ARGUMENT_COUNT + 1:
            raise Bad("expected input, expected-output, and actual-output paths")
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
