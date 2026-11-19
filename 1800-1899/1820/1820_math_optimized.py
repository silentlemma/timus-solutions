import os
from sys import stdout

steaks, capacity = map(int, open(0, "rb", buffering=0).read().split())
print(max(2, (2 * steaks + capacity - 1) // capacity))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
