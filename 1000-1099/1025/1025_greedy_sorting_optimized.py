import os
from sys import stdout

values = map(int, open(0, "rb", buffering=0).read().split())
count = next(values)
groups = sorted(values)
needed = count // 2 + 1
print(sum(size // 2 + 1 for size in groups[:needed]))

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
