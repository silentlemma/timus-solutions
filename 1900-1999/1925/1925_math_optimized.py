import os
from sys import stdout

values = iter(map(int, open(0, "rb", buffering=0).read().split()))
count, current = next(values), next(values)
answer = current - 2
for _ in range(count):
    answer += next(values) - next(values) - 2
print(answer if answer >= 0 else "Big Bang!")

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
