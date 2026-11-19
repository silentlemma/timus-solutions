import os
from sys import stdout

DIGITS = 9
BASE = 10
target = int(open(0, "rb", buffering=0).read())
ways = [1]
for length in range(1, DIGITS + 1):
    following = []
    window = 0
    for total in range(min(target, length * (BASE - 1)) + 1):
        if total < len(ways):
            window += ways[total]
        if total >= BASE and total - BASE < len(ways):
            window -= ways[total - BASE]
        following.append(window)
    ways = following
print(ways[target] + (target == 1))

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
