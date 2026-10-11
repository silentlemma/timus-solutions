import math
from itertools import permutations

EPS = 1e-9  # relative to the size of the tray


def touching(a, ra, b, rb):
    """Centres of a circle of radius r touching circles (a, ra) and (b, rb)
    from outside, given here as ra and rb already increased by r."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    d2 = dx * dx + dy * dy
    if d2 == 0:
        return []
    d = math.sqrt(d2)
    x = (d2 + ra * ra - rb * rb) / (2 * d)
    h2 = (ra - x) * (ra + x)
    if h2 < 0:
        return []
    h = math.sqrt(h2)
    mx, my = a[0] + dx * x / d, a[1] + dy * x / d
    return [(mx - dy * h / d, my + dx * h / d), (mx + dy * h / d, my - dx * h / d)]


def main():
    h_side, w_side, *radii = map(int, open(0).read().split())
    tol = EPS * (h_side + w_side)

    def fits(p, r):
        return r - tol <= p[0] <= h_side - r + tol and r - tol <= p[1] <= w_side - r + tol

    def apart(p, r, q, s):
        return math.hypot(p[0] - q[0], p[1] - q[1]) >= r + s - tol

    def candidates(r, placed):
        xs, ys = (r, h_side - r), (r, w_side - r)
        out = [(x, y) for x in xs for y in ys]  # the four corners
        for q, s in placed:
            for x in xs:  # against a side wall and a placed plate
                t = (s + r) ** 2 - (x - q[0]) ** 2
                if t >= 0:
                    out += [(x, q[1] - math.sqrt(t)), (x, q[1] + math.sqrt(t))]
            for y in ys:
                t = (s + r) ** 2 - (y - q[1]) ** 2
                if t >= 0:
                    out += [(q[0] - math.sqrt(t), y), (q[0] + math.sqrt(t), y)]
        for i in range(len(placed)):  # against two placed plates
            for j in range(i):
                (a, ra), (b, rb) = placed[i], placed[j]
                out += touching(a, ra + r, b, rb + r)
        return out

    def place(order, placed):
        if len(placed) == len(order):
            return placed
        r = radii[order[len(placed)]]
        for p in candidates(r, placed):
            if fits(p, r) and all(apart(p, r, q, s) for q, s in placed):
                done = place(order, placed + [(p, r)])
                if done:
                    return done
        return None

    # pushing every plate down and to the left as far as it goes leaves each
    # one held by two walls or plates placed before it, so some order of the
    # plates and some choice of two such supports finds a placement
    for order in permutations(range(len(radii))):
        done = place(order, [])
        if done:
            where = [None] * len(radii)
            for k, (p, _) in zip(order, done):
                where[k] = p
            print(" ".join("%.4f %.4f" % p for p in where))
            return
    print(0)


main()
