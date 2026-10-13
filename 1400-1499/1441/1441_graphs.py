import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    ends = [int(x) for x in data[2 : 2 + 2 * m]]
    # vertex 0 is a helper joined to every room with an odd number of tunnels
    degree = [0] * (n + 1)
    for v in ends:
        degree[v] += 1
    for v in range(1, n + 1):
        if degree[v] % 2:
            ends += [0, v]
    adj = [[] for _ in range(n + 1)]
    for e in range(len(ends) // 2):
        a, b = ends[2 * e], ends[2 * e + 1]
        adj[a].append(e)
        adj[b].append(e)
    # an Euler circuit, found without recursion
    used = [False] * (len(ends) // 2)
    pos = [0] * (n + 1)
    start = 0 if adj[0] else 1
    stack = [start]
    circuit = []
    while stack:
        v = stack[-1]
        edges = adj[v]
        while pos[v] < len(edges) and used[edges[pos[v]]]:
            pos[v] += 1
        if pos[v] == len(edges):
            circuit.append(stack.pop())
            continue
        e = edges[pos[v]]
        used[e] = True
        stack.append(ends[2 * e] + ends[2 * e + 1] - v)
    # the helper edges cut the circuit into trails of real tunnels
    trails = []
    current = []
    for v in circuit:
        if v == 0:
            if current:
                trails.append(current)
            current = []
        else:
            current.append(v)
    if current:
        trails.append(current)
    out = [str(len(trails))]
    out += [" ".join(map(str, t)) for t in trails]
    sys.stdout.write("\n".join(out) + "\n")


main()
