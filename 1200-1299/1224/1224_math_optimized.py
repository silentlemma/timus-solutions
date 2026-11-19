import os
from sys import stdout

rows, columns = map(int, open(0, "rb", buffering=0).read().split())
print(2 * (rows - 1) if rows <= columns else 2 * columns - 1)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
