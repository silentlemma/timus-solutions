import sys
from collections import deque

SIDES = 6
HEADER = 6  # X, Y, A, B, C and D
TOP, BOTTOM, NORTH, SOUTH, EAST, WEST = range(SIDES)

# a roll moves every face to a new side; only the side that holds the
# starting top face matters, so each roll is a map from side to side
ROLLS = (
    (1, 0, {TOP: EAST, EAST: BOTTOM, BOTTOM: WEST, WEST: TOP}),
    (-1, 0, {TOP: WEST, WEST: BOTTOM, BOTTOM: EAST, EAST: TOP}),
    (0, 1, {TOP: NORTH, NORTH: BOTTOM, BOTTOM: SOUTH, SOUTH: TOP}),
    (0, -1, {TOP: SOUTH, SOUTH: BOTTOM, BOTTOM: NORTH, NORTH: TOP}),
)


def main():
    words = sys.stdin.read().split()
    width, height, a, b, c, d = (int(w) for w in words[:HEADER])
    walls = set()
    kind = None
    rest = iter(words[HEADER:])
    for word in rest:
        if word in ("v", "h"):
            kind = word
            continue
        n, m = int(word), int(next(rest))
        # a v wall stands between (n, m) and (n + 1, m), an h wall between
        # (n, m) and (n, m + 1), and each blocks the move both ways
        other = (n + 1, m) if kind == "v" else (n, m + 1)
        walls.add(((n, m), other))
        walls.add((other, (n, m)))
    start = (a, b, TOP)
    dist = {start: 0}
    queue = deque([start])
    while queue:
        state = queue.popleft()
        x, y, side = state
        if state == (c, d, TOP):
            print(dist[state])
            return
        for dx, dy, turn in ROLLS:
            nx, ny = x + dx, y + dy
            if not (1 <= nx <= width and 1 <= ny <= height) or ((x, y), (nx, ny)) in walls:
                continue
            nxt = (nx, ny, turn.get(side, side))
            if nxt not in dist:
                dist[nxt] = dist[state] + 1
                queue.append(nxt)
    print("No solution")


main()
