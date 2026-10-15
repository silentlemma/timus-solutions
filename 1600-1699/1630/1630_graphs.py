import sys

MAX_CLIQUE = 4  # four points pairwise 1 apart fit in space, five do not


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    parent = list(range(n))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    degree = [0] * n
    ends = []
    nums = iter(data[2 : 2 + 2 * m])
    for a, b in zip(nums, nums):
        u, v = int(a) - 1, int(b) - 1
        degree[u] += 1
        degree[v] += 1
        ends.append(u)
        parent[find(u)] = find(v)
    size, edges, widest = [0] * n, [0] * n, [0] * n
    for v in range(n):
        root = find(v)
        size[root] += 1
        widest[root] = max(widest[root], degree[v])
    for u in ends:
        edges[find(u)] += 1
    # every component must be a path or a clique of at most four vertices
    for root in range(n):
        k = size[root]
        if not k:
            continue
        path = edges[root] == k - 1 and widest[root] <= 2
        clique = edges[root] == k * (k - 1) // 2 and k <= MAX_CLIQUE
        if not path and not clique:
            print("Unlucky Petr")
            return
    print("Luck is possible")


main()
