import sys
from collections import deque


def main():
    tok = list(map(int, sys.stdin.read().split()))
    k = tok[0]
    route, back = tok[1 : 2 * k + 1 : 2], tok[2 : 2 * k + 2 : 2]
    *_, t, s1, s2 = tok
    by_route = {}
    for j in range(k):
        by_route.setdefault(route[j], []).append(j)
    # a state is the plate in hand: the first one, or the plate of bus j; a
    # driver swaps when the plate in hand shows the route of his bus
    came = [None] * k
    queue = deque([(s1, s2, -1)])
    while queue:
        x, y, j = queue.popleft()
        for r in {x, y}:
            for i in by_route.pop(r, []):
                came[i] = j
                if t in (route[i], back[i]):
                    path = []
                    while i >= 0:
                        path.append(i + 1)
                        i = came[i]
                    print(len(path))
                    print("\n".join(map(str, reversed(path))))
                    return
                queue.append((route[i], back[i], i))
    print("IMPOSSIBLE")


main()
