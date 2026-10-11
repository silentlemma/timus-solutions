import math

ROLLS = 70
DIRS = 6
TURN = 60  # degrees between neighbouring directions
# a jump through the base in half steps: (1 + sqrt 3) / 2 = 1/2 + sin 60
SIDE = (1 + 2 * math.sin(math.radians(TURN))) / 2
# the six directions of a hexagonal lattice, as integer combinations of
# the first two of them
UNIT = ((1, 0), (0, 1), (-1, 1), (-1, 0), (0, -1), (1, -1))
CLASSES = (0, 90)  # the starting edges at 0 and 180, or at 90 and 270 degrees


def main():
    tx, ty = map(float, input().split())
    best = math.hypot(tx, ty)  # no rolls at all
    for start in CLASSES:
        w = [
            (math.cos(math.radians(start + TURN * k)), math.sin(math.radians(start + TURN * k)))
            for k in range(DIRS)
        ]
        # a state is a triangle lying on the table: twice its apex position
        # (in steps of the base jump) and the direction from the apex to
        # the base edge; it costs one roll to reach from the start
        cost = {}
        buckets = [[] for _ in range(ROLLS + 1)]
        for u in (0, DIRS // 2):
            state = (UNIT[u], (u + DIRS // 2) % DIRS)
            cost[state] = 1
            buckets[1].append(state)
        for c in range(1, ROLLS):
            for state in buckets[c]:
                if cost[state] != c:
                    continue
                (a, b), d = state
                # roll onto the base: its centre is half a step beyond the apex
                ua, ub = UNIT[d]
                x = SIDE * ((a + ua) * w[0][0] + (b + ub) * w[1][0])
                y = SIDE * ((a + ua) * w[0][1] + (b + ub) * w[1][1])
                best = min(best, math.hypot(x - tx, y - ty))
                moves = (
                    ((a, b), (d + 1) % DIRS, 1),  # onto the next side face
                    ((a, b), (d - 1) % DIRS, 1),
                    ((a + 2 * ua, b + 2 * ub), (d + DIRS // 2) % DIRS, 2),  # over the base
                )
                for pos, nd, add in moves:
                    nxt = (pos, nd)
                    if c + add < ROLLS and cost.get(nxt, ROLLS) > c + add:
                        cost[nxt] = c + add
                        buckets[c + add].append(nxt)
    print("%.4f" % best)


main()
