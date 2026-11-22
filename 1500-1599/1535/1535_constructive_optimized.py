import os
from itertools import chain
from sys import stdout

BATCH_SIZE = 512


def cheap(n):
    pairs = (n - 1) // 2
    yield 1
    yield n
    for step in range(1, pairs + 1):
        yield step + 1 if step % 2 else n - step
    middle = (n // 2) | 1
    if n % 2 == 0 and middle != 1:
        yield middle
    for step in range(pairs, 1, -1):
        yield step if step % 2 else n - step + 1


def write_route(values):
    batch = []
    first = True
    for value in values:
        batch.append(str(value))
        if len(batch) == BATCH_SIZE:
            stdout.write(("" if first else " ") + " ".join(batch))
            first = False
            batch.clear()
    if batch:
        stdout.write(("" if first else " ") + " ".join(batch))
    stdout.write("\n")


count = int(open(0, "rb", buffering=0).read())
# Convert and write bounded groups of cities instead of encoding each number separately.
write_route(cheap(count))
write_route(chain(range(1, count + 1, 2), range(count - count % 2, 1, -2)))
stdout.flush()
os._exit(0)
