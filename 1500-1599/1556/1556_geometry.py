import heapq
import math
import sys
from bisect import bisect_left

TAU = 2 * math.pi
EPS = 1e-12  # events closer than this in angle happen together
MOST_HITS = 5  # an arrow stops after the fifth cow
PERCENT = 100
HALF = 0.5
ENTER, LEAVE = 0, 1  # at one angle, rays start touching before they stop


def norm(a):
    """The angle in [0, 2 pi); a tiny negative angle may round up to 2 pi."""
    a %= TAU
    return 0.0 if a >= TAU else a


def main():
    words = iter(sys.stdin.buffer.read().split())
    n, k, p = int(next(words)), int(next(words)), int(next(words))
    r, vx, vy = float(next(words)), float(next(words)), float(next(words))
    # expected hits of an arrow whose ray meets m cows, kept exact as integers
    # in units of 1 / 100^4: each further cow adds p / 100 of the last addition
    gain = [0]
    for m in range(1, MOST_HITS + 1):
        gain.append(gain[-1] + p ** (m - 1) * PERCENT ** (MOST_HITS - m))
    gain += [gain[MOST_HITS]] * (n + 1 - len(gain))
    shift = [math.atan(i / (k - 1) - HALF) for i in range(k)]
    # rays meet a cow at angles within asin(R / d) of its centre, and
    # each arrow sees the same angular intervals turned back by its offset
    angles, kinds = [], []
    for _ in range(n):
        cx, cy = float(next(words)) - vx, float(next(words)) - vy
        centre = math.atan2(cy, cx)
        half = math.asin(min(1.0, r / math.hypot(cx, cy)))
        angles += [norm(centre - half), norm(centre + half)]
        kinds += [ENTER, LEAVE]
    order = sorted(range(2 * n), key=lambda e: (angles[e], kinds[e]))
    base = [angles[e] for e in order]
    base_kind = [kinds[e] for e in order]
    turn = [norm(a) for a in shift]

    def turned(a, i):
        """Angle a seen by arrow i: the events of one arrow come in this order."""
        return a - turn[i] if a >= turn[i] else a - turn[i] + TAU

    # how many intervals of each arrow hold the angle 0: those that wrap
    count = [0] * k
    for i in range(k):
        for j in range(n):
            if turned(angles[2 * j], i) > turned(angles[2 * j + 1], i):
                count[i] += 1

    def stream(i):
        """The events of arrow i in increasing angle, from 0 up to 2 pi."""
        cut = bisect_left(base, turn[i])
        for part in (range(cut, 2 * n), range(cut)):  # walked lazily: k streams at once
            for e in part:
                yield turned(base[e], i), base_kind[e], i

    best, best_angle = -1, 0.0
    total = sum(gain[c] for c in count)
    events = heapq.merge(*(stream(i) for i in range(k)))
    pending = next(events)
    first = pending[0]
    while pending:
        x = pending[0]
        leaving = []
        while pending and pending[0] - x <= EPS:
            i = pending[2]
            if pending[1] == ENTER:
                total += gain[count[i] + 1] - gain[count[i]]
                count[i] += 1
            else:
                leaving.append(i)
            pending = next(events, None)
        # at the angle itself, touching counts: new cows join, none leave yet
        point = total
        for i in leaving:
            count[i] -= 1
            total -= gain[count[i] + 1] - gain[count[i]]
        # after the last event the stretch runs on past 2 pi to the first one
        following = pending[0] if pending else TAU + first
        # an open stretch is safer than a single tangent angle, so it wins ties
        if following - x > EPS and total >= best:
            best, best_angle = total, (x + following) / 2
        if point > best:
            best, best_angle = point, x
    print(
        "The best shot at (%.10f;%.10f) gives Vasya %.4f average hits."
        % (math.cos(best_angle), math.sin(best_angle), best / PERCENT ** (MOST_HITS - 1))
    )


main()
