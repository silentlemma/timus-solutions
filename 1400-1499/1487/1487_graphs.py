import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    table = data[1 : n + 1]
    beaten_by = [[] for _ in range(n)]
    indegree = [0] * n
    for i in range(n):
        row = table[i]
        for j in range(n):
            if row[j] == ord("1"):
                beaten_by[j].append(i)
                indegree[j] += 1

    # stronger[v]: every team that is stronger than v, as a bit set; the
    # results are transitive, so the wins form an acyclic graph
    winners = [[] for _ in range(n)]
    for j in range(n):
        for i in beaten_by[j]:
            winners[i].append(j)
    stronger = [0] * n
    queue = [v for v in range(n) if indegree[v] == 0]
    for v in queue:
        for u in winners[v]:
            stronger[u] |= stronger[v] | (1 << v)
            indegree[u] -= 1
            if indegree[u] == 0:
                queue.append(u)

    # A plays better than B when no team stronger than B is stronger than A
    q = int(data[n + 1])
    asked = data[n + 2 :]
    out = []
    for k in range(q):
        a, b = int(asked[2 * k]) - 1, int(asked[2 * k + 1]) - 1
        out.append("No" if stronger[a] & stronger[b] else "YES")
    sys.stdout.write("\n".join(out) + "\n")


main()
