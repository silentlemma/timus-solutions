import os
from sys import stdout

WIDTH = 4
tokens = list(map(int, open(0, "rb", buffering=0).read().split()))
count, columns = tokens[:2]
height = (count + columns - 1) // columns
for row in range(height):
    print("".join(str(tokens[2 + at]).rjust(WIDTH) for at in range(row, count, height)))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
