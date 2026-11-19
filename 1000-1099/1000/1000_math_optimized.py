import os
from sys import stdout

left, right = map(int, open(0, "rb", buffering=0).read().split())
print(left + right)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
