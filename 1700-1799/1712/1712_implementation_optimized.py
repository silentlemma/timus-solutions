import os
from sys import stdout

SIZE = 4
rows = open(0, "rb", buffering=0).read().split()
holes = [(r, c) for r in range(SIZE) for c in range(SIZE) if rows[r][c] == ord("X")]
answer = bytearray()
for _ in range(SIZE):
    for row, column in sorted(holes):
        answer.append(rows[SIZE + row][column])
    holes = [(column, SIZE - 1 - row) for row, column in holes]
stdout.buffer.write(answer + b"\n")

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
