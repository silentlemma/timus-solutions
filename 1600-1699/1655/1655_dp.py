import sys

FULL = 360.0
MINUTES = 60.0
EPS = 1e-9
INF = float("inf")
FIELDS = 3  # azimuth, distance, speed


def main():
    data = sys.stdin.read().split()
    a, w, n = float(data[0]), float(data[1]), int(data[2])
    first = []  # ships right in front of the gun, shot at once
    ships = []
    for k in range(n):
        b, d, v = (float(x) for x in data[FIELDS + FIELDS * k : FIELDS * (k + 2)])
        deadline = (d - 1) / v * MINUTES  # when the ship reaches one mile
        turn = (b - a) % FULL
        if turn <= EPS or FULL - turn <= EPS:
            first.append(k + 1)
        else:
            ships.append((turn, deadline, k + 1))
    ships.sort()
    m = len(ships)
    speed = FULL * w  # degrees a minute
    angle = [s[0] for s in ships]
    due = [s[1] for s in ships]
    # the shot ships form an arc around the start: i taken turning left
    # (from the end of the sorted list), j turning right; left and right
    # keep the earliest time with the gun at that end of the arc
    size = m + 1
    left = [INF] * (size * size)
    right = [INF] * (size * size)
    came_left = [0] * (size * size)  # the side before the last step
    came_right = [0] * (size * size)
    left[0] = right[0] = 0.0
    for i in range(size):
        for j in range(size - i):
            here = i * size + j
            tl, tr = left[here], right[here]
            if tl == INF and tr == INF:
                continue
            at_left = FULL - angle[m - i] if i else 0.0
            at_right = angle[j - 1] if j else 0.0
            if i + j < m:
                nxt = angle[j]  # the next ship turning right
                there = here + 1
                moves = ((tr + (nxt - at_right) / speed, 1), (tl + (at_left + nxt) / speed, 0))
                for t, side in moves:
                    if t <= due[j] + EPS and t + EPS < right[there]:
                        right[there], came_right[there] = t, side
                nxt = FULL - angle[m - i - 1]  # the next ship turning left
                there = here + size
                moves = ((tl + (nxt - at_left) / speed, 0), (tr + (at_right + nxt) / speed, 1))
                for t, side in moves:
                    if t <= due[m - i - 1] + EPS and t + EPS < left[there]:
                        left[there], came_left[there] = t, side
    # ending at the left end wins ties, then the fewest ships taken leftwards
    best, side = INF, 0
    for s, at in ((0, left), (1, right)):
        for i in range(size):
            if at[i * size + m - i] < best:
                best, side = at[i * size + m - i], s
    if best == INF:
        print("Impossible")
        return
    at = right if side else left
    i = next(i for i in range(size) if abs(at[i * size + m - i] - best) <= EPS)
    end = (i, m - i, side)
    order = []
    i, j, side = end
    while i or j:
        here = i * size + j
        if side:
            order.append(ships[j - 1][2])
            side, j = came_right[here], j - 1
        else:
            order.append(ships[m - i][2])
            side, i = came_left[here], i - 1
    out = ["%.3f" % best] + [str(k) for k in first + order[::-1]]
    print("\n".join(out))


main()
