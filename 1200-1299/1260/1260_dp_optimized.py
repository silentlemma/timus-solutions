import os
import sys

count = int(sys.stdin.buffer.read())
older, old, current = -1, 0, 1
for _ in range(1, count):
    older, old, current = old, current, current + older + 1
print(current)

# Finish the answer before avoiding interpreter teardown on the judge.
sys.stdout.flush()
os._exit(0)
