import sys

FIELDS = 5  # R, x1, y1, x2, y2


def same_side(r, x1, y1, x2, y2):
    """Whether one side of some inscribed square passes through both
    points: a side lies on a line at distance R / sqrt(2) from the centre,
    and the disc cuts exactly the side out of that line."""
    if (x1, y1) == (x2, y2):
        return 2 * (x1 * x1 + y1 * y1) >= r * r
    cross = x1 * y2 - y1 * x2
    dx, dy = x1 - x2, y1 - y2
    return 2 * cross * cross == r * r * (dx * dx + dy * dy)


def main():
    data = [int(w) for w in sys.stdin.buffer.read().split()]
    t = data[0]
    out = []
    for i in range(t):
        r, x1, y1, x2, y2 = data[1 + FIELDS * i:1 + FIELDS * (i + 1)]
        # the second point on the same, the opposite or an adjacent side:
        # turning it by 0, 180, 90 or -90 degrees brings it onto the first one's side
        turns = ((x2, y2), (-x2, -y2), (-y2, x2), (y2, -x2))
        ok = any(same_side(r, x1, y1, x, y) for x, y in turns)
        out.append("YES" if ok else "NO")
    print("\n".join(out))


main()
