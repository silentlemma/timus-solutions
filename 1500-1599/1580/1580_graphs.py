import sys
from collections import deque


def show(twice):
    """A sum given in halves of a rouble, with two digits after the point."""
    sign = "-" if twice < 0 else ""
    whole, half = divmod(abs(twice), 2)
    return "%s%d.%s" % (sign, whole, "50" if half else "00")


def main():
    words = iter(sys.stdin.buffer.read().split())
    n, m = int(next(words)), int(next(words))
    edges = [(int(next(words)) - 1, int(next(words)) - 1, int(next(words))) for _ in range(m)]
    adj = [[] for _ in range(n)]
    for u, v, a in edges:
        adj[u].append((v, a))
        adj[v].append((u, a))
    # in halves of a rouble, each debt in a component is sign * t + base for the
    # debt t of its first student; an edge closing an odd cycle fixes t
    sign, base = [0] * n, [0] * n
    twice = [0] * n
    for start in range(n):
        if sign[start]:
            continue
        sign[start] = 1
        comp, queue, fixed = [start], deque([start]), None
        while queue:
            v = queue.popleft()
            for u, a in adj[v]:
                if not sign[u]:
                    sign[u], base[u] = -sign[v], 2 * a - base[v]
                    comp.append(u)
                    queue.append(u)
                elif sign[u] == sign[v] and fixed is None:
                    fixed = (2 * a - base[u] - base[v]) // (2 * sign[v])
        if fixed is None:
            # no odd cycle: one debt can move freely against its neighbours
            print("IMPOSSIBLE")
            return
        for v in comp:
            twice[v] = sign[v] * fixed + base[v]
    # the claims may also contradict each other
    if any(twice[u] + twice[v] != 2 * a for u, v, a in edges):
        print("IMPOSSIBLE")
        return
    print("\n".join(show(t) for t in twice))


main()
