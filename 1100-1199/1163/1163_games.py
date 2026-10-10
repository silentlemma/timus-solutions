import math
import sys

# a draught is hit when its centre is this close to the path of the centre
# of the moving one, two radii of 0.4
REACH = 0.8
EPS = 1e-9
SIDE = 8
PIECES = 2 * SIDE


def main():
    v = list(map(float, sys.stdin.read().split()))
    pts = [(v[2 * k], v[2 * k + 1]) for k in range(PIECES)]
    # every direction kills the draughts within REACH of its ray; the set
    # changes only where the ray becomes tangent to some draught, so the
    # tangent directions and the gaps between them give every possible set
    kills = []
    for p, (px, py) in enumerate(pts):
        angles = []
        for q, (qx, qy) in enumerate(pts):
            if q != p:
                d = math.hypot(qx - px, qy - py)
                centre, half = math.atan2(qy - py, qx - px), math.asin(min(1.0, REACH / d))
                angles += [(centre - half) % (2 * math.pi), (centre + half) % (2 * math.pi)]
        angles.sort()
        tries = angles + [
            (a + b) / 2 for a, b in zip(angles, angles[1:] + [angles[0] + 2 * math.pi])
        ]
        sets = set()
        for t in tries:
            ux, uy = math.cos(t), math.sin(t)
            mask = 0
            for q, (qx, qy) in enumerate(pts):
                dx, dy = qx - px, qy - py
                if q != p and dx * ux + dy * uy >= 0 and abs(dx * uy - dy * ux) <= REACH + EPS:
                    mask |= 1 << q
            sets.add(mask | 1 << p)
        kills.append(sorted(sets))
    red, white = (1 << SIDE) - 1, ((1 << SIDE) - 1) << SIDE
    memo = {}

    def wins(alive, turn):
        # the player to move, red (0) or white (1), wins from here
        key = alive << 1 | turn
        if key in memo:
            return memo[key]
        own = alive & (white if turn else red)
        result = False
        p = 0
        while own and not result:
            if own >> p & 1:
                own &= ~(1 << p)
                for s in kills[p]:
                    if not wins(alive & ~s, 1 - turn):
                        result = True
                        break
            p += 1
        memo[key] = result
        return result

    print("RED" if wins((1 << PIECES) - 1, 0) else "WHITE")


main()
