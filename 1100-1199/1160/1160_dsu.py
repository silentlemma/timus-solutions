import sys


def main():
    tok = iter(map(int, sys.stdin.buffer.read().split()))
    n, m = next(tok), next(tok)
    edges = sorted(((next(tok), next(tok), next(tok)) for _ in range(m)), key=lambda e: e[2])
    parent = list(range(n + 1))

    def find(v):
        while parent[v] != v:
            parent[v] = parent[parent[v]]
            v = parent[v]
        return v

    # Kruskal's tree: its longest cable is the smallest possible longest
    # cable of any plan that connects every hub
    chosen = []
    for a, b, length in edges:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb
            chosen.append((a, b, length))
    out = [str(chosen[-1][2]), str(len(chosen))] + ["%d %d" % (a, b) for a, b, _ in chosen]
    sys.stdout.write("\n".join(out) + "\n")


main()
