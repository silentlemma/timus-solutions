import math
import sys

COLORS = ["VIOLET", "INDIGO", "BLUE", "GREEN", "YELLOW", "ORANGE", "RED"]
RED = len(COLORS) - 1
PER_DECADE = 5  # a level per 2 dB: five levels per tenfold distance
EPS = 1e-9  # events closer than this in segment time happen together
TIE = 1e-9  # powers closer than this relative gap are equal


def main():
    data = sys.stdin.buffer.read().split()
    pos = 0

    def take():
        nonlocal pos
        pos += 1
        return data[pos - 1]

    n = int(take())
    xs, ys, rs, names = [], [], [], []
    for _ in range(n):
        xs.append(int(take()))
        ys.append(int(take()))
        rs.append(int(take()))
        names.append(take())
    # squared radii where the level steps up: violet inside the first, red outside the last
    bounds = [[(r * 10 ** (k / PER_DECADE)) ** 2 for k in range(RED)] for r in rs]
    m = int(take())
    # each segment as its start and its end
    segments = [((int(take()), int(take())), (int(take()), int(take()))) for _ in range(m)]
    out = []

    def level(i, px, py):
        d2 = (px - xs[i]) ** 2 + (py - ys[i]) ** 2
        return sum(d2 > b for b in bounds[i])

    def best(cands, px, py):
        """The strongest station at (px, py); equal powers go to the smaller name."""
        top = None
        for i in cands:
            if top is None:
                top = i
                continue
            # power is r / d: compare r_i * d_top with r_top * d_i
            di = math.hypot(px - xs[i], py - ys[i])
            dt = math.hypot(px - xs[top], py - ys[top])
            a, b = rs[i] * dt, rs[top] * di
            if a > b * (1 + TIE) or (abs(a - b) <= TIE * max(a, b) and names[i] < names[top]):
                top = i
        return top

    sx, sy = segments[0][0]
    cur = best(range(n), sx, sy)
    lev = level(cur, sx, sy)
    out.append(b"Power on. CELL_ID:%s, SIGNAL_LEVEL:%s" % (names[cur], COLORS[lev].encode()))

    for (sx, sy), (ex, ey) in segments:
        dx, dy = ex - sx, ey - sy
        a = dx * dx + dy * dy
        if a == 0:
            continue

        def roots(i, rad2):
            # times in (0, 1) where the distance to station i squared is rad2
            px, py = sx - xs[i], sy - ys[i]
            b = dx * px + dy * py
            c = px * px + py * py - rad2
            disc = b * b - a * c
            if disc <= 0:
                return []
            q = -(b + math.copysign(math.sqrt(disc), b))
            return [t for t in (q / a, c / q) if 0 < t < 1]

        # red and not red switch only on the outer circles
        reds = [(t, i) for i in range(n) for t in roots(i, bounds[i][RED - 1])]

        def timeline():
            own = [(t, -1) for b in bounds[cur] for t in roots(cur, b)]
            return sorted(reds + own)

        def level_after(i, t):
            # the level of station i just after time t, before its own next change
            later = [u for b in bounds[i] for u in roots(i, b) if u > t + EPS]
            u = (t + min(later + [1.0])) / 2
            return level(i, sx + dx * u, sy + dy * u)

        events = timeline()
        k = 0
        while k < len(events):
            t0 = events[k][0]
            group = []
            while k < len(events) and events[k][0] - t0 <= EPS:
                group.append(events[k][1])
                k += 1
            # the state right after the group holds until the next event
            tend = events[k - 1][0]
            t1 = events[k][0] if k < len(events) else 1.0
            mx, my = sx + dx * (t0 + t1) / 2, sy + dy * (t0 + t1) / 2
            px, py = sx + dx * t0, sy + dy * t0
            switched = False
            if lev != RED:
                now = level(cur, mx, my)
                if now != lev:
                    lev = now
                    out.append(b"Signal changed. SIGNAL_LEVEL:%s" % COLORS[lev].encode())
                    if lev == RED:
                        cands = [i for i in range(n) if level(i, mx, my) < RED]
                        switched = True
            else:
                cands = [i for i in group if i >= 0 and level(i, mx, my) < RED]
                switched = True
            if switched and cands:
                pick = best(cands, px, py)
                lev = level_after(pick, tend)
                if pick == cur:
                    out.append(b"Signal changed. SIGNAL_LEVEL:%s" % COLORS[lev].encode())
                else:
                    cur = pick
                    out.append(
                        b"Cell changed. CELL_ID:%s, SIGNAL_LEVEL:%s"
                        % (names[cur], COLORS[lev].encode())
                    )
                    events = [e for e in timeline() if e[0] > tend + EPS]
                    k = 0
    sys.stdout.buffer.write(b"".join(line + b"\n" for line in out))


main()
