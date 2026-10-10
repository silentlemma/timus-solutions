# the cube: A B C D around the bottom face, E F G H above them
EDGES = ["AB", "BC", "CD", "DA", "EF", "FG", "GH", "HE", "AE", "BF", "CG", "DH"]
# the cube is bipartite; every operation changes one chamber of each side
EVEN = "ACFH"
CELLS = "ABCDEFGH"


def main():
    count = dict(zip(CELLS, map(int, input().split())))
    if sum(count[c] for c in EVEN) != sum(count[c] for c in CELLS if c not in EVEN):
        print("IMPOSSIBLE")
        return
    near = {c: [e[1] if e[0] == c else e[0] for e in EDGES if c in e] for c in CELLS}
    steps = []
    # annihilate along every edge as long as both ends hold duons; afterwards
    # every edge has an empty end
    for u, v in EDGES:
        k = min(count[u], count[v])
        steps += ["%s%s-" % (u, v)] * k
        count[u] -= k
        count[v] -= k
    # what is left can only sit at two opposite corners u and w, in equal
    # numbers; a pair made on the middle edge of a path u x y w removes both
    for u in EVEN:
        if count[u]:
            w = next(c for c in CELLS if count[c] and c not in EVEN)
            x = near[u][0]
            y = next(c for c in near[x] if c in near[w])
            steps += ["%s%s+" % (x, y), "%s%s-" % (u, x), "%s%s-" % (y, w)] * count[u]
            count[w] -= count[u]
            count[u] = 0
    print("\n".join(steps))


main()
