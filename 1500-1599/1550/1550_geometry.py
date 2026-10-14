import math

THIRD = 1 / 3  # a pyramid is a third of its prism


def main():
    h, w, x, y, r = map(float, open(0).read().split())
    # the hole meets no edge, so it lies over a single face, where the height
    # is linear: the cut-out volume is the hole's area times the height at
    # its centre, and that height falls from H to 0 with max(|x|, |y|)
    centre = h * (1 - max(abs(x), abs(y)) / (w / 2))
    print("%.5f" % (h * w * w * THIRD - math.pi * r * r * centre))


main()
