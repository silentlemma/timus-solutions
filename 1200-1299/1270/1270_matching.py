import sys

FACES = 6
COORDS = 3  # the cell's place does not matter

# faces in the input order: front, up, right, down, left, back; a turn p
# gives face f the colour of face p[f]; SPIN turns the cube about the
# vertical axis, TIP about the left-right one
SPIN = (2, 1, 5, 3, 0, 4)
TIP = (1, 5, 2, 0, 4, 3)


def rotations():
    """All 24 rotations of a cube, from two quarter turns."""
    found, queue = {tuple(range(FACES))}, [tuple(range(FACES))]
    for p in queue:
        for g in (SPIN, TIP):
            q = tuple(p[g[f]] for f in range(FACES))
            if q not in found:
                found.add(q)
                queue.append(q)
    return queue


def main():
    nums = map(int, sys.stdin.read().split())
    n = next(nums)
    cubes = [[next(nums) for _ in range(FACES)] for _ in range(n)]
    m = next(nums)
    turns = rotations()
    # fits[j]: the cubes that can stand in cell j, turned somehow
    fits = []
    for _ in range(m):
        need = [next(nums) for _ in range(COORDS + FACES)][COORDS:]
        fits.append(
            [
                i
                for i in range(n)
                if any(
                    all(c == 0 or c == cubes[i][p[f]] for f, c in enumerate(need)) for p in turns
                )
            ]
        )
    # Kuhn's augmenting paths from every cell
    owner = [-1] * n

    def augment(j, seen):
        for i in fits[j]:
            if not seen[i]:
                seen[i] = True
                if owner[i] < 0 or augment(owner[i], seen):
                    owner[i] = j
                    return True
        return False

    for j in range(m):
        if not augment(j, [False] * n):
            print(0)
            return
    cube_of = [0] * m
    for i, j in enumerate(owner):
        if j >= 0:
            cube_of[j] = i + 1
    print("\n".join(map(str, cube_of)))


main()
