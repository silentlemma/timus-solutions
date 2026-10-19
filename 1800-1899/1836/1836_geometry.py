import sys
from fractions import Fraction

CORNERS = 4
TETRAHEDRON = 6  # a corner with legs a, b, c cuts off abc/6


def volume(side, h):
    # the surface is a plane, so the levels at opposite corners add up to
    # the same sum; a sensor reads max(0, level), and 0 hides the level
    dry = [i for i in range(CORNERS) if h[i] == 0]
    if len(dry) == CORNERS:
        return "0.000000"
    diagonal = [0, 0]
    hidden = [False, False]
    for i in range(CORNERS):
        diagonal[i % 2] += h[i]
        hidden[i % 2] |= h[i] == 0
    if not dry:
        if diagonal[0] != diagonal[1]:
            return "error"
        return f"{side * side * sum(h) / CORNERS:.6f}"
    if len(dry) == 1:
        i = dry[0]
        left, far, right = (h[(i + k) % CORNERS] for k in range(1, CORNERS))
        x = left + right - far
        if x > 0:
            return "error"
        # the plane dips below the bottom at corner i in a tetrahedron with
        # legs -x up and -x/(left - x), -x/(right - x) along the edges, so
        # that much negative water is added back
        level = Fraction(x + left + right + far, CORNERS)
        level += Fraction(-x * x * x, TETRAHEDRON * (left - x) * (right - x))
        return f"{float(side * side * level):.6f}"
    # two or more hidden levels: they only have to be at most 0 and keep
    # the two diagonal sums equal, and when that is possible they can move
    if hidden[0] and hidden[1]:
        return "ambiguous"
    low = 0 if hidden[0] else 1
    if diagonal[1 - low] > diagonal[low]:
        return "error"
    return "ambiguous"


def main():
    data = iter(map(int, sys.stdin.read().split()))
    out = []
    for _ in range(next(data)):
        side = next(data)
        out.append(volume(side, [next(data) for _ in range(CORNERS)]))
    print("\n".join(out))


main()
