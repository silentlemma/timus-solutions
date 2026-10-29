import sys
from itertools import permutations

POINTS = 5
# point k has index k - 1: start 0, middle points FIRST_MIDDLE..LAST_MIDDLE, finish END
FIRST_MIDDLE = 1
POINT_3 = 2
LAST_MIDDLE = 3
END = 4

numbers = list(map(int, sys.stdin.read().split()))
d = [numbers[POINTS * i : POINTS * (i + 1)] for i in range(POINTS)]
best, route = None, None
# points 2, 3 and 4 (indices 1, 2, 3) come in any order, except that 3 may
# not be the last of them
for a, b, c in permutations(range(FIRST_MIDDLE, LAST_MIDDLE + 1)):
    if c == POINT_3:
        continue
    cost = d[0][a] + d[a][b] + d[b][c] + d[c][END]
    if best is None or cost < best:
        best, route = cost, (0, a, b, c, END)
print(best)
print(*(point + 1 for point in route))
