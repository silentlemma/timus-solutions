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
intervals = []
for _ in range(count):
    start, end = next(tokens), next(tokens)
    intervals.append((end, start))
intervals.sort()
chosen = 0
last_end = None
for end, start in intervals:
    if last_end is None or start >= last_end:
        # Compact the chosen prefix behind the current iterator position.
        intervals[chosen] = (end, start)
        chosen += 1
        last_end = end
print(chosen)
for index in range(chosen):
    end, start = intervals[index]
    print(start, end)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
