import math
import sys

# Faces: 0 the base, 1..4 the sides clockwise from the one facing +y. On the
# base, side k rests on the edge of corners k - 1 and k % 4; on a side,
# corners 0, 1 are its base corners and corner 2 its apex: (x0, y0, x1, ...).
SIDES = 4
FACES = 5
EPS = 1e-12
NONE = -1e100
BEAM = 200  # states kept per depth by the first, greedy pass (see the README)

EXACT = 8  # rolls for which the bounds are exact
KINDS_WITHIN = 3  # every kind of state appears within this many rolls

TRIANGLE = 3  # corners of a side: its centroid is a third of the way up
START = FACES * FACES  # the key of the starting state
X0, Y0, X1, Y1, X2, Y2, X3, Y3 = range(2 * SIDES)


def can_roll(face, nxt):
    return face != nxt and (face == 0 or nxt == 0 or (face - nxt) % 2 == 1)  # not opposite


def main():
    s, side, x, y, n = sys.stdin.read().split()
    s, side, x, y, n = float(s), float(side), float(x), float(y), int(n)
    t = math.sqrt(side * side - (s / 2) ** 2)
    hypot = math.hypot

    def roll(face, v, cx, cy, nxt):
        """the corners and the centre after rolling from face onto nxt"""
        if face == 0:  # onto side nxt: its apex beyond the edge, away from the centre
            i, j = 2 * (nxt - 1), 2 * (nxt % SIDES)
            ax, ay, bx, by = v[i], v[i + 1], v[j], v[j + 1]
            dx, dy = bx - ax, by - ay
            length = hypot(dx, dy)
            nx, ny = -dy / length, dx / length
            if dx * (cy - ay) - dy * (cx - ax) > 0:
                nx, ny = -nx, -ny
            px, py = (ax + bx) / 2 + nx * t, (ay + by) / 2 + ny * t
            return (ax, ay, bx, by, px, py), (ax + bx + px) / TRIANGLE, (ay + by + py) / TRIANGLE
        if nxt == 0:  # onto the base: the square beyond the edge, away from the apex
            ax, ay, bx, by = v[X0], v[Y0], v[X1], v[Y1]
            dx, dy = bx - ax, by - ay
            length = hypot(dx, dy)
            nx, ny = -dy / length, dx / length
            if dx * (v[Y2] - ay) - dy * (v[X2] - ax) > 0:
                nx, ny = -nx, -ny
            corner = (ax, ay, bx, by, bx + nx * s, by + ny * s, ax + nx * s, ay + ny * s)
            shift = 2 * (SIDES - face + 1)  # corner i goes to slot (face - 1 + i) % 4
            nv = corner[shift:] + corner[:shift]
            return (
                nv,
                (nv[X0] + nv[X1] + nv[X2] + nv[X3]) / SIDES,
                (nv[Y0] + nv[Y1] + nv[Y2] + nv[Y3]) / SIDES,
            )
        # over a lateral edge: clockwise over (corner 1, apex), else over (corner 0, apex)
        cw = nxt == face % SIDES + 1
        ax, ay = (v[X1], v[Y1]) if cw else (v[X0], v[Y0])
        qx, qy = (v[X0], v[Y0]) if cw else (v[X1], v[Y1])
        ex, ey = v[X2], v[Y2]
        dx, dy = ex - ax, ey - ay
        k = ((qx - ax) * dx + (qy - ay) * dy) / (dx * dx + dy * dy)
        px, py = 2 * (ax + k * dx) - qx, 2 * (ay + k * dy) - qy
        nv = (ax, ay, px, py, ex, ey) if cw else (px, py, ax, ay, ex, ey)
        return nv, (ax + px + ex) / TRIANGLE, (ay + py + ey) / TRIANGLE

    half = s / 2
    start = (-half, half, half, half, half, -half, -half, -half)

    # The farthest the centre goes in r rolls ending on the base, by key (previous
    # face * FACES + face): exact up to EXACT rolls, playing every sequence from
    # one state of each kind; beyond, a roll adds at most base_step or side_step.
    kinds = {START: (0, FACES, start, 0.0, 0.0)}
    frontier = [kinds[START]]
    for _ in range(KINDS_WITHIN):
        later = []
        for face, prev, v, cx, cy in frontier:
            for f in range(FACES):
                if f != prev and can_roll(face, f):
                    state = (f, face) + roll(face, v, cx, cy, f)
                    kinds.setdefault(face * FACES + f, state)
                    later.append(state)
        frontier = later
    exact = {}
    for k, (face0, prev0, v0, cx0, cy0) in kinds.items():
        far = [NONE] * (EXACT + 1)
        stack = [(face0, prev0, v0, cx0, cy0, 0)]
        while stack:
            face, prev, v, cx, cy, d = stack.pop()
            if face == 0:
                far[d] = max(far[d], hypot(cx - cx0, cy - cy0))
            if d < EXACT:
                for f in range(FACES):
                    if f != prev and can_roll(face, f):
                        stack.append((f, face) + roll(face, v, cx, cy, f) + (d + 1,))
        for r in range(1, EXACT + 1):
            far[r] = max(far[r], far[r - 1])
        exact[k] = far
    base_step, side_step = s / 2 + t / TRIANGLE, 2 * s * t / (TRIANGLE * side)
    reach = [[NONE] * (n + 1) for _ in range(START + 1)]
    for r in range(n + 1):
        for face in range(FACES):
            for prev in range(FACES + 1):  # prev == FACES: the start
                if (prev == FACES and face) or (prev < FACES and not can_roll(prev, face)):
                    continue
                k = START if prev == FACES else prev * FACES + face
                if r <= EXACT:
                    reach[k][r] = exact[k][r]
                    continue
                u = reach[k][r - 1]
                if face == 0:
                    u = max(u, 0)
                for f in range(FACES):
                    if can_roll(face, f) and f != prev and reach[face * FACES + f][r - 1] > NONE:
                        step = base_step if face == 0 or f == 0 else side_step
                        u = max(u, step + reach[face * FACES + f][r - 1])
                reach[k][r] = u
    # the rolls from a face that came from prev: (next face, its bound by rolls left)
    moves = [
        [
            [(f, reach[face * FACES + f]) for f in range(FACES) if f != prev and can_roll(face, f)]
            for prev in range(FACES + 1)
        ]
        for face in range(FACES)
    ]

    best = [hypot(x, y), 0, [0]]

    def consider(seq, d):
        rolls = len(seq) - 1
        if d + EPS < best[0] or (abs(d - best[0]) <= EPS and rolls < best[1]):
            best[:] = [d, rolls, list(seq)]

    # a first answer: a beam search keeping the states that may get closest
    states = [(0.0, 0, FACES, start, 0.0, 0.0, (0,))]
    for depth in range(n):
        nxt_states = []
        left = n - depth - 1
        for _, face, prev, v, cx, cy, seq in states:
            for f, bound in moves[face][prev]:
                r = bound[left]
                if r <= NONE:
                    continue
                nv, ncx, ncy = roll(face, v, cx, cy, f)
                d = hypot(ncx - x, ncy - y)
                nseq = seq + (f,)
                if f == 0:
                    consider(nseq, d)
                nxt_states.append((max(0.0, d - r), f, face, nv, ncx, ncy, nseq))
        nxt_states.sort(key=lambda e: e[0])
        states = nxt_states[:BEAM]

    seq = [0]

    def search(face, prev, v, cx, cy, depth):
        if face == 0:
            consider(seq, hypot(cx - x, cy - y))
        if depth == n:
            return
        left = n - depth - 1
        best_d = best[0] + EPS
        options = []
        for f, bound in moves[face][prev]:
            u = bound[left]
            if u <= NONE:
                continue
            nv, ncx, ncy = roll(face, v, cx, cy, f)
            dx, dy = ncx - x, ncy - y
            lim = best_d + u
            d2 = dx * dx + dy * dy
            if d2 <= lim * lim:
                options.append((d2, f, nv, ncx, ncy))
        options.sort()  # nearest first
        for _, f, nv, ncx, ncy in options:
            seq.append(f)
            search(f, face, nv, ncx, ncy, depth + 1)
            seq.pop()

    search(0, FACES, start, 0.0, 0.0, 0)
    print("%.3f" % (best[0] + EPS))
    print(best[1])
    print(" ".join(map(str, best[2])))


main()
