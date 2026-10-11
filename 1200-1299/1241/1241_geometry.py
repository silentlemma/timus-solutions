import sys

# the four small triangles of a unit square, cut by both its diagonals
SOUTH = 0
EAST = 1
NORTH = 2
WEST = 3
PARTS = 4
# outward directions of a triangle's edges, counterclockwise from +x
RIGHT = 1 << 0
UP_RIGHT = 1 << 1
UP = 1 << 2
UP_LEFT = 1 << 3
LEFT = 1 << 4
DOWN_LEFT = 1 << 5
DOWN = 1 << 6
DOWN_RIGHT = 1 << 7
TRIANGLE = 3
CUT = 4


def main():
    data = list(map(int, sys.stdin.read().split()))
    m, n, _, *cuts = data
    # a cut runs from border to border, so it is a whole line of one of the
    # four kinds: x = c, y = c, x - y = c or x + y = c
    vert, hor = [False] * (m + 1), [False] * (n + 1)
    diff, total = [False] * (m + n + 1), [False] * (m + n + 1)
    for x1, y1, x2, y2 in zip(*[iter(cuts)] * CUT):
        if x1 == x2:
            vert[x1] = True
        elif y1 == y2:
            hor[y1] = True
        elif x2 - x1 == y2 - y1:
            diff[x1 - y1 + n] = True
        else:
            total[x1 + y1] = True
    parent = list(range(m * n * PARTS))
    out = [0] * (m * n * PARTS)

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    def side(a, da, b, db, cut):
        # join two small triangles, or record their outward directions
        if cut:
            out[a] |= da
            out[b] |= db
        else:
            parent[find(a)] = find(b)

    for i in range(m):
        for j in range(n):
            s = (i * n + j) * PARTS
            e, no, w = s + EAST, s + NORTH, s + WEST
            side(s, UP_RIGHT, e, DOWN_LEFT, total[i + j + 1])
            side(s, UP_LEFT, w, DOWN_RIGHT, diff[i - j + n])
            side(e, UP_LEFT, no, DOWN_RIGHT, diff[i - j + n])
            side(no, DOWN_LEFT, w, UP_RIGHT, total[i + j + 1])
            if j == 0:
                out[s] |= DOWN
            else:
                side(s, DOWN, s - PARTS + NORTH, UP, hor[j])
            if i == 0:
                out[w] |= LEFT
            else:
                side(w, LEFT, s - n * PARTS + EAST, RIGHT, vert[i])
            if j == n - 1:
                out[no] |= UP
            if i == m - 1:
                out[e] |= RIGHT
    # every piece is convex with sides in these 8 directions, one side per
    # direction, so a piece is a triangle when its edges face 3 directions
    faces = {}
    for a, d in enumerate(out):
        r = find(a)
        faces[r] = faces.get(r, 0) | d
    print(sum(1 for d in faces.values() if bin(d).count("1") == TRIANGLE))


main()
