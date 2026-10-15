import math

PHI = (1 + math.sqrt(5)) / 2
TINY = 1e-14
DIM = 3
SAME = 1e-7  # equal edge lengths up to rounding


def unit(v):
    n = math.sqrt(sum(c * c for c in v))
    return tuple(c / n for c in v)


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def apply(m, v):
    return tuple(dot(row, v) for row in m)


def compose(a, b):
    cols = list(zip(*b))
    return [tuple(dot(row, col) for col in cols) for row in a]


def rotation(axis, angle):
    """rotation by angle around axis, right-handed"""
    x, y, z = unit(axis)
    c, s = math.cos(angle), math.sin(angle)
    t = 1 - c
    return [
        (t * x * x + c, t * x * y - s * z, t * x * z + s * y),
        (t * x * y + s * z, t * y * y + c, t * y * z - s * x),
        (t * x * z - s * y, t * y * z + s * x, t * z * z + c),
    ]


def solid(name):
    signs = (-1, 1)
    if name == "tetrahedron":
        pts = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    elif name == "hexahedron":
        pts = [(x, y, z) for x in signs for y in signs for z in signs]
    elif name == "octahedron":
        pts = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
    elif name == "icosahedron":
        pts = []
        for a in signs:
            for b in signs:
                pts += [(0, a, b * PHI), (a, b * PHI, 0), (b * PHI, 0, a)]
    else:  # dodecahedron
        pts = [(x, y, z) for x in signs for y in signs for z in signs]
        for a in signs:
            for b in signs:
                pts += [(0, a / PHI, b * PHI), (a / PHI, b * PHI, 0), (b * PHI, 0, a / PHI)]
    return [unit(p) for p in pts]


def main():
    words = open(0).read().split()
    guns = solid(words[0])
    edge = min(math.dist(a, b) for a in guns for b in guns if a != b)
    # turn the solid so that one gun points along z and a neighbour lies in
    # the half-plane x >= 0 of Oxz; any choice is the same up to symmetry
    top = guns[0]
    near = next(g for g in guns if abs(math.dist(g, top) - edge) < SAME)
    z = top
    x = unit(tuple(n - dot(near, z) * t for n, t in zip(near, z)))
    y = cross(z, x)
    guns = [unit((dot(g, x), dot(g, y), dot(g, z))) for g in guns]
    n = int(words[1])
    turn = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    total = 0.0
    for i in range(n):
        start = 2 + DIM * i
        v = [float(w) for w in words[start : start + DIM]]
        target = unit(tuple(-c for c in v))  # the ship comes from there
        gun = max((apply(turn, g) for g in guns), key=lambda g: dot(g, target))
        angle = math.acos(max(-1.0, min(1.0, dot(gun, target))))
        total += angle
        axis = cross(gun, target)
        if angle > TINY and math.sqrt(dot(axis, axis)) > TINY:
            # the shortest turn: around the axis normal to both directions
            turn = compose(rotation(axis, angle), turn)
    print("%.5f" % total)


main()
