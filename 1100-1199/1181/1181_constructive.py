TRIANGLE = 3


def main():
    n = int(input())
    color = input().strip()
    poly = list(range(n))
    cuts = []
    while len(poly) > TRIANGLE:
        m = len(poly)
        counts = {}
        for v in poly:
            counts[color[v]] = counts.get(color[v], 0) + 1
        lonely = [k for k in range(m) if counts[color[poly[k]]] == 1]
        if lonely:
            # a color met once: every triangle of the fan from that vertex
            # has it plus two neighbouring vertices, which differ
            k = lonely[0]
            cuts += [(poly[k], poly[(k + j) % m]) for j in range(2, m - 1)]
            break
        # every color is met twice or more; a vertex whose neighbours differ
        # exists, as otherwise two colors would alternate around the whole
        # polygon, and cutting it off leaves all three colors
        k = next(k for k in range(m) if color[poly[k - 1]] != color[poly[(k + 1) % m]])
        cuts.append((poly[k - 1], poly[(k + 1) % m]))
        del poly[k]
    print(len(cuts))
    print("\n".join("%d %d" % (a + 1, b + 1) for a, b in cuts))


main()
