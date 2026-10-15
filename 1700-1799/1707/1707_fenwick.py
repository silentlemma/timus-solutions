import sys
from array import array

MOD = 200904040963  # the modulus of the hash printed for long experiments
BASE = 7
SHORT = 20  # experiments up to this length are printed digit by digit
CORNERS = 4
OPPOSITE = 3  # the corner (a - 1, c - 1) among the four of a step
LAW = 5  # numbers describing a law
EXPERIMENT = 9  # numbers describing an experiment


def by_row(xs, ys, n):
    # counting sort of the indices by row, kept in compact arrays
    start = array("i", [0]) * (n + 1)
    for y in ys:
        start[y + 1] += 1
    for y in range(n):
        start[y + 1] += start[y]
    order = array("i", [0]) * len(ys)
    fill = array("i", start)
    for i, y in enumerate(ys):
        order[fill[y]] = i
        fill[y] += 1
    return start, order


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    pos = 2
    # the eyes' states are points (s, t); an experiment step asks whether a
    # rectangle holds one, answered by four prefix counts of a sweep over t
    point_x, point_y = array("i"), array("i")
    for _ in range(m):
        s0, t0, ds, dt, k = (int(w) for w in data[pos:pos + LAW])
        pos += LAW
        for i in range(k):
            point_x.append((s0 + i * ds) % n)
            point_y.append((t0 + i * dt) % n)
    p = int(data[pos])
    pos += 1
    # corner 4j + r of the steps in input order; a corner outside the grid
    # sits at row -1, is never asked and keeps the count 0
    ask_x, ask_y = array("i"), array("i")
    lengths = []
    for _ in range(p):
        a0, b0, c0, d0, da, db, dc, dd, q = (int(w) for w in data[pos:pos + EXPERIMENT])
        pos += EXPERIMENT
        lengths.append(q)
        for j in range(q):
            a, b = (a0 + j * da) % n, (b0 + j * db) % n
            c, d = (c0 + j * dc) % n, (d0 + j * dd) % n
            if a > b:
                a, b = b, a
            if c > d:
                c, d = d, c
            for x, y in ((b, d), (a - 1, d), (b, c - 1), (a - 1, c - 1)):
                ask_x.append(x)
                ask_y.append(y if x >= 0 else -1)
    point_start, point_order = by_row(point_x, point_y, n)
    shifted = array("i", (y + 1 for y in ask_y))
    ask_start, ask_order = by_row(ask_x, shifted, n + 1)
    below = array("i", [0]) * len(ask_x)  # points with s <= x and t <= y per corner
    tree = array("i", [0]) * (n + 1)
    for y in range(n):
        for r in range(point_start[y], point_start[y + 1]):
            i = point_x[point_order[r]] + 1
            while i <= n:
                tree[i] += 1
                i += i & -i
        for r in range(ask_start[y + 1], ask_start[y + 2]):
            corner = ask_order[r]
            i = ask_x[corner] + 1
            total = 0
            while i > 0:
                total += tree[i]
                i -= i & -i
            below[corner] = total
    out = []
    first = 0
    for q in lengths:
        bits = []
        for j in range(first, first + q * CORNERS, CORNERS):
            inside = below[j] - below[j + 1] - below[j + 2] + below[j + OPPOSITE]
            bits.append(1 if inside > 0 else 0)
        first += q * CORNERS
        if q <= SHORT:
            out.append("".join(map(str, bits)))
        else:
            value = 0
            for bit in reversed(bits):
                value = (value * BASE + bit) % MOD
            out.append(str(value))
    print("\n".join(out))


main()
