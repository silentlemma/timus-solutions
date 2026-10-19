import math
import sys

TOP = 10.0  # the speed limit; both accelerations are limited by 1
EPS = 1e-12


def piece_time(length, cap, v0, v1):
    # fastest run over a piece entered at v0 and left at v1: speed up,
    # perhaps cruise at the cap, slow down
    if length <= EPS:
        return 0.0
    up = (cap * cap - v0 * v0) / 2
    down = (cap * cap - v1 * v1) / 2
    if up + down <= length:
        return (cap - v0) + (cap - v1) + (length - up - down) / cap
    peak = math.sqrt(length + (v0 * v0 + v1 * v1) / 2)
    return (peak - v0) + (peak - v1)


def main():
    data = iter(map(int, sys.stdin.read().split()))
    n = next(data)
    segs, lengths = [], []
    for _ in range(n):
        ax, ay, bx, by = next(data), next(data), next(data), next(data)
        length = math.hypot(bx - ax, by - ay)
        segs.append((ax, ay, bx, by, (bx - ax) / length, (by - ay) / length))
        lengths.append(length)
    extra = [0.0] * n  # how far each segment is lengthened
    arcs = []  # (length, speed cap) of the arc after each segment
    for i in range(n - 1):
        _, _, bx, by, ux, uy = segs[i]
        ax, ay, _, _, vx, vy = segs[i + 1]
        dx, dy = ax - bx, ay - by
        sin = ux * vy - uy * vx
        cos = ux * vx + uy * vy
        if abs(sin) > EPS:
            # the lines meet t past the end of this segment and back
            # before the start of the next one; the arc touches both lines
            # at the same distance from that point, as far as it can
            t = (dx * vy - dy * vx) / sin
            back = -(dx * uy - dy * ux) / sin
            near = min(t, back)
            extra[i] += t - near
            extra[i + 1] += back - near
            if abs(near) <= EPS:
                arcs.append((0.0, 0.0))
                continue
            radius = abs(near) * (1 + cos) / abs(sin)
            turn = math.atan2(abs(sin), cos)
            # a meeting point behind forces the long way around the circle
            angle = turn if near > 0 else 2 * math.pi - turn
        else:
            # opposite directions: a half circle across the gap
            along = dx * ux + dy * uy
            across = -dx * uy + dy * ux
            if along > 0:
                extra[i] += along
            else:
                extra[i + 1] -= along
            radius = abs(across) / 2
            angle = math.pi
        arcs.append((radius * angle, min(TOP, math.sqrt(radius))))
    pieces = []
    for i in range(n):
        pieces.append((lengths[i] + extra[i], TOP))
        if i < n - 1:
            pieces.append(arcs[i])
    # the speed where pieces meet: what acceleration from the start and
    # braking before the end allow, within the caps on both sides
    m = len(pieces)
    reach = [0.0] * (m + 1)
    for i in range(m):
        length, cap = pieces[i]
        reach[i + 1] = min(cap, math.sqrt(reach[i] ** 2 + 2 * length))
    stop = [0.0] * (m + 1)
    for i in range(m - 1, -1, -1):
        length, cap = pieces[i]
        stop[i] = min(cap, math.sqrt(stop[i + 1] ** 2 + 2 * length))
    speed = [min(a, b) for a, b in zip(reach, stop)]
    total = sum(piece_time(length, cap, speed[i], speed[i + 1])
                for i, (length, cap) in enumerate(pieces))
    print(f"{total:.10f}")


main()
