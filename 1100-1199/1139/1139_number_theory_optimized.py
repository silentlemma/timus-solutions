import os
from sys import stdout

rows, columns = map(int, open(0, "rb", buffering=0).read().split())
left, right = rows - 1, columns - 1
total = left + right
while right:
    left, right = right, left % right
print(total - left)

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
