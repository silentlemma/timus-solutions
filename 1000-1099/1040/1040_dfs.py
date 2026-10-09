import sys


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m, ends = data[0], data[1], data[2:]
    adj = [[] for _ in range(n + 1)]
    for e in range(m):
        a, b = ends[2 * e], ends[2 * e + 1]
        adj[a].append((b, e))
        adj[b].append((a, e))
    number = [0] * m
    visited = [False] * (n + 1)
    counter = 0

    # numbers the flights in the order the search meets them; the first flight
    # met at a new airport right after its entry flight k gets k + 1
    def dfs(v):
        nonlocal counter
        visited[v] = True
        for w, e in adj[v]:
            if number[e] == 0:
                counter += 1
                number[e] = counter
                if not visited[w]:
                    dfs(w)

    dfs(1)
    print("YES")
    print(" ".join(map(str, number)))


main()
