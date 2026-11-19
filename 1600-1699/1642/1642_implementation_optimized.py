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
count, exit_at = next(tokens), next(tokens)
left = right = None
for _ in range(count):
    wall = next(tokens)
    if wall < 0 and (left is None or wall > left):
        left = wall
    elif wall > 0 and (right is None or wall < right):
        right = wall
if (left is not None and exit_at < left) or (right is not None and exit_at > right):
    print("Impossible")
elif exit_at > 0:
    print(exit_at, exit_at - 2 * left)
else:
    print(2 * right - exit_at, -exit_at)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
