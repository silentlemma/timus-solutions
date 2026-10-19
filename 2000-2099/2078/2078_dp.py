PINS = 10
INF = float("inf")


def last_frame(total):
    # rolls of the last frame: two, and a third one after a strike or a spare
    options = []
    for r1 in range(PINS + 1):
        for r2 in range(PINS + 1 if r1 == PINS else PINS - r1 + 1):
            if r1 < PINS and r1 + r2 < PINS:
                if r1 + r2 == total:
                    options.append((r1, r2))
                continue
            fresh = r1 == PINS and r2 == PINS or r1 < PINS
            r3 = total - r1 - r2
            if 0 <= r3 <= (PINS if fresh else PINS - r2):
                options.append((r1, r2, r3))
    return options


def main():
    totals = list(map(int, input().split()))
    # best[(x, y)]: the least and the most points of the frames from the current
    # one on, when the rolls from the current frame on start with x and y
    best = {}
    for rolls in last_frame(totals[-1]):
        key = rolls[:2]
        low, high = best.get(key, (INF, -INF))
        best[key] = (min(low, totals[-1]), max(high, totals[-1]))
    for t in reversed(totals[:-1]):
        nxt = {}
        for (x, y), (low, high) in best.items():
            if t < PINS:
                choices = [((r1, t - r1), 0) for r1 in range(t + 1)]
            else:
                # a strike takes the next two rolls, a spare the next one
                choices = [((PINS, x), x + y)] + [((r1, PINS - r1), x) for r1 in range(PINS)]
            for key, bonus in choices:
                a, b = nxt.get(key, (INF, -INF))
                nxt[key] = (min(a, low + t + bonus), max(b, high + t + bonus))
        best = nxt
    print(min(v[0] for v in best.values()), max(v[1] for v in best.values()))


main()
