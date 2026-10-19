import sys


def straighten(points):
    # drop repeated points and points in the middle of a straight run
    out = []
    for p in points:
        if out and out[-1] == p:
            continue
        while len(out) >= 2 and (out[-2][0] == out[-1][0] == p[0]
                                 or out[-2][1] == out[-1][1] == p[1]):
            out.pop()
        out.append(p)
    return out


def main():
    w, h, x, y, d = map(int, sys.stdin.read().split())
    half = w * h // 2
    # Finland always holds the column of cells along its coast (the border
    # cannot touch that coast), the lighthouse, and a corridor of cells from
    # the lighthouse to that column
    right = w - 1 - x - d
    if h + d * d + right > half:
        print("Impossible")
        return
    if h + d * (w - 1 - x) <= half:
        # every row of Finland runs from column c[r] to the coast: the rows
        # of the lighthouse from x on, the others from w - 1, and the area
        # still missing pushes rows west from the top down
        extra = half - (h + d * (w - 1 - x))
        cuts = []  # (rows, column) from the top down
        for top, bottom, column in ((h, y + d, w - 1), (y + d, y, x), (y, 0, w - 1)):
            rows = top - bottom
            if rows == 0:
                continue
            full = min(rows, extra // (column - 1)) if column > 1 else 0
            extra -= full * (column - 1)
            if full:
                cuts.append((full, 1))
            if full < rows:
                part = min(extra, column - 1)
                extra -= part
                cuts.append((1, column - part))
                if full + 1 < rows:
                    cuts.append((rows - full - 1, column))
        points, level = [(cuts[0][1], h)], h
        for rows, column in cuts:
            points += [(column, level), (column, level - rows)]
            level -= rows
    else:
        # the border goes round the lighthouse: Finland takes full corridor
        # rows at the top of the lighthouse rows and part of one more row
        rest = half - (h + d * d + right)
        more, part = divmod(rest, right)
        level = y + d - 1 - more
        points = [(w - 1, h), (w - 1, y + d), (x, y + d), (x, y), (x + d, y), (x + d, level),
                  (w - 1 - part, level), (w - 1 - part, level - 1), (w - 1, level - 1), (w - 1, 0)]
    points = straighten(points)
    print(len(points))
    print("\n".join("%d %d" % p for p in points))


main()
