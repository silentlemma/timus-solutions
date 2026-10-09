import sys

SIDE_AREA = 9
ENTRANCE_SIDES = 4


def main():
    data = sys.stdin.read().split()
    n, grid = int(data[0]), data[1 : 1 + int(data[0])]
    # visit every empty cell reachable from either entrance; each side of
    # such a cell that faces a block or the outer wall is a visible wall
    seen = {(0, 0), (n - 1, n - 1)}
    stack = list(seen)
    sides = 0
    while stack:
        i, j = stack.pop()
        for a, b in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
            if not (0 <= a < n and 0 <= b < n) or grid[a][b] == "#":
                sides += 1
            elif (a, b) not in seen:
                seen.add((a, b))
                stack.append((a, b))
    # the outer sides of the two entrance cells are openings, not walls
    print((sides - ENTRANCE_SIDES) * SIDE_AREA)


main()
