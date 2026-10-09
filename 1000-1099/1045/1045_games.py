import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, ends = data[0], data[1], data[2:]
    adj = [[] for _ in range(n + 1)]
    for i in range(n - 1):
        a, b = ends[2 * i], ends[2 * i + 1]
        adj[a].append(b)
        adj[b].append(a)
    # the destroyed airports are exactly the ones on the way back to k, so a
    # move always goes down the tree rooted at k; a breadth-first order lists
    # parents before children
    parent = [0] * (n + 1)
    parent[k] = -1
    order = [k]
    for v in order:
        for w in adj[v]:
            if w != parent[v]:
                parent[w] = v
                order.append(w)
    # win[v]: the player to move at v wins, that is, some child is a loss
    win = [False] * (n + 1)
    for v in reversed(order[1:]):
        if not win[v]:
            win[parent[v]] = True
    good = [w for w in adj[k] if not win[w]]
    if good:
        print("First player wins flying to airport %d" % min(good))
    else:
        print("First player loses")


main()
