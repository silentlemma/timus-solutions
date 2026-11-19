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


BASE = 10
FIXED = 153
CUBES = tuple(digit * digit * digit for digit in range(BASE))
tokens = map(int, words())
count = next(tokens)
answer = bytearray()
for _ in range(count):
    steps, gap, distance = next(tokens) - 1, next(tokens), next(tokens)
    # A fixed point makes all remaining iterations unnecessary.
    while steps and gap != FIXED:
        following, remaining = 0, gap
        while remaining:
            remaining, digit = divmod(remaining, BASE)
            following += CUBES[digit]
        steps -= 1
        if following == gap:
            break
        gap = following
    answer.extend(str(gap - distance).encode() + b"\n")
    if len(answer) >= READ_CHUNK:
        stdout.buffer.write(answer)
        answer.clear()
stdout.buffer.write(answer)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
