import sys


def main():
    k = int(sys.stdin.readline())
    # roots[v]: the residues s with v + s * s = 0 (mod k), the residues of
    # the earlier numbers b joined to a number a = v by a + b * b = 0
    roots = [[] for _ in range(k)]
    for s in range(k):
        roots[(-s * s) % k].append(s)
    parent = [0]
    written = [[] for _ in range(k)]  # the numbers so far, by residue

    def find(x):
        root = x
        while parent[root] != root:
            root = parent[root]
        while parent[x] != root:
            parent[x], x = root, parent[x]
        return root

    a = 0
    while True:
        a += 1
        parent.append(a)
        r = a % k
        for s in {(-r * r) % k, *roots[r]}:
            for b in written[s]:
                # every edge either joins two trees or closes the first cycle
                ra, rb = find(a), find(b)
                if ra == rb:
                    print(a)
                    return
                parent[rb] = ra
        written[r].append(a)


main()
