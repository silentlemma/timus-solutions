import sys

MOST = 6  # dots in one square
FULL = 4  # from four dots on, all corners of the inner square are used
QUARTER = 0.25  # the inner square's corners are L / 4 from the centre

SMALLEST = 1
LARGEST = 100
EPS = 2e-3  # the coordinates are given to 1e-4, and a fit spreads that error


def square(k, centre):
    """The dots of a square with k dots around centre, for L = 1, with the
    domino lying along the x axis."""
    q = QUARTER
    dots = []
    if k >= 2:
        dots += [complex(-q, -q), complex(q, q)]
    if k >= FULL:
        dots += [complex(q, -q), complex(-q, q)]
    if k == MOST:
        dots += [complex(0, -q), complex(0, q)]  # beside the long sides
    if k % 2 == 1:
        dots.append(0)
    return [centre + d for d in dots]


def fits(template, given):
    """Whether a similarity, maybe mirrored, with scale in the allowed range
    takes the template onto the given dots."""
    g0 = given[0]
    g1 = max(given, key=lambda g: abs(g - g0))
    for mirror in (False, True):
        pts = [t.conjugate() for t in template] if mirror else template
        for a in pts:
            for b in pts:
                if a == b:
                    continue
                turn = (g1 - g0) / (b - a)  # rotation times the scale L
                if not SMALLEST - EPS <= abs(turn) <= LARGEST + EPS:
                    continue
                hit = set()
                for t in pts:
                    image = g0 + (t - a) * turn
                    near = min(range(len(given)), key=lambda i: abs(given[i] - image))
                    if abs(given[near] - image) > EPS:
                        break
                    hit.add(near)
                else:
                    if len(hit) == len(given):
                        return True
    return False


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    given = [complex(float(data[1 + 2 * i]), float(data[2 + 2 * i])) for i in range(n)]
    answers = []
    for a in range(MOST + 1):
        b = n - a
        if a <= b <= MOST:
            template = square(a, 0) + square(b, 1)
            if n == 1 or fits(template, given):
                answers.append("%d %d" % (a, b))
    print("\n".join(answers))


main()
