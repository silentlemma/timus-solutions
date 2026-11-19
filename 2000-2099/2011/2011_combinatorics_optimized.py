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


ALPHABET = 3
TARGET = 6
tokens = map(int, words())
count = next(tokens)
counts = [0] * ALPHABET
ways = 1
for length in range(1, count + 1):
    value = next(tokens) - 1
    counts[value] += 1
    ways = ways * length // counts[value]
    if ways >= TARGET:
        break
print("Yes" if ways >= TARGET else "No")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
