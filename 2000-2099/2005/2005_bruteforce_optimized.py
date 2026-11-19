import os
from sys import stdout

POINTS = 5
FIRST = 1
FORBIDDEN_LAST = 2
LAST = POINTS - 2
MIDDLE_SUM = sum(range(FIRST, LAST + 1))
costs = list(map(int, open(0, "rb", buffering=0).read().split()))
best = route = None
for a in range(FIRST, LAST + 1):
    for b in range(FIRST, LAST + 1):
        if a == b:
            continue
        c = MIDDLE_SUM - a - b
        if c == FORBIDDEN_LAST:
            continue
        cost = (
            costs[a]
            + costs[POINTS * a + b]
            + costs[POINTS * b + c]
            + costs[POINTS * c + POINTS - 1]
        )
        if best is None or cost < best:
            best, route = cost, (1, a + 1, b + 1, c + 1, POINTS)
print(best)
print(*route)

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
