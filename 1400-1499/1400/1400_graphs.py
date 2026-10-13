import sys


def distances(n, m, start):
    """Key presses from the start to every character, by breadth-first search."""
    dist = [-1] * n
    dist[start] = 0
    queue = [start]
    for v in queue:
        # left and right run on through the rows; up and down stop at the edges
        for u in ((v - 1) % n, (v + 1) % n, v - m if v >= m else v, v + m if v + m < n else v):
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                queue.append(u)
    return dist


def main():
    n, m = map(int, sys.stdin.read().split()[:2])
    best = min((distances(n, m, s) for s in range(n)), key=sum)
    out = ["Mean = %.2f" % (sum(best) / n)]
    for r in range(0, n, m):
        out.append(" ".join(map(str, best[r : r + m])))
    print("\n".join(out))


main()
