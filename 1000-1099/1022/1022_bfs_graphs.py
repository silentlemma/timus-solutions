import os
from sys import stdout

READ_CHUNK = 4096
SPACE = 32


def words():
    pending = b""
    while True:
        block = os.read(0, READ_CHUNK)
        if not block:
            break
        data = pending + block
        parts = data.split()
        pending = parts.pop() if data[-1] > SPACE else b""
        yield from parts
    if pending:
        yield pending


tokens = map(int, words())
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
print(*(vertex + 1 for vertex in ready))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
