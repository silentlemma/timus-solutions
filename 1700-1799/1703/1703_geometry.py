import math
import sys

DIM = 3


def cross(u, v):
    return [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]


def dot(u, v):
    return sum(x * y for x, y in zip(u, v))


def main():
    data = [int(w) for w in sys.stdin.read().split()]
    a, b = data[0], data[1]
    p = data[2:2 + DIM]
    d = [data[2 + DIM + i] - p[i] for i in range(DIM)]
    # the elbow's axis is parallel to the rail and across both segments, so the
    # shoulder, the elbow and the claw lie in the plane through the shoulder
    # across the rail, and the claw sits at the rail's point q nearest to it
    dd = dot(d, d)
    rr_num = dot(cross(p, d), cross(p, d))  # |q|^2 = rr_num / dd, exactly
    # the bend (the angle opposite q) is not acute and the triangle closes:
    # a^2 + b^2 <= |q|^2 <= (a + b)^2
    if not (a * a + b * b) * dd <= rr_num <= (a + b) ** 2 * dd:
        print("No solution.")
        return
    t = -dot(p, d) / dd
    q = [p[i] + t * d[i] for i in range(DIM)]
    r = math.sqrt(rr_num / dd)
    e1 = [x / r for x in q]
    e2 = cross([x / math.sqrt(dd) for x in d], e1)
    # the elbow is at distance a from the shoulder and b from q
    along = (a * a - b * b + r * r) / (2 * r)
    side = math.sqrt(max(0.0, a * a - along * along))
    elbow = [along * e1[i] + side * e2[i] for i in range(DIM)]
    bend = math.acos(max(-1.0, min(1.0, (a * a + b * b - r * r) / (2 * a * b))))
    print(" ".join("%.15f" % x for x in elbow + [bend]))


main()
