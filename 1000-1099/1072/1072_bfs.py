import sys
from collections import deque

OCTET_BITS = 8


def address(s):
    value = 0
    for part in s.split("."):
        value = value << OCTET_BITS | int(part)
    return value


def main():
    tok = sys.stdin.read().split()
    n = int(tok[0])
    pos = 1
    # each interface is reduced to its subnet, IP AND mask
    nets = []
    for _ in range(n):
        k = int(tok[pos])
        pos += 1
        nets.append({address(tok[pos + 2 * j]) & address(tok[pos + 2 * j + 1]) for j in range(k)})
        pos += 2 * k
    start, end = int(tok[pos]) - 1, int(tok[pos + 1]) - 1
    linked = [[not nets[u].isdisjoint(nets[v]) for v in range(n)] for u in range(n)]
    came = [-1] * n
    came[start] = start
    queue = deque([start])
    while queue:
        u = queue.popleft()
        for v in range(n):
            if came[v] < 0 and linked[u][v]:
                came[v] = u
                queue.append(v)
    if came[end] < 0:
        print("No")
        return
    path = [end]
    while path[-1] != start:
        path.append(came[path[-1]])
    print("Yes")
    print(" ".join(str(v + 1) for v in reversed(path)))


main()
