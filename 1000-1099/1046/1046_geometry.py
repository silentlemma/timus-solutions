import cmath
import math
import sys

ROUNDING = 0.005


def clean(v):
    """A value that would print as -0.00 is printed as 0.00."""
    return 0.0 if abs(v) < ROUNDING else v


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    apex = [complex(float(data[1 + 2 * i]), float(data[2 + 2 * i])) for i in range(n)]
    angles = data[1 + 2 * n :]
    turn = [cmath.exp(1j * math.radians(float(x))) for x in angles[:n]]
    # a step turns z around M[i] by its angle, z -> w z + (1 - w) M[i], and going
    # around the polygon composes the steps into z -> a z + b that fixes A[0]
    a, b = 1, 0
    for w, m in zip(turn, apex):
        a, b = w * a, w * b + (1 - w) * m
    # the angles never add up to a multiple of 360, so a != 1
    z = b / (1 - a)
    out = []
    for w, m in zip(turn, apex):
        out.append("%.2f %.2f" % (clean(z.real), clean(z.imag)))
        z = m + w * (z - m)
    print("\n".join(out))


main()
