import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    adj = [[] for _ in range(n + 1)]
    for i, p in enumerate(data[1:n], start=2):
        adj[i].append(p)
        adj[p].append(i)

    def bfs(s):
        """Distances from s and the predecessors on the shortest paths."""
        dist = [-1] * (n + 1)
        prev = [0] * (n + 1)
        dist[s] = 0
        queue = [s]
        for v in queue:
            for w in adj[v]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    prev[w] = v
                    queue.append(w)
        return dist, prev

    # the farthest computer from any start is an end of a longest path; the
    # farthest one from it is the other end
    dist, _ = bfs(1)
    u = max(range(1, n + 1), key=dist.__getitem__)
    dist, prev = bfs(u)
    v = max(range(1, n + 1), key=dist.__getitem__)
    # the centers are the middle one or two computers of that path
    length = dist[v]
    path = [v]
    while len(path) <= length:
        path.append(prev[path[-1]])
    centers = sorted({path[length // 2], path[(length + 1) // 2]})
    print(" ".join(map(str, centers)))


main()
