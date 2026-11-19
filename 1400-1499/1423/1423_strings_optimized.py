import os
from sys import stdout

size, first, second = open(0, "rb", buffering=0).read().split()
size = int(size)
offset = (first + first).find(second)
print(-1 if offset < 0 else (size - offset) % size)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
