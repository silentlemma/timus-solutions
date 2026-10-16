import sys


def swagness(s):
    n = len(s)
    # suffix automaton; first[v] is the end of the first occurrence of v
    nxt, link, size, first = [{}], [-1], [0], [0]
    prefix = []
    last = 0
    for i, ch in enumerate(s):
        cur = len(size)
        nxt.append({})
        link.append(0)
        size.append(size[last] + 1)
        first.append(i)
        p = last
        while p != -1 and ch not in nxt[p]:
            nxt[p][ch] = cur
            p = link[p]
        if p != -1:
            q = nxt[p][ch]
            if size[p] + 1 == size[q]:
                link[cur] = q
            else:
                clone = len(size)
                nxt.append(nxt[q].copy())
                link.append(link[q])
                size.append(size[p] + 1)
                first.append(first[q])
                while p != -1 and nxt[p].get(ch) == q:
                    nxt[p][ch] = clone
                    p = link[p]
                link[q] = clone
                link[cur] = clone
        last = cur
        prefix.append(cur)
    states = len(size)
    # the states in order of length, by counting
    by_size = [[] for _ in range(n + 1)]
    for v in range(states):
        by_size[size[v]].append(v)
    order = [v for group in by_size for v in group]

    # a state with exactly one way out is squeezed into the edge through it
    keep = [v == 0 or len(nxt[v]) != 1 for v in range(states)]
    target = list(range(states))
    extra = [0] * states
    for v in reversed(order):
        if not keep[v]:
            (t,) = nxt[v].values()
            target[v] = target[t]
            extra[v] = extra[t] + 1
    # the compressed edges and, for each, its label s[from .. to]
    edge_source, edge_dest, edge_from, edge_to = [], [], [], []
    for u in range(states):
        if keep[u]:
            for t in nxt[u].values():
                dest = target[t]
                to = first[dest]
                edge_source.append(u)
                edge_dest.append(dest)
                edge_from.append(to - extra[t])
                edge_to.append(to)
    edges = len(edge_to)

    # the suffix link tree in Euler order
    children = [[] for _ in range(states)]
    for v in range(1, states):
        children[link[v]].append(v)
    tin = [0] * states
    tout = [0] * states
    timer = 1
    stack = [(0, iter(children[0]))]
    while stack:
        v, rest = stack[-1]
        child = next(rest, None)
        if child is None:
            tout[v] = timer
            stack.pop()
        else:
            tin[child] = timer
            timer += 1
            stack.append((child, iter(children[child])))
    # the latest end seen in a subtree, as a segment tree of maxima
    width = 1
    while width < states:
        width *= 2
    latest = [0] * (2 * width)

    by_end = [[] for _ in range(n + 1)]
    for e in range(edges):
        by_end[edge_to[e] + 1].append(e)
    # count[p]: distinct substrings of s[0 .. end) whose last occurrence
    # starts at p, kept in two Fenwick trees for range adds and sums
    plain = [0] * (n + 1)
    scaled = [0] * (n + 1)
    tree_size = n + 1

    def add(lo, hi, value):
        if lo >= hi:
            return
        at = lo + 1
        while at < tree_size:
            plain[at] += value
            scaled[at] += value * lo
            at += at & -at
        at = hi + 1
        while at < tree_size:
            plain[at] -= value
            scaled[at] -= value * hi
            at += at & -at

    def total_below(count):
        a = b = 0
        at = count
        while at:
            a += plain[at]
            b += scaled[at]
            at &= at - 1
        return a * count - b

    distinct = [0] * edges
    # the states on one suffix link path that share their last end form
    # chains, and top[end] is the state just above a chain
    seen = [False] * states
    seen[0] = True
    top = [0] * (n + 1)
    for end in range(1, n + 1):
        v = prefix[end - 1]
        add(end - size[v], end, 1)
        u = v
        while not seen[u]:
            seen[u] = True
            u = link[u]
        while u:
            lo, hi = tin[u] + width, tout[u] + width
            was = 0
            while lo < hi:
                if lo & 1:
                    if latest[lo] > was:
                        was = latest[lo]
                    lo += 1
                if hi & 1:
                    hi -= 1
                    if latest[hi] > was:
                        was = latest[hi]
                lo >>= 1
                hi >>= 1
            above = top[was]
            add(was - size[u], was - size[above], -1)
            top[was] = u
            u = above
        at = tin[v] + width
        latest[at] = end
        while at > 1:
            at >>= 1
            latest[at] = end
        top[end] = 0
        for e in by_end[end]:
            distinct[e] = total_below(end) - total_below(edge_from[e])

    # each compressed edge stands for as many tree edges as there are
    # paths from the root to its source
    out = [[] for _ in range(states)]
    for e in range(edges):
        out[edge_source[e]].append(e)
    paths = [0] * states
    paths[0] = 1
    total = 0
    for v in order:
        ways = paths[v]
        if keep[v] and ways:
            for e in out[v]:
                total += ways * distinct[e]
                paths[edge_dest[e]] += ways
    return total


def main():
    data = sys.stdin.read().split()
    count = int(data[0])
    print("\n".join(str(swagness(s)) for s in data[1:1 + count]))


main()
