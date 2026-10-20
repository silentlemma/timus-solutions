"""Generate only valid maps with a unique shortest route, or no route."""

from collections import deque
import random
import sys

from checker import Maze, MAX_SIDE

SMALL_SIDE = 6
MIN_TERRAIN = 12
MAX_TERRAIN_HEIGHT = 8
WALL_DENOMINATOR = 10
WALL_THRESHOLD = 4
MAX_ATTEMPTS = 10000
RANDOM_MODE = 1
TERRAIN_MODE = 2
CORRIDOR_MODE = 3
SNAKE_MODE = 4
LAYERS_MODE = 5
SAME_MODE = 6
STAIR_ROW = 4
DIMENSIONS = 3


def unique(maze, start, goal):
    distance = {start: 0}
    ways = {start: 1}
    queue = deque([start])
    while queue:
        point = queue.popleft()
        if point == goal:
            return ways[point] == 1
        for target, _, _ in maze.moves(point):
            candidate = distance[point] + 1
            if target not in distance:
                distance[target] = candidate
                ways[target] = ways[point]
                queue.append(target)
            elif distance[target] == candidate:
                ways[target] = min(2, ways[target] + ways[point])
    return True


def random_map(rng, seed):
    for _ in range(MAX_ATTEMPTS):
        a, b, h = (rng.randint(1, SMALL_SIDE) for _ in range(DIMENSIONS))
        rows = [
            "".join(
                "#" if rng.randrange(WALL_DENOMINATOR) < WALL_THRESHOLD else "." for _ in range(b)
            )
            for _ in range(a * h)
        ]
        maze = Maze(a, b, h, rows)
        points = [
            (x, y, z)
            for z in range(h)
            for x in range(a)
            for y in range(b)
            if maze.standing(x, y, z)
        ]
        if len(points) < 2:
            continue
        start, goal = rng.sample(points, 2)
        if seed % DIMENSIONS and maze.shortest(start, goal) is None:
            continue
        if unique(maze, start, goal):
            return maze, start, goal
    raise RuntimeError("could not generate a unique random route")


def terrain(rng):
    for _ in range(MAX_ATTEMPTS):
        length = rng.randint(MIN_TERRAIN, MAX_SIDE)
        heights = [rng.randrange(MAX_TERRAIN_HEIGHT)]
        for _ in range(length - 1):
            heights.append(max(0, min(MAX_TERRAIN_HEIGHT - 1, heights[-1] + rng.randint(-1, 1))))
        h = max(heights) + 2
        rows = ["".join("#" if z < floor else "." for floor in heights) for z in range(h)]
        maze = Maze(1, length, h, rows)
        start, goal = (0, 0, heights[0]), (0, length - 1, heights[-1])
        if rng.randrange(2):
            start, goal = goal, start
        if unique(maze, start, goal):
            return maze, start, goal
    raise RuntimeError("could not generate a unique terrain route")


def corridor(rng):
    length = rng.randint(2, MAX_SIDE)
    along_x = rng.randrange(2)
    a, b = (length, 1) if along_x else (1, length)
    h = rng.randint(1, MAX_SIDE)
    rows = ["." * b for _ in range(a)] + ["#" * b for _ in range(a * (h - 1))]
    maze = Maze(a, b, h, rows)
    start, goal = (0, 0, 0), (a - 1, b - 1, 0)
    if rng.randrange(2):
        start, goal = goal, start
    return maze, start, goal


def snake(rng):
    side = MAX_SIDE
    rows = [list("#" * side) for _ in range(side * side)]
    path = []
    for x in range(0, side, 2):
        forward = (x // 2) % 2 == 0
        columns = range(side) if forward else range(side - 1, -1, -1)
        for y in columns:
            rows[x][y] = "."
            path.append((x, y, 0))
        if x + 2 < side:
            y = side - 1 if forward else 0
            rows[x + 1][y] = "."
            path.append((x + 1, y, 0))
    start, goal = path[0], path[-1]
    if rng.randrange(2):
        start, goal = goal, start
    return Maze(side, side, side, ["".join(row) for row in rows]), start, goal


def layers(rng):
    del rng
    side = MAX_SIDE
    rows = [list(("." if z % 2 == 0 else "#") * side) for z in range(side) for _ in range(side)]
    for z in range(1, side - 1, 2):
        y = 1 if (z // 2) % 2 == 0 else STAIR_ROW
        rows[z * side + 1][y] = "."
        rows[z * side + 2][y] = "."
        rows[(z - 1) * side + 2][y] = "#"
    goal = side - 1, side - 1, side - 1
    rows[(side - 1) * side + side - 1][side - 1] = "."
    rows[(side - 2) * side + side - 1][side - 1] = "#"
    maze = Maze(side, side, side, ["".join(row) for row in rows])
    return maze, (0, 0, 0), goal


def same(rng):
    side = MAX_SIDE
    rows = [
        "".join("#" if rng.randrange(2) else "." for _ in range(side)) for _ in range(side * side)
    ]
    rows[0] = "." + rows[0][1:]
    return Maze(side, side, side, rows), (0, 0, 0), (0, 0, 0)


def main():
    if len(sys.argv) != DIMENSIONS:
        raise SystemExit("usage: gen.py MODE SEED")
    mode, seed = map(int, sys.argv[1:])
    rng = random.Random(seed)
    if mode == RANDOM_MODE:
        maze, start, goal = random_map(rng, seed)
    else:
        modes = {
            TERRAIN_MODE: terrain,
            CORRIDOR_MODE: corridor,
            SNAKE_MODE: snake,
            LAYERS_MODE: layers,
            SAME_MODE: same,
        }
        if mode not in modes:
            raise SystemExit("unknown generator mode")
        maze, start, goal = modes[mode](rng)
    print(maze.a, maze.b, maze.h)
    print("\n".join(maze.rows))
    print(*(value + 1 for value in start))
    print(*(value + 1 for value in goal))


if __name__ == "__main__":
    main()
