import sys


def main():
    s, p = sys.stdin.read().split()[:2]
    n, m = len(s), len(p)
    # every erased character is a node; a node on the source side becomes
    # 1, on the sink side 0. Characters s[j] and p[i] meet once in every
    # window where j - i is between 0 and n - m, and differing costs 1.
    node_s = [-1] * n
    node_p = [-1] * m
    count = 0
    for j in range(n):
        if s[j] == "?":
            node_s[j] = count
            count += 1
    for i in range(m):
        if p[i] == "?":
            node_p[i] = count
            count += 1
    source, sink = count, count + 1
    ones = [0] * count  # pairs with a fixed 1: cost when the node is 0
    zeros = [0] * count  # pairs with a fixed 0: cost when the node is 1
    base = 0
    # arcs in pairs e, e ^ 1: an undirected edge is two arcs of full
    # capacity, each the reverse of the other
    head = [[] for _ in range(count + 2)]
    target, cap = [], []

    def link(a, b, forward, backward):
        head[a].append(len(target))
        target.append(b)
        cap.append(forward)
        head[b].append(len(target))
        target.append(a)
        cap.append(backward)

    for i in range(m):
        a, u = p[i], node_p[i]
        for j in range(i, i + n - m + 1):
            b, v = s[j], node_s[j]
            if u < 0 and v < 0:
                base += a != b
            elif u < 0 or v < 0:
                w, c = (v, a) if u < 0 else (u, b)
                if c == "1":
                    ones[w] += 1
                else:
                    zeros[w] += 1
            else:
                link(u, v, 1, 1)
    for w in range(count):
        # a node with both kinds of fixed partners pays the smaller anyway
        both = min(ones[w], zeros[w])
        base += both
        if ones[w] > both:
            link(source, w, ones[w] - both, 0)
        if zeros[w] > both:
            link(w, sink, zeros[w] - both, 0)
    flow = 0
    while True:
        level = [-1] * (count + 2)
        level[source] = 0
        queue = [source]
        for v in queue:
            for e in head[v]:
                if cap[e] and level[target[e]] < 0:
                    level[target[e]] = level[v] + 1
                    queue.append(target[e])
        if level[sink] < 0:
            break
        arc = [0] * (count + 2)
        while True:
            # one augmenting path along the levels, found without recursion
            path = []
            v = source
            while v != sink:
                edges = head[v]
                while arc[v] < len(edges):
                    e = edges[arc[v]]
                    if cap[e] and level[target[e]] == level[v] + 1:
                        break
                    arc[v] += 1
                if arc[v] == len(edges):
                    if v == source:
                        break
                    level[v] = -1
                    v = target[path.pop() ^ 1]
                    arc[v] += 1
                    continue
                path.append(edges[arc[v]])
                v = target[edges[arc[v]]]
            if v != sink:
                break
            push = min(cap[e] for e in path)
            for e in path:
                cap[e] -= push
                cap[e ^ 1] += push
            flow += push
    # the source side of the last search is a minimum cut
    seen = [False] * (count + 2)
    seen[source] = True
    queue = [source]
    for v in queue:
        for e in head[v]:
            if cap[e] and not seen[target[e]]:
                seen[target[e]] = True
                queue.append(target[e])

    def fill(text, nodes):
        return "".join(("1" if seen[nodes[k]] else "0") if c == "?" else c
                       for k, c in enumerate(text))

    print(base + flow)
    print(fill(s, node_s))
    print(fill(p, node_p))


main()
