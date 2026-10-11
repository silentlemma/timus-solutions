"""Rivers: a seed and a mode. Each system is a main river running right
along a horizontal line, with tributaries coming down into its inner
vertices inside their own vertical strips, and side streams flowing
left into inner vertices of a tributary along a horizontal line, so no
two rivers cross. Mode 1 builds one small system with one decimal
place, mode 2 several systems and up to 1000 points with two decimal
places, mode 3 long rivers without tributaries. Mode 4 builds one
1000-point river near a parabola, mode 5 a 1000-point ten-river chain,
and mode 6 a 1000-point main river with nine meandering tributaries.
All modes take a seed followed by the mode number."""

import random
import sys

RIVERS = 10
POINTS = 1000
STRIP = 40


def maximal(seed, mode):
    rng = random.Random(seed)
    if mode == 4:
        xs = sorted(rng.sample(range(-100000, 100001), POINTS))
        rivers = [[(x, x * x // 100000 - 50000) for x in xs]]
    elif mode == 5:
        rows = [-90000 + 18000 * i + rng.randrange(1000) for i in range(RIVERS)]
        rivers = [[(-90000 + 1600 * j, rows[0]) for j in range(100)]]
        for i in range(1, RIVERS):
            river = [(-90000 + 1600 * j, rows[i]) for j in range(i + 98, i - 1, -1)]
            river.append((-90000 + 1600 * i, rows[i - 1]))
            rivers.append(river)
    else:
        rivers = [[(-100000 + 20000 * j, -100000) for j in range(11)]]
        for i in range(9):
            count = 110 if i < 8 else 109
            cx = -80000 + 20000 * i
            ys = sorted(rng.sample(range(1, 190001), count - 1), reverse=True)
            river = [(cx + rng.randrange(-5000, 5001), y - 100000) for y in ys]
            river.append((cx, -100000))
            rivers.append(river)
    rng.shuffle(rivers)

    def fmt(v):
        return ("%.2f" % (v / 100)).rstrip("0").rstrip(".")

    out = [str(len(rivers))]
    for river in rivers:
        out.append(str(len(river)))
        out.extend(fmt(x) + " " + fmt(y) for x, y in river)
    sys.stdout.write("\n".join(out) + "\n")


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    if mode in (4, 5, 6):
        maximal(seed, mode)
        return
    rng = random.Random(seed)
    unit = 0.1 if mode == 1 else 0.01
    rivers = []
    budget = POINTS
    systems = 1 if mode == 1 else rng.randint(1, 3)
    for s in range(systems):
        base_y = -900 + 600 * s
        slots = 0 if mode == 3 else rng.randint(0, (RIVERS - len(rivers)) // (systems - s) - 1)
        if len(rivers) >= RIVERS:
            break
        # the main river: inner vertices every STRIP along the line
        main = [(-990 + STRIP * j, base_y) for j in range(slots + 2)]
        rivers.append(main)
        budget -= len(main)
        free = RIVERS - len(rivers)
        for j in range(1, slots + 1):
            if free <= 0:
                break
            cx = main[j][0]
            steps = rng.randint(2, max(2, min(80, budget // (2 * RIVERS))))
            # down to the mouth, with x wandering inside the strip
            ys = sorted(rng.sample(range(1, 4000), steps), reverse=True)
            trib = [
                (round(cx + rng.uniform(-STRIP / 4, STRIP / 4), 2), base_y + y * 0.1) for y in ys
            ]
            trib.append((cx, base_y))
            trib = [(round(x / unit) * unit, round(y / unit) * unit) for x, y in trib[:-1]] + [
                trib[-1]
            ]
            rivers.append(trib)
            budget -= len(trib)
            free -= 1
            if free > 0 and len(trib) > 2 and rng.random() < 0.7:
                # a side stream along the height of an inner vertex
                vx, vy = trib[rng.randrange(1, len(trib) - 1)]
                head = cx + STRIP * 0.45
                rivers.append([(round(head, 2), vy), (round((head + vx) / 2, 2), vy), (vx, vy)])
                free -= 1
    if mode == 3:
        rivers = []
        for i in range(rng.randint(1, RIVERS)):
            k = rng.randint(2, POINTS // RIVERS)
            xs = sorted(rng.sample(range(-990, 990), k))
            y0 = -950 + 190 * i
            rivers.append([(x, y0 + rng.randint(0, 150)) for x in xs])
    rng.shuffle(rivers)

    def fmt(v):
        return ("%.2f" % v).rstrip("0").rstrip(".")

    out = ["%d" % len(rivers)]
    for r in rivers:
        out.append("%d" % len(r))
        out += ["%s %s" % (fmt(x), fmt(y)) for x, y in r]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
