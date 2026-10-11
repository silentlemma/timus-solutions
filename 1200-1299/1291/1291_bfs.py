import sys
from math import gcd


def main():
    words = iter(sys.stdin.buffer.read().split())
    n = int(next(words))
    teeth = [0] * (n + 1)
    adj = [[] for _ in range(n + 1)]
    for i in range(1, n + 1):
        teeth[i] = int(next(words))
        while (j := int(next(words))) != 0:
            # a link may be listed at one end only, so store it both ways
            adj[i].append(j)
            adj[j].append(i)
    root, speed = int(next(words)), int(next(words))
    # meshed gears share the speed of their rims, speed * teeth, and turn
    # opposite ways; so gear j turns at +-speed * teeth[root] / teeth[j]
    rim = speed * teeth[root]
    sign = [0] * (n + 1)
    sign[root] = 1
    queue = [root]
    for u in queue:
        for v in adj[u]:
            if sign[v] == 0:
                sign[v] = -sign[u]
                queue.append(v)
    out = []
    for i in range(1, n + 1):
        if sign[i] == 0:
            out.append("0/1")
        else:
            g = gcd(rim, teeth[i])
            out.append("%d/%d" % (sign[i] * rim // g, teeth[i] // g))
    print("\n".join(out))


main()
