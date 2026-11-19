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


# Squared chord scales follow directly from the three shapes in the statement.
NARROWEST = (0, 16, 4, 3)
WIDEST = (0, 16, 8, 4)
tokens = map(int, words())
kind, size = next(tokens), next(tokens)
hole = WIDEST[kind] * size * size
count = next(tokens)
answer = 0
for _ in range(count):
    kind, size = next(tokens), next(tokens)
    answer += NARROWEST[kind] * size * size <= hole
print(answer)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
