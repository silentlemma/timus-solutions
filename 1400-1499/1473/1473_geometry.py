import sys
from functools import cmp_to_key
from math import gcd

CAMEL = 1
FIELDS = 3  # A, B and the kind


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    kind = {}  # a ray from the origin, reduced by the gcd, to its animal kind
    for j in range(n):
        a, b, c = (int(x) for x in data[1 + FIELDS * j : 1 + FIELDS * (j + 1)])
        g = gcd(a, b)
        if g == 0:
            print(-1)  # nobody can judge an animal at the origin
            return
        ray = (a // g, b // g)
        if kind.setdefault(ray, c) != c:
            print(-1)  # every expert judges a whole ray alike
            return

    # rays by angle, counterclockwise from the A axis
    rays = sorted(kind, key=cmp_to_key(lambda p, q: p[1] * q[0] - p[0] * q[1]))
    experts = []
    for p, q in zip(rays, rays[1:]):
        if kind[p] == kind[q]:
            continue
        # a line along p + q passes strictly between the two rays
        x, y = p[0] + q[0], p[1] + q[1]
        g = gcd(x, y)
        x, y = x // g, y // g
        experts.append((y, -x) if kind[p] == CAMEL else (-y, x))
    if len(experts) % 2 == 0:
        # an odd count avoids ties; one more expert votes for the first kind
        experts.append((1, 1) if kind[rays[0]] == CAMEL else (-1, -1))
    out = [str(len(experts))] + ["%d %d" % e for e in experts]
    sys.stdout.write("\n".join(out) + "\n")


main()
