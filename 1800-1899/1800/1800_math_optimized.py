import os
from sys import stdout

from math import cos, pi, sin

GRAVITY = 9.81
SQUARE_ROOT_POWER = 0.5
CENTIMETRES = 100
SECONDS = 60
# Positive odd-quarter intervals have ratio at most two: 60 bisections exhaust float precision.
STEPS = 60
TURN = 4


def main():
    length, height, turns = map(int, open(0, "rb", buffering=0).read().split())
    half = length / CENTIMETRES / 2
    top = height / CENTIMETRES
    omega = turns * 2 * pi / SECONDS
    quarter = pi / 2 / omega

    def gap(t):
        # the height of the lowest end of the toast at time t
        return top - GRAVITY * t * t / 2 - half * abs(sin(omega * t))

    def slope(t, k):
        # d gap / dt in quarter k, where the angle within the half turn is
        # omega*t - (k // 2)*pi
        return -GRAVITY * t - half * omega * cos(omega * t - (k // 2) * pi)

    def bend(t, k):
        # d slope / dt, falling through an odd quarter
        return -GRAVITY + half * omega * omega * sin(omega * t - (k // 2) * pi)

    # No endpoint can touch before the centre has fallen to half the toast length.
    earliest = (2 * max(0.0, top - half) / GRAVITY) ** SQUARE_ROOT_POWER
    # Keep one preceding quarter so floating-point rounding cannot skip contact.
    k = max(0, int(earliest / quarter) - 1)
    while True:
        a, b = k * quarter, (k + 1) * quarter
        lowest = gap(b)
        if k % 2 == 1:
            # the end rises again here: the slope of the gap is concave, so
            # find its peak; where it turns positive, the gap has a minimum
            lo, hi = a, b
            for _ in range(STEPS):
                mid = (lo + hi) / 2
                if bend(mid, k) > 0:
                    lo = mid
                else:
                    hi = mid
            if slope(lo, k) > 0:
                lo, hi = a, lo
                for _ in range(STEPS):
                    mid = (lo + hi) / 2
                    if slope(mid, k) < 0:
                        lo = mid
                    else:
                        hi = mid
                lowest = min(lowest, gap(lo))
        if lowest <= 0:
            break
        k += 1
    # in quarters 0 and 3 of a turn the butter faces down
    print("butter" if k % TURN in (0, TURN - 1) else "bread")


main()

# Flush the complete answer before skipping interpreter teardown.
stdout.flush()
os._exit(0)
