"""Checker: every piece is turned so that the named faces become the
front and the bottom, and moved to the given corner. The pieces must fill
the box without overlapping, every face lying on the surface of the box
must have the colour of that side, and every other face must be inner."""

import sys

FACES = "FBDULR"


class Bad(Exception):
    pass


def rotations():
    turns = ((4, 5, 2, 3, 1, 0), (0, 1, 4, 5, 3, 2))
    seen = {tuple(range(len(FACES)))}
    todo = list(seen)
    while todo:
        p = todo.pop()
        for q in turns:
            r = tuple(p[q[k]] for k in range(len(FACES)))
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return seen


def check(source, expected, output):
    data = open(source).read().split()
    size = [int(v) for v in data[0:3]]
    box = data[3]
    n = int(data[4])
    turns = {(p[0], p[2]): p for p in rotations()}
    got = open(output).read().split()
    if len(got) != 5 * n:
        raise Bad("expected %d lines of five fields" % n)
    placed = []
    volume = 0
    for i in range(n):
        at = 5 + 4 * i
        dims = [int(v) for v in data[at:at + 3]]
        colors = data[at + 3]
        front, down = got[5 * i], got[5 * i + 1]
        if front not in FACES or down not in FACES:
            raise Bad("piece %d: unknown face" % (i + 1))
        p = turns.get((FACES.index(front), FACES.index(down)))
        if p is None:
            raise Bad("piece %d: faces %s and %s are opposite or equal" % (i + 1, front, down))
        try:
            corner = [int(v) for v in got[5 * i + 2:5 * i + 5]]
        except ValueError:
            raise Bad("piece %d: bad coordinates" % (i + 1))
        extent = [dims[p[2 * a] // 2] for a in range(3)]
        for a in range(3):
            if corner[a] < 0 or corner[a] + extent[a] > size[a]:
                raise Bad("piece %d sticks out of the box" % (i + 1))
            for side, touches in ((0, corner[a] == 0), (1, corner[a] + extent[a] == size[a])):
                face = colors[p[2 * a + side]]
                if face != (box[2 * a + side] if touches else "."):
                    raise Bad("piece %d: face %s has the wrong colour" % (i + 1, FACES[2 * a + side]))
        volume += extent[0] * extent[1] * extent[2]
        placed.append((corner, extent))
    if volume != size[0] * size[1] * size[2]:
        raise Bad("the pieces do not fill the box")
    placed.sort()
    for i in range(n):
        ci, ei = placed[i]
        for j in range(i + 1, n):
            cj, ej = placed[j]
            if cj[0] >= ci[0] + ei[0]:
                break
            if all(cj[a] < ci[a] + ei[a] and ci[a] < cj[a] + ej[a] for a in range(3)):
                raise Bad("two pieces overlap")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
