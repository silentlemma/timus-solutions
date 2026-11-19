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


FIELDS = 4
tokens = map(int, words())
count = next(tokens)
left, previous_low, right, previous_high = (next(tokens) for _ in range(FIELDS))
height, vertical = 1, 0
possible = True
for _ in range(count - 1):
    left, low, right, high = (next(tokens) for _ in range(FIELDS))
    first, last = max(previous_low, low) + 1, min(previous_high, high) - 1
    if first > last:
        possible = False
        break
    # Cross the common border at the nearest permitted integer height.
    following = min(max(height, first), last)
    vertical += abs(following - height)
    height = following
    previous_low, previous_high = low, high
print(right - 2 + vertical + abs(previous_high - 1 - height) if possible else -1)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
