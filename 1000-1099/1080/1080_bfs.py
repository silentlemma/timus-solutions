import sys
from collections import deque


def main():
    tok = list(map(int, sys.stdin.read().split()))
    n = tok[0]
    adj = [[] for _ in range(n + 1)]
    pos = 1
    for i in range(1, n + 1):
        while tok[pos] != 0:
            adj[i].append(tok[pos])
            adj[tok[pos]].append(i)
            pos += 1
        pos += 1
    # the map is connected, so the colour of the first country decides all
    color = [-1] * (n + 1)
    color[1] = 0
    queue = deque([1])
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] < 0:
                color[v] = 1 - color[u]
                queue.append(v)
            elif color[v] == color[u]:
                print(-1)
                return
    print("".join(str(c) for c in color[1:]))


main()
