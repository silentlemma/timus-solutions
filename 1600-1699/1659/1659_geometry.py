import sys

CORNERS = 3
INNER = 0.5  # inner points go this share of the way from the centre to a vertex
OUTER = 1 + INNER  # outer points go this far the opposite way


def main():
    v = [float(w) for w in sys.stdin.read().split()]
    corners = [(v[2 * i], v[2 * i + 1]) for i in range(CORNERS)]
    gx = sum(x for x, _ in corners) / CORNERS
    gy = sum(y for _, y in corners) / CORNERS
    out = []
    for k in (INNER, -OUTER):
        for x, y in corners:
            out.append("%.10f %.10f" % (gx + (x - gx) * k, gy + (y - gy) * k))
    print("\n".join(out))


main()
