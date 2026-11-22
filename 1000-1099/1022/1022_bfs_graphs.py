import os
from sys import stdout

import sys


def main():
    tokens = map(int, sys.stdin.buffer.read().split())
    count = next(tokens)
    children = [[] for _ in range(count)]
    indegree = [0] * count
    for vertex in range(count):
        child = next(tokens)
        while child:
            child -= 1
            children[vertex].append(child)
            indegree[child] += 1
            child = next(tokens)
    ready = [i for i, degree in enumerate(indegree) if degree == 0]
    for vertex in ready:
        for child in children[vertex]:
            indegree[child] -= 1
            if indegree[child] == 0:
                ready.append(child)
    stdout.write(" ".join(str(vertex + 1) for vertex in ready) + "\n")


main()

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
