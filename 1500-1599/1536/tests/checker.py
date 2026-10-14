"""Checker: "Impossible" exactly when expected; otherwise a true sum X+Y=Z
of as many characters, numbers of 1 to 8 digits without leading zeros,
made of the same number of sticks, at most K of them moved."""

import sys

TOP, MIDDLE, BOTTOM, UPPER_LEFT, UPPER_RIGHT, LOWER_LEFT, LOWER_RIGHT = (1 << i for i in range(7))
UPPER_SLASH, LOWER_SLASH, PLUS_UPRIGHT, EQUAL_UPPER, EQUAL_LOWER = (1 << i for i in range(7, 12))
SIDES = UPPER_LEFT | UPPER_RIGHT | LOWER_LEFT | LOWER_RIGHT
SHAPES = {
    "0": TOP | SIDES | BOTTOM,
    "1": UPPER_SLASH | UPPER_RIGHT | LOWER_RIGHT,
    "2": TOP | UPPER_RIGHT | LOWER_SLASH | BOTTOM,
    "3": TOP | UPPER_SLASH | MIDDLE | LOWER_SLASH,
    "4": UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_RIGHT,
    "5": TOP | UPPER_LEFT | MIDDLE | LOWER_RIGHT | BOTTOM,
    "6": UPPER_SLASH | MIDDLE | LOWER_LEFT | LOWER_RIGHT | BOTTOM,
    "7": TOP | UPPER_SLASH | LOWER_LEFT,
    "8": TOP | SIDES | MIDDLE | BOTTOM,
    "9": TOP | UPPER_LEFT | UPPER_RIGHT | MIDDLE | LOWER_SLASH,
    "+": MIDDLE | PLUS_UPRIGHT,
    "=": EQUAL_UPPER | EQUAL_LOWER,
}
LONGEST = 8


def fail(reason):
    print(reason)
    sys.exit(1)


def count(shape):
    return bin(shape).count("1")


def main():
    source, expected, output = sys.argv[1:4]
    tokens = open(source).read().split()
    start, k = "".join(tokens[:-1]), int(tokens[-1])
    want = open(expected).read().strip()
    got = open(output).read().strip()
    if (want == "Impossible") != (got == "Impossible"):
        fail("got %r, expected %r" % (got, want))
    if got == "Impossible":
        return
    if len(got) != len(start) or got.count("+") != 1 or got.count("=") != 1:
        fail("%r is not an expression of the same length" % got)
    left, z = got.split("=")
    if "+" not in left:
        fail("the plus is not before the equals sign in %r" % got)
    x, y = left.split("+")
    for number in (x, y, z):
        if not number.isdigit() or len(number) > LONGEST or (len(number) > 1 and number[0] == "0"):
            fail("bad number %r" % number)
    if int(x) + int(y) != int(z):
        fail("%s + %s is not %s" % (x, y, z))
    before = [SHAPES[c] for c in start]
    after = [SHAPES[c] for c in got]
    if sum(map(count, before)) != sum(map(count, after)):
        fail("sticks were added or removed")
    moved = sum(count(b & ~a) for a, b in zip(before, after))
    if moved > k:
        fail("%d sticks moved, more than %d" % (moved, k))


main()
