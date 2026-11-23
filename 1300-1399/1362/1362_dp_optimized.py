import os
import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    adj = [[] for _ in range(n + 1)]
    pos = 1
    for boss in range(1, n + 1):
        while data[pos] != b"0":
            v = int(data[pos])
            adj[boss].append(v)
            adj[v].append(boss)
            pos += 1
        pos += 1
    root = int(data[pos])
    # calls go both up and down, so the news spreads over the tree rooted
    # at Tanya; order parents before children
    parent = [0] * (n + 1)
    parent[root] = -1
    order = [root]
    for v in order:
        for u in adj[v]:
            if u != parent[v]:
                parent[u] = v
                order.append(u)
    # time[v]: minutes v needs to tell its whole subtree; the slowest
    # subtrees are called first, the i-th call starting at minute i
    kids = [None] * (n + 1)
    answer = 0
    for v in reversed(order):
        child_times = kids[v]
        delay = 0
        if child_times is not None:
            child_times.sort(reverse=True)
            for index, value in enumerate(child_times, 1):
                candidate = value + index
                if candidate > delay:
                    delay = candidate
        p = parent[v]
        if p > 0:
            if kids[p] is None:
                kids[p] = [delay]
            else:
                kids[p].append(delay)
        else:
            answer = delay
    print(answer)


main()


if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
