import os
from sys import stdout

left_bound, right_bound, total = map(int, open(0, "rb", buffering=0).read().split())
left = min(left_bound, total)
right = total - left
if right <= right_bound:
    print(left, right)
else:
    print("Impossible")

# The answer is flushed before interpreter teardown is skipped.
stdout.flush()
os._exit(0)
