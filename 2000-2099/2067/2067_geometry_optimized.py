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


FIRST_AFTER_ANCHORS = 3
tokens = map(int, words())
count = next(tokens)
# A best pair is exactly the two extremes when all points are collinear.
anchor = (next(tokens), next(tokens))
second = (next(tokens), next(tokens))
dx, dy = second[0] - anchor[0], second[1] - anchor[1]
least = (anchor, 1)
greatest = (anchor, 1)
least = min(least, (second, 2))
greatest = max(greatest, (second, 2))
collinear = True
for index in range(FIRST_AFTER_ANCHORS, count + 1):
    point = (next(tokens), next(tokens))
    if dx * (point[1] - anchor[1]) != dy * (point[0] - anchor[0]):
        collinear = False
        break
    least = min(least, (point, index))
    greatest = max(greatest, (point, index))
if collinear:
    print(1)
    print(least[1], greatest[1])
else:
    print(0)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
