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


TOP = 30
tokens = map(int, words())
count = next(tokens)
frequencies = [0] * (TOP + 1)
for _ in range(count):
    frequencies[next(tokens)] += 1
pairs = left = 0
for value in range(1, TOP + 1):
    matched = min(left, frequencies[value])
    pairs += matched
    left = frequencies[value] - matched
print(count - pairs)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
