"""A harbour, the tanker, the goal and up to 40 ships: a seed and a mode.
Triangles are drawn at random and kept only if they do not overlap the
ones already placed (touching is allowed). Mode 1 uses a 20 x 20
harbour, mode 2 a 1000 x 1000 one with 40 ships, mode 3 coordinates up
to 10^8 with long thin ships, mode 4 a wall of ships across a small
harbour with gaps about as wide as the tanker. Mode 5 places 40 random
ships in disjoint cells of a 99999999 x 99999999 harbour, with a large
tanker travelling from the bottom right to the top left."""

import random
import sys

SHIPS = 40


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def overlap(s, t):
    """Whether two triangles share interior points: no edge separates them."""
    for p, q in ((s, t), (t, s)):
        for i in range(3):
            a, b = p[i], p[(i + 1) % 3]
            side = cross(a, b, p[(i + 2) % 3])
            if all(cross(a, b, v) * side <= 0 for v in q):
                return False
    return True


def triangle(rng, w, h, size):
    while True:
        x, y = rng.randint(0, w), rng.randint(0, h)
        tri = [(x, y)] + [
            (
                min(max(x + rng.randint(-size, size), 0), w),
                min(max(y + rng.randint(-size, size), 0), h),
            )
            for _ in range(2)
        ]
        if cross(*tri) != 0:
            return tri


def largest_harbour(rng):
    limit = 10**8 - 1
    tanker = [(limit - 1, 1), (limit - 1000001, 1), (limit - 1, 2000001)]
    goal = (1000000, limit - 2000000)
    ships = []
    for row in range(5):
        for col in range(8):
            x0, y0 = 4000000 + col * 11500000, 5000000 + row * 18000000
            while True:
                ship = [(x0 + rng.randint(0, 6000000), y0 + rng.randint(0, 10000000))
                        for _ in range(3)]
                if cross(*ship) != 0:
                    ships.append(ship)
                    break
    out = [f"{limit} {limit}"] + [f"{x} {y}" for x, y in tanker + [goal]]
    out.append(str(len(ships)))
    out += [f"{x} {y}" for ship in ships for x, y in ship]
    return "\n".join(out) + "\n"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 5:
        sys.stdout.write(largest_harbour(rng))
        return
    w, h, size, count = {
        1: (20, 20, 6, 8),
        2: (1000, 1000, 120, SHIPS),
        3: (10**8, 10**8, 10**8, 12),
    }.get(mode, (60, 60, 8, 0))
    placed = []
    tanker = triangle(rng, w, h, size)
    placed.append(tanker)
    if mode == 4:
        # a row of ships across the middle with random gaps
        x = 0
        while x < w and len(placed) <= SHIPS:
            width = rng.randint(3, 9)
            ship = [(x, 30), (min(x + width, w), 30), (x + width // 2, 30 + rng.randint(1, 6))]
            if cross(*ship) != 0 and not any(overlap(ship, t) for t in placed):
                placed.append(ship)
            x += width + rng.randint(0, 6)
    tries = 0
    while len(placed) <= count and tries < 20000:
        tries += 1
        ship = triangle(rng, w, h, size)
        if not any(overlap(ship, t) for t in placed):
            placed.append(ship)
    # a goal where the tanker fits, if one turns up soon
    ax, ay = tanker[0]
    for _ in range(1000):
        goal = (rng.randint(0, w), rng.randint(0, h))
        moved = [(x - ax + goal[0], y - ay + goal[1]) for x, y in tanker]
        inside = all(0 <= x <= w and 0 <= y <= h for x, y in moved)
        if inside and not any(overlap(moved, t) for t in placed[1:]):
            break
    out = ["%d %d" % (w, h)] + ["%d %d" % p for p in tanker] + ["%d %d" % goal]
    out.append("%d" % (len(placed) - 1))
    out += ["%d %d" % p for ship in placed[1:] for p in ship]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
