import os
from sys import stdout

panels, width, height = map(int, open(0, "rb", buffering=0).read().split())
print(2 * panels * width * height)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
