import math
import sys

QUARTER = 0.25
THIRD = 1 / 3


def main():
    a, b, n = sys.stdin.read().split()
    a, b, n = float(a), float(b), int(n)
    half = b / 2

    def below(z):
        """The volume of the pineapple between its middle and height z: the
        cross-section at z is a disc of area pi (a / 2)^2 (1 - (z / half)^2)."""
        return math.pi * a * a * QUARTER * (z - z * z * z * THIRD / (half * half))

    for i in range(n):
        print("%.6f" % (below(-half + b * (i + 1) / n) - below(-half + b * i / n)))


main()
