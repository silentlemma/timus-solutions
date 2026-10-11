import sys
from collections import deque


def main():
    nums = map(int, sys.stdin.read().split())
    k = next(nums)
    n, m, s, f = next(nums), next(nums), next(nums), next(nums)
    cost = [next(nums) for _ in range(n)]
    if s == f:
        print("NO")
        return
    # station v enters at 2v and leaves at 2v + 1; the arc between them
    # costs the police needed there. Museum and refuge cannot be taken,
    # and anything above K counts as too much
    big = k + 1
    head = [-1] * (2 * n)
    to, cap, nxt = [], [], []

    def arc(a, b, c):
        for u, v, w in ((a, b, c), (b, a, 0)):
            to.append(v)
            cap.append(w)
            nxt.append(head[u])
            head[u] = len(to) - 1

    for v in range(n):
        arc(2 * v, 2 * v + 1, big if v + 1 in (s, f) else min(cost[v], big))
    for _ in range(m):
        a, b = next(nums) - 1, next(nums) - 1
        arc(2 * a + 1, 2 * b, big)
        arc(2 * b + 1, 2 * a, big)
    source, sink = 2 * (s - 1) + 1, 2 * (f - 1)
    # Dinic's blocking flows until the flow exceeds K or nothing gets through
    flow = 0
    while flow <= k:
        level = [-1] * (2 * n)
        level[source] = 0
        queue = deque([source])
        while queue:
            u = queue.popleft()
            e = head[u]
            while e >= 0:
                if cap[e] and level[to[e]] < 0:
                    level[to[e]] = level[u] + 1
                    queue.append(to[e])
                e = nxt[e]
        if level[sink] < 0:
            break
        current = head[:]

        def push(u, limit):
            if u == sink:
                return limit
            while current[u] >= 0:
                e = current[u]
                v = to[e]
                if cap[e] and level[v] == level[u] + 1:
                    got = push(v, min(limit, cap[e]))
                    if got:
                        cap[e] -= got
                        cap[e ^ 1] += got
                        return got
                current[u] = nxt[e]
            return 0

        while flow <= k:
            got = push(source, big)
            if not got:
                break
            flow += got
    print("YES" if flow <= k else "NO")


main()
