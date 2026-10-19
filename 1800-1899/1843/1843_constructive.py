import sys

FACES = "FBDULR"  # front, back, down, up, left, right: face 2a + side on axis a
AXES = len(FACES) // 2
AXIS_SUM = sum(range(AXES))  # the axis other than a and b is AXIS_SUM - a - b
INSIDE = "."
# quarter turns about the vertical and the front-back axis: the face at
# each letter's place comes from the place of the next letter, cyclically
QUARTER_TURNS = ("FLBR", "DLUR")


def rotations():
    # a rotation p puts the old face p[k] at place k; the two quarter turns
    # generate all 24
    turns = []
    for cycle in QUARTER_TURNS:
        p = list(range(len(FACES)))
        for x, y in zip(cycle, cycle[1:] + cycle[0]):
            p[FACES.index(x)] = FACES.index(y)
        turns.append(p)
    seen = {tuple(range(len(FACES)))}
    todo = list(seen)
    while todo:
        p = todo.pop()
        for q in turns:
            r = tuple(p[q[k]] for k in range(len(FACES)))
            if r not in seen:
                seen.add(r)
                todo.append(r)
    return sorted(seen)


def turned(p, dims, colors):
    return (tuple(dims[p[2 * a] // 2] for a in range(AXES)),
            "".join(colors[p[k]] for k in range(len(FACES))))


def main():
    tokens = iter(sys.stdin.read().split())
    [next(tokens) for _ in range(AXES)]
    box = next(tokens)
    n = int(next(tokens))
    pieces = []
    for _ in range(n):
        dims = [int(next(tokens)) for _ in range(AXES)]
        pieces.append((dims, next(tokens)))
    turns = rotations()

    def sections(axis):
        # the pieces on the edge along an axis carry the two box colours of
        # the faces before it on the other axes; their remaining extents are
        # the sections, the first one also coloured like the start face
        a, b = [k for k in range(AXES) if k != axis]
        first, middle, last = [], [], []
        for dims, colors in pieces:
            if box[2 * a] in colors and box[2 * b] in colors:
                other = AXIS_SUM - colors.index(box[2 * a]) // 2 - colors.index(box[2 * b]) // 2
                if box[2 * axis] in colors:
                    first.append(dims[other])
                elif box[2 * axis + 1] in colors:
                    last.append(dims[other])
                else:
                    middle.append(dims[other])
        return first + middle + last

    cuts = [sections(axis) for axis in range(AXES)]
    # middle sections may come in any order: the pieces are the same
    groups = {}
    for i, (dims, colors) in enumerate(pieces):
        key = min(turned(p, dims, colors) for p in turns)
        groups.setdefault(key, []).append(i)
    answer = [None] * n
    corner = [0] * AXES
    for i, front in enumerate(cuts[0]):
        corner[1] = 0
        for j, down in enumerate(cuts[1]):
            corner[2] = 0
            for k, left in enumerate(cuts[2]):
                place = [i, j, k]
                colors = ""
                for axis in range(AXES):
                    end = len(cuts[axis]) - 1
                    colors += box[2 * axis] if place[axis] == 0 else INSIDE
                    colors += box[2 * axis + 1] if place[axis] == end else INSIDE
                want = ((front, down, left), colors)
                piece = groups[min(turned(p, *want) for p in turns)].pop()
                for p in turns:
                    if turned(p, *pieces[piece]) == want:
                        answer[piece] = "%s %s %d %d %d" % (
                            FACES[p[0]], FACES[p[2]], corner[0], corner[1], corner[2])
                        break
                corner[2] += left
            corner[1] += down
        corner[0] += front
    print("\n".join(answer))


main()
