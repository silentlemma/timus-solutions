import sys

SIDE = 3
CUBES = SIDE ** 3
# the six directions as cell steps in a 3 x 3 x 3 cube numbered x*9 + y*3 + z
STEPS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
NAMES = "RLFBUD"
AXIS = [0, 0, 1, 1, 2, 2]
RIGHT, UP = NAMES.index("R"), NAMES.index("U")


def main():
    snake = sys.stdin.readline().strip()
    cells = [(x, y, z) for x in range(SIDE) for y in range(SIDE) for z in range(SIDE)]
    index = {c: k for k, c in enumerate(cells)}
    near = [[index.get((x + dx, y + dy, z + dz), -1) for dx, dy, dz in STEPS] for x, y, z in cells]
    used = [False] * CUBES
    answer = []

    def connected(left):
        """the free cells must stay one piece for the rest of the snake"""
        start = used.index(False) if left else -1
        if start < 0:
            return True
        seen = {start}
        stack = [start]
        while stack:
            for nxt in near[stack.pop()]:
                if nxt >= 0 and not used[nxt] and nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        return len(seen) == left

    def fold(k, at, way):
        """place cube k + 1 after cube k, which sits at cell at"""
        if k == CUBES - 1:
            return True
        if snake[k] == "F":
            options = [way]  # a straight cube keeps the direction
        else:
            options = [d for d in range(len(STEPS)) if AXIS[d] != AXIS[way]]
        for d in options:
            nxt = near[at][d]
            if nxt < 0 or used[nxt]:
                continue
            used[nxt] = True
            answer.append(NAMES[d])
            if connected(CUBES - 2 - k) and fold(k + 1, nxt, d):
                return True
            answer.pop()
            used[nxt] = False
        return False

    # the cube colours 14 cells one way and 13 the other, and the snake
    # alternates, so it starts on the larger colour: a corner or the centre
    # of a face; up to symmetry that leaves three first moves
    roots = [(index[(0, 0, 0)], RIGHT), (index[(1, 1, 0)], UP), (index[(1, 1, 0)], RIGHT)]
    for start, d in roots:
        nxt = near[start][d]
        used[:] = [False] * CUBES
        used[start] = used[nxt] = True
        answer[:] = [NAMES[d]]
        if connected(CUBES - 2) and fold(1, nxt, d):
            print("".join(answer))
            return
    print("IMPOSSIBLE")


main()
