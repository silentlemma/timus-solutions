"""Check every reattachment, then compare unordered rooted tree shapes."""

import sys
from pathlib import Path

MIN_SIZE = 2
MAX_SIZE = 1000
ARGUMENT_COUNT = 4


class Bad(Exception):
    pass


def read_integers(path):
    try:
        return [int(token) for token in Path(path).read_text(encoding="utf-8").split()]
    except (OSError, UnicodeError, ValueError) as error:
        raise Bad("cannot read a sequence of integers") from error


def children_of(parents):
    n = len(parents)
    children = [[] for _ in range(n)]
    for vertex in range(1, n):
        parent = parents[vertex]
        if not 0 <= parent < n:
            raise Bad("input parent is out of range")
        children[parent].append(vertex)
        if len(children[parent]) > 2:
            raise Bad("input tree is not binary")
    order = [0]
    for vertex in order:
        order.extend(children[vertex])
        if len(order) > n:
            raise Bad("input tree contains a cycle")
    if len(order) != n:
        raise Bad("input tree is disconnected")
    return children


def shape(children, shapes):
    order = [0]
    for vertex in order:
        order.extend(children[vertex])
    identifiers = [0] * len(children)
    for vertex in reversed(order):
        key = tuple(sorted(identifiers[child] for child in children[vertex]))
        if key not in shapes:
            shapes[key] = len(shapes) + 1
        identifiers[vertex] = shapes[key]
    return identifiers[0]


def check(source, expected, output):
    data = read_integers(source)
    if not data or not MIN_SIZE <= data[0] <= MAX_SIZE:
        raise Bad("input size is out of range")
    n = data[0]
    if len(data) != 1 + 2 * (n - 1):
        raise Bad("input has the wrong number of parents")
    parents = [-1] + data[1:n]
    children = children_of(parents)
    target = children_of([-1] + data[n:])
    got = read_integers(output)
    if not got:
        raise Bad("missing operation count")
    count = got[0]
    if not 0 <= count <= n:
        raise Bad("operation count must be between zero and the number of vertices")
    if len(got) != 1 + 2 * count:
        raise Bad("wrong number of operation endpoints")
    for index in range(count):
        vertex, parent = got[1 + 2 * index : 1 + 2 * (index + 1)]
        step = index + 1
        if not 1 <= vertex < n or not 0 <= parent < n:
            raise Bad("operation %d: vertex is out of range" % step)
        ancestor = parent
        while ancestor != -1:
            if ancestor == vertex:
                raise Bad("operation %d: destination belongs to the moved subtree" % step)
            ancestor = parents[ancestor]
        old_parent = parents[vertex]
        if parent != old_parent and len(children[parent]) == 2:
            raise Bad("operation %d: destination would have more than two children" % step)
        children[old_parent].remove(vertex)
        children[parent].append(vertex)
        parents[vertex] = parent
    shapes = {}
    if shape(children, shapes) != shape(target, shapes):
        raise Bad("the final tree is not isomorphic to the target")


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        print("usage: checker.py input expected output")
        sys.exit(1)
    try:
        check(*sys.argv[1:])
    except Bad as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
