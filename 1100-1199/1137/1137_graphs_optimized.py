import sys
from array import array
from itertools import chain

MAX_STOP = 1000
MAX_SEGMENTS = 20_000
OUTPUT_CHUNK = 256


def main():
    tokens = map(int, chain.from_iterable(map(bytes.split, sys.stdin.buffer)))
    routes = next(tokens)
    if not routes:
        print(0)
        return

    first = array("H", [0]) * (MAX_STOP + 1)
    successor = array("H", [0]) * (MAX_SEGMENTS + 1)
    destination = array("H", [0]) * (MAX_SEGMENTS + 1)
    start = edges = 0
    for _ in range(routes):
        count = next(tokens)
        origin = next(tokens)
        if not start:
            start = origin
        for _ in range(count):
            stop = next(tokens)
            edges += 1
            successor[edges] = first[origin]
            destination[edges] = stop
            first[origin] = edges
            origin = stop

    # The walk's stack and the finished circuit grow toward each other.
    route = array("H", [0]) * (edges + 1)
    route[0] = start
    depth, done = 1, edges + 1
    while depth:
        stop = route[depth - 1]
        edge = first[stop]
        if edge:
            first[stop] = successor[edge]
            route[depth] = destination[edge]
            depth += 1
        else:
            depth -= 1
            done -= 1
            route[done] = stop

    if done:
        print(0)
        return
    output = sys.stdout.write
    output(str(edges))
    for offset in range(0, edges + 1, OUTPUT_CHUNK):
        output(" " + " ".join(map(str, route[offset : offset + OUTPUT_CHUNK])))
    output("\n")


main()
