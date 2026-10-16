import sys

HEADER = 3
CORNERS = 3


def main():
    v = [int(w) for w in sys.stdin.read().split()]
    mana, h, top = v[0], v[1], v[2]
    pts = [(v[i], v[i + 1]) for i in range(HEADER, len(v), 2)]
    # after flying up, mana - h is left for the radius, and the field must
    # reach the nearest of the floor and the three walls
    spare = mana - h
    ok = spare >= h
    corners = [(x, y, 0) for x, y in pts[1:CORNERS + 1]]
    apex = pts[CORNERS + 1] + (top,)
    centre = pts[0] + (h,)
    for i in range(len(corners)):
        a, b = corners[i], corners[i - 1]
        u = [b[j] - a[j] for j in range(len(a))]
        w = [apex[j] - a[j] for j in range(len(a))]
        normal = (u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2],
                  u[0] * w[1] - u[1] * w[0])
        reach = sum(normal[j] * (centre[j] - a[j]) for j in range(len(a)))
        # the distance to the wall is reach / |normal|, compared exactly
        if spare >= 0 and reach * reach <= spare * spare * sum(c * c for c in normal):
            ok = True
    print("YES" if ok and spare >= 0 else "NO")


main()
