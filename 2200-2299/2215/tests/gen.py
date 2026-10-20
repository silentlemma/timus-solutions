"""Generate deterministic cases: python gen.py MODE SEED.

Modes: 1 small random, 2 sparse random, 3 maximum static, 4 maximum mixed,
5 translation drift, 6 collinear, 7 rotations only, 8 single city,
9 maximum grid with repeated query edges and gaps between coordinates.
"""

import random
import sys

MAX_SIZE = 40_000
COORD_LIMIT = 10**9
SMALL_SIZE = 50
SMALL_EVENTS = 100
SMALL_COORD = 20
MEDIUM_SIZE = 500
MEDIUM_EVENTS = 700
WIDE_COORD = COORD_LIMIT // 10
PIVOT_RANGE = 100_000
TURN_COUNT = 4
THREE_QUARTERS = TURN_COUNT - 1
ROTATIONS = ("r90", "r180", "r270")
TURNS = dict(zip(ROTATIONS, (1, 2, THREE_QUARTERS)))
SMALL = 1
SPARSE = 2
STATIC = 3
MIXED = 4
DRIFT = 5
AXIS = 6
NO_RAIN = 7
SINGLE = 8
GRID = 9


def grid(rng):
    points = [(2 * x, 2 * y) for x in range(-100, 100) for y in range(-100, 100)]
    rng.shuffle(points)
    rectangles = (
        (-201, -201, 199, 199),
        (-200, -200, -200, 198),
        (-199, -200, -199, 198),
        (-198, -198, 196, 196),
        (-200, -200, -198, -198),
        (-199, -199, -197, -197),
        (-1, -201, 1, 199),
        (-201, -1, 199, 1),
        (-200, 198, 198, 198),
        (-201, -201, -201, 199),
        (198, -200, 198, 198),
        (199, -200, 199, 198),
        (-200, -200, 198, 198),
    )
    rotations = {10_000: "r90 1 -2", 20_000: "r180 -3 4", 30_000: "r270 5 -6"}
    output = [str(MAX_SIZE)]
    output.extend(f"{x} {y}" for x, y in points)
    output.append(str(MAX_SIZE))
    for i in range(MAX_SIZE):
        if i in rotations:
            output.append(rotations[i])
        else:
            output.append("ask " + " ".join(map(str, rng.choice(rectangles))))
    sys.stdout.write("\n".join(output) + "\n")


def main():
    mode, seed = map(int, sys.argv[1:])
    if not SMALL <= mode <= GRID:
        raise SystemExit("mode must be between 1 and 9")
    rng = random.Random(seed)
    if mode == GRID:
        grid(rng)
        return
    if mode == SMALL:
        n, q, span = rng.randint(1, SMALL_SIZE), rng.randint(1, SMALL_EVENTS), SMALL_COORD
    elif mode == SPARSE:
        n, q, span = MEDIUM_SIZE, MEDIUM_EVENTS, COORD_LIMIT
    elif mode == SINGLE:
        n, q, span = 1, MAX_SIZE, WIDE_COORD
    else:
        n, q, span = MAX_SIZE, MAX_SIZE, WIDE_COORD

    if mode == AXIS:
        points = [(0, y - n // 2) for y in range(n)]
    else:
        points_set = set()
        while len(points_set) < n:
            points_set.add((rng.randint(-span, span), rng.randint(-span, span)))
        points = sorted(points_set)
        rng.shuffle(points)

    # Following one city lets queries hit transformed boundaries without moving all cities.
    witness_x, witness_y = points[0]
    events = []

    def rotate(command, x, y):
        nonlocal witness_x, witness_y
        dx, dy = witness_x - x, witness_y - y
        for _ in range(TURNS[command]):
            dx, dy = -dy, dx
        witness_x, witness_y = x + dx, y + dy
        events.append(f"{command} {x} {y}")

    def ask():
        if abs(witness_x) <= COORD_LIMIT and abs(witness_y) <= COORD_LIMIT:
            if rng.randrange(2) == 0:
                width = rng.choice((0, 1, span))
                height = rng.choice((0, 1, span))
                x1 = max(-COORD_LIMIT, witness_x - width)
                y1 = max(-COORD_LIMIT, witness_y - height)
                x2 = min(COORD_LIMIT, witness_x + width)
                y2 = min(COORD_LIMIT, witness_y + height)
                events.append(f"ask {x1} {y1} {x2} {y2}")
                return
        x1, x2 = sorted((rng.randint(-span, span), rng.randint(-span, span)))
        y1, y2 = sorted((rng.randint(-span, span), rng.randint(-span, span)))
        events.append(f"ask {x1} {y1} {x2} {y2}")

    if mode == DRIFT:
        # Each pair adds a translation; reverse pairs bring every city back.
        stages = q // (2 * THREE_QUARTERS)
        for direction in (1, -1):
            for _ in range(stages):
                rotate("r180", -direction * COORD_LIMIT, -direction * COORD_LIMIT)
                rotate("r180", direction * COORD_LIMIT, direction * COORD_LIMIT)
                ask()
        while len(events) < q:
            ask()
    else:
        for i in range(q):
            if mode == STATIC or (mode != NO_RAIN and (i == q - 1 or rng.randrange(2) == 0)):
                ask()
            else:
                pivot_span = SMALL_COORD if mode == SMALL else PIVOT_RANGE
                rotate(
                    rng.choice(ROTATIONS),
                    rng.randint(-pivot_span, pivot_span),
                    rng.randint(-pivot_span, pivot_span),
                )
    output = [str(n)]
    output.extend(f"{x} {y}" for x, y in points)
    output.append(str(q))
    output.extend(events)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()
