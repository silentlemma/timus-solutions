import math
import sys

TURN = 2 * math.pi
SCALE = 1000000


def main():
    x0, y0, eps = map(float, sys.stdin.read().split())
    eps = min(eps, 1.0)
    across = math.asin(max(-1.0, min(1.0, x0)))
    up = math.acos(max(-1.0, min(1.0, y0)))
    # take sqrt(t) = s0 with sin(s0) = x0 and s0 > 2 pi / eps; within pi of
    # t0 = s0^2 some t has cos(t) = y0, and sqrt(t) moves by less than eps / 4
    s0 = across + TURN * (math.ceil(1 / eps) + 1)
    t0 = s0 * s0
    t = up + TURN * math.floor((t0 - up) / TURN + 0.5)
    ticks = math.floor(t * SCALE + 0.5)
    print("%d.%06d" % (ticks // SCALE, ticks % SCALE))


main()
