"""Validate every move and independently find the shortest distance."""

from collections import deque
import sys

MAX_SIDE = 50
COORDINATES = 3
DIRECTIONS = {
    "north": (-1, 0),
    "east": (0, 1),
    "south": (1, 0),
    "west": (0, -1),
}
KINDS = ("walk", "jump", "drop", "climb")


class Bad(Exception):
    pass


class Maze:
    def __init__(self, a, b, h, rows):
        self.a, self.b, self.h = a, b, h
        self.rows = rows

    def empty(self, x, y, z):
        return (
            0 <= x < self.a
            and 0 <= y < self.b
            and 0 <= z < self.h
            and self.rows[z * self.a + x][y] == "."
        )

    def standing(self, x, y, z):
        return self.empty(x, y, z) and (z == 0 or not self.empty(x, y, z - 1))

    def advance(self, point, kind, direction):
        x, y, z = point
        dx, dy = DIRECTIONS[direction]
        nx, ny, nz = x + dx, y + dy, z
        if kind == "jump":
            if not self.empty(nx, ny, z) or not self.empty(nx, ny, z - 1):
                return None
            nx, ny = x + 2 * dx, y + 2 * dy
        elif kind == "drop":
            if not self.empty(nx, ny, z):
                return None
            nz -= 1
        elif kind == "climb":
            if not self.empty(x, y, z + 1):
                return None
            nz += 1
        if self.standing(nx, ny, nz):
            return nx, ny, nz
        return None

    def moves(self, point):
        for direction in DIRECTIONS:
            for kind in KINDS:
                target = self.advance(point, kind, direction)
                if target is not None:
                    yield target, kind, direction

    def shortest(self, start, goal):
        distance = {start: 0}
        queue = deque([start])
        while queue:
            point = queue.popleft()
            if point == goal:
                return distance[point]
            for target, _, _ in self.moves(point):
                if target not in distance:
                    distance[target] = distance[point] + 1
                    queue.append(target)
        return None


def read_maze(text):
    data = text.split()
    try:
        a, b, h = map(int, data[:COORDINATES])
        if not all(1 <= size <= MAX_SIDE for size in (a, b, h)):
            raise Bad("invalid map dimensions")
        row_end = COORDINATES + a * h
        rows = data[COORDINATES:row_end]
        if len(data) != row_end + 2 * COORDINATES:
            raise Bad("invalid input length")
        if any(len(row) != b or set(row) - {".", "#"} for row in rows):
            raise Bad("invalid map rows")
        values = [int(value) - 1 for value in data[row_end:]]
        start = tuple(values[:COORDINATES])
        goal = tuple(values[COORDINATES:])
    except ValueError as error:
        raise Bad("invalid input integer") from error
    maze = Maze(a, b, h, rows)
    if not maze.standing(*start) or not maze.standing(*goal):
        raise Bad("an endpoint is not an empty cell above the floor")
    return maze, start, goal


def check(source, expected, output):
    del expected
    with open(source, encoding="utf-8") as stream:
        maze, start, goal = read_maze(stream.read())
    with open(output, encoding="utf-8") as stream:
        got = stream.read().split()
    shortest = maze.shortest(start, goal)
    if got == ["NO"]:
        if shortest is not None:
            raise Bad("a route exists")
        return
    if len(got) < 2 or got[0] != "YES":
        raise Bad("expected NO or YES followed by a move count")
    try:
        count = int(got[1])
    except ValueError as error:
        raise Bad("invalid move count") from error
    if count < 0 or count > maze.a * maze.b * maze.h:
        raise Bad("move count is outside its possible range")
    if len(got) != 2 + 2 * count:
        raise Bad("wrong number of moves or extra output")
    if shortest is None:
        raise Bad("the destination is unreachable")
    if count != shortest:
        raise Bad("the move count is not minimal")
    point = start
    for step in range(count):
        kind, direction = got[2 + 2 * step : 2 + 2 * (step + 1)]
        if kind not in KINDS or direction not in DIRECTIONS:
            raise Bad("unknown move at step %d" % (step + 1))
        point = maze.advance(point, kind, direction)
        if point is None:
            raise Bad("illegal move at step %d" % (step + 1))
    if point != goal:
        raise Bad("the route does not end at the destination")


def main():
    try:
        if len(sys.argv) != 1 + COORDINATES:
            raise Bad("usage: checker.py input expected output")
        check(*sys.argv[1:])
    except (Bad, OSError, UnicodeError) as error:
        print(error)
        sys.exit(1)


if __name__ == "__main__":
    main()
