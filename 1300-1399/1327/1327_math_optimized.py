import os
from sys import stdout

first, last = map(int, open(0, "rb", buffering=0).read().split())
print((last + 1) // 2 - first // 2)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
