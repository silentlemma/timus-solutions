import os
from sys import stdout

elements, maximum = map(int, open(0, "rb", buffering=0).read().split())
print(elements * (maximum + 1))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
