import os
from sys import stdout

stripes = int(open(0, "rb", buffering=0).read())
previous, current = 2, 2
for _ in range(stripes - 2):
    previous, current = current, previous + current
print(current)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
