import heapq
import sys


def main():
    code = list(map(int, sys.stdin.read().split()))
    n = len(code) + 1
    # a vertex stays until all its neighbours but one are removed, and each
    # removed neighbour writes the vertex once
    deg = [1] * (n + 1)
    for c in code:
        deg[c] += 1
    leaves = [u for u in range(1, n + 1) if deg[u] == 1]
    heapq.heapify(leaves)
    adj = [[] for _ in range(n + 1)]
    for c in code:
        leaf = heapq.heappop(leaves)
        adj[leaf].append(c)
        adj[c].append(leaf)
        deg[c] -= 1
        if deg[c] == 1:
            heapq.heappush(leaves, c)
    out = ["%d: %s" % (u, " ".join(map(str, sorted(adj[u])))) for u in range(1, n + 1)]
    sys.stdout.write("\n".join(out) + "\n")


main()
