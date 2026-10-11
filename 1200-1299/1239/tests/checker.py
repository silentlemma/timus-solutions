"""Checker: the count must match the reference, the numbers must be that
many distinct ghosts, and one ray from the origin must touch all of them.
The ray is searched with 50-digit decimals among the directions to the
listed centres and the points where two of their outlines meet."""

import sys
from decimal import Decimal, getcontext

getcontext().prec = 50
TOL = Decimal("1e-30")
FIELDS = 4


def common_ray(ghosts):
    centres = [tuple(Decimal(v) for v in g[:3]) for g in ghosts]
    norm2 = [x * x + y * y + z * z for x, y, z in centres]
    tan = [(m - Decimal(g[-1]) ** 2).sqrt() for m, g in zip(norm2, ghosts)]

    def all_touched(d):
        length = (d[0] ** 2 + d[1] ** 2 + d[2] ** 2).sqrt()
        for c, t, m in zip(centres, tan, norm2):
            gap = d[0] * c[0] + d[1] * c[1] + d[2] * c[2] - t * length
            if gap < -TOL * length * m.sqrt():
                return False
        return True

    if not ghosts or any(all_touched(c) for c in centres):
        return True
    for i, ci in enumerate(centres):
        for j in range(i + 1, len(centres)):
            cj = centres[j]
            g = sum(a * b for a, b in zip(ci, cj))
            det = norm2[i] * norm2[j] - g * g
            if det == 0:
                continue
            a = (tan[i] * norm2[j] - tan[j] * g) / det
            b = (tan[j] * norm2[i] - tan[i] * g) / det
            p = [a * u + b * v for u, v in zip(ci, cj)]
            rest = 1 - sum(t * t for t in p)
            if rest < -TOL:
                continue
            c = (max(rest, Decimal(0)) / det).sqrt()
            cross = (
                ci[1] * cj[2] - ci[2] * cj[1],
                ci[2] * cj[0] - ci[0] * cj[2],
                ci[0] * cj[1] - ci[1] * cj[0],
            )
            for s in (1, -1):
                if all_touched([pt + s * c * cr for pt, cr in zip(p, cross)]):
                    return True
    return False


def main():
    inp, ans, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n = data[0]
    ghosts = [data[1 + FIELDS * i : 1 + FIELDS * (i + 1)] for i in range(n)]
    want = int(open(ans).read().split()[0])
    tokens = open(output).read().split()
    try:
        values = [int(t) for t in tokens]
    except ValueError:
        print("not integers")
        sys.exit(1)
    if not values or values[0] != want:
        print("expected %d ghosts" % want)
        sys.exit(1)
    ids = values[1:]
    if len(ids) != want or len(set(ids)) != want or any(not 1 <= k <= n for k in ids):
        print("expected %d distinct ghost numbers" % want)
        sys.exit(1)
    if not common_ray([ghosts[k - 1] for k in ids]):
        print("no single ray touches all the listed ghosts")
        sys.exit(1)


if __name__ == "__main__":
    main()
