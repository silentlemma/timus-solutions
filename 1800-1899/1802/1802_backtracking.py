import sys

FACES = 6
TURNS = 4


def face_cell(n, face, r, c):
    """The cube cell (y, z, x) under the face at row r, column c, and the
    step (dy, dz, dx) into the cube. Every face is the bottom one turned by
    a rotation of the cube, so no part is ever mirrored."""
    last = n - 1
    starts = [((0, r, c), (1, 0, 0)), ((last, last - r, c), (-1, 0, 0)),
              ((r, last, c), (0, -1, 0)), ((r, 0, last - c), (0, 1, 0)),
              ((r, c, 0), (0, 0, 1)), ((r, last - c, last), (0, 0, -1))]
    return starts[face]


def turn(n, r, c, k):
    for _ in range(k):
        r, c = c, n - 1 - r
    return r, c


def placement(n, heights, face, k):
    """The bit mask of the cells a part fills on a face, turned k times."""
    mask = 0
    for r in range(n):
        for c in range(n):
            h = heights[r][c]
            if h:
                (y, z, x), (dy, dz, dx) = face_cell(n, face, *turn(n, r, c, k))
                for _ in range(h):
                    mask |= 1 << ((y * n + z) * n + x)
                    y, z, x = y + dy, z + dz, x + dx
    return mask


def main():
    data = list(map(int, sys.stdin.read().split()))
    n = data[0]
    cells = n * n
    parts = [[data[1 + p * cells + r * n:1 + p * cells + (r + 1) * n] for r in range(n)]
             for p in range(FACES)]
    volume = [sum(map(sum, part)) for part in parts]
    # options[p][f]: the different masks of part p on face f
    options = [[sorted({placement(n, parts[p][:], f, k) for k in range(TURNS)})
                for f in range(FACES)] for p in range(FACES)]
    # a turn of the whole cube brings the largest part onto face 0 unturned
    anchor = max(range(FACES), key=volume.__getitem__)
    chosen = {anchor: placement(n, parts[anchor], 0, 0)}
    free_faces = set(range(1, FACES))

    def solve(used):
        if not free_faces:
            return True
        # fill next the face with the fewest ways left
        best = None
        for f in free_faces:
            ways = [(p, mask) for p in range(FACES) if p not in chosen
                    for mask in options[p][f] if not mask & used]
            if not ways:
                return False
            if best is None or len(ways) < len(best[1]):
                best = (f, ways)
        face, ways = best
        free_faces.discard(face)
        for p, mask in ways:
            chosen[p] = mask
            if solve(used | mask):
                return True
            del chosen[p]
        free_faces.add(face)
        return False

    if not solve(chosen[anchor]):
        print("No")
        return
    label = [0] * (cells * n)
    for p, mask in chosen.items():
        bit = 0
        while mask:
            if mask & 1:
                label[bit] = p + 1
            mask >>= 1
            bit += 1
    out = ["Yes"]
    for row in range(cells):
        out.append(" ".join(map(str, label[row * n:(row + 1) * n])))
    print("\n".join(out))


main()
