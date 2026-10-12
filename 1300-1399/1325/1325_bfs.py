import sys

WALL = ord("0")
HEADER = 6  # numbers before the plan


def main():
    data = sys.stdin.buffer.read().split()
    n, m = int(data[0]), int(data[1])
    sr, sc, tr, tc = (int(x) for x in data[2:HEADER])
    width = m + 2
    # the plan with a frame of walls, as one flat array
    grid = bytearray([WALL]) * width
    for row in data[HEADER : HEADER + n]:
        grid += bytes([WALL]) + row[:m] + bytes([WALL])
    grid += bytearray([WALL]) * width
    steps = [-1] * len(grid)
    seeded = [-1] * len(grid)  # the layer that last took the cell as a seed
    moves = [dr * width + dc for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc]
    start, target = sr * width + sc, tr * width + tc
    # layer c holds the cells first reached after c changes of shoes, all of
    # the same kind; seeds come in sorted by the number of steps
    kind, changes, seeds = grid[start], 0, [(0, start)]
    while seeds and steps[target] < 0:
        later, i, level, current = [], 0, seeds[0][0], []
        while (i < len(seeds) or current) and steps[target] < 0:
            if not current:
                level = max(level, seeds[i][0])
            while i < len(seeds) and seeds[i][0] == level:
                cell = seeds[i][1]
                i += 1
                if steps[cell] < 0:
                    steps[cell] = level
                    current.append(cell)
            following = []
            for cell in current:
                for move in moves:
                    near = cell + move
                    if steps[near] >= 0 or grid[near] == WALL:
                        continue
                    if grid[near] == kind:
                        steps[near] = level + 1
                        following.append(near)
                    elif seeded[near] != changes:
                        seeded[near] = changes
                        later.append((level + 1, near))
            current = following
            level += 1
        if steps[target] < 0:
            kind, changes, seeds = grid[later[0][1]] if later else kind, changes + 1, later
    if steps[target] < 0:
        print(0, 0)
    else:
        print(steps[target] + 1, changes)


main()
