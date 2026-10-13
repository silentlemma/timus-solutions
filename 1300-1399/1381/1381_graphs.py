import sys

CHECK_EVERY = 8  # passes between looks for a cycle among the last improvements


def has_cycle(parent, nodes):
    """Does following parent links from some node come back to a node?"""
    state = dict.fromkeys(nodes, 0)  # 0 new, 1 on the current walk, 2 done
    for start in nodes:
        walk, v = [], start
        while v is not None and state[v] == 0:
            state[v] = 1
            walk.append(v)
            v = parent[v]
        if v is not None and state[v] == 1:
            return True
        for u in walk:
            state[u] = 2
    return False


def negative_cycle(nodes, edges):
    """Bellman-Ford from every node at once: is some cycle negative?"""
    dist = dict.fromkeys(nodes, 0)
    parent = dict.fromkeys(nodes)
    for rounds in range(1, len(nodes) + 1):
        changed = False
        for v, u, w in edges:
            if dist[v] + w < dist[u]:
                dist[u], parent[u], changed = dist[v] + w, v, True
        if not changed:
            return False
        # a cycle among the parent links is always a negative one
        if rounds % CHECK_EVERY == 0 and has_cycle(parent, nodes):
            return True
    return True


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    s = n + 1
    # rule[j][i][k]: cockroaches next month in a flat with j, i below, k above
    rule = [
        [data[1 + (j * s + i) * s : 1 + (j * s + i + 1) * s] for i in range(s)] for j in range(s)
    ]
    # a finite floor plan read upwards is a closed walk through the pair (0, 0)
    # of the graph on pairs of neighbours; a step (a, b) -> (b, c) changes the
    # total by rule[b][a][c] - b, so the totals of a walk give the change
    edges = []
    for a in range(s):
        for b in range(s):
            for c in range(s):
                edges.append((a * s + b, b * s + c, rule[b][a][c] - b))
    out_of, into = [[] for _ in range(s * s)], [[] for _ in range(s * s)]
    for v, u, _ in edges:
        out_of[v].append(u)
        into[u].append(v)

    def reach(links):
        seen, stack = {0}, [0]
        while stack:
            for u in links[stack.pop()]:
                if u not in seen:
                    seen.add(u)
                    stack.append(u)
        return seen

    nodes = sorted(reach(out_of) & reach(into))
    keep = set(nodes)
    edges = [e for e in edges if e[0] in keep and e[1] in keep]
    fall = negative_cycle(nodes, edges)
    rise = negative_cycle(nodes, [(v, u, -w) for v, u, w in edges])
    signs = {(False, False): "=", (True, False): "<", (False, True): ">", (True, True): "<>"}
    print(signs[fall, rise])


main()
