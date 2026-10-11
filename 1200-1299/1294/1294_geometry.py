import math

KM = 1000  # input distances are in thousands of kilometres
HALF = 0.5


def main():
    # a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
    # inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
    a, b, c, d = map(int, input().split())
    den = a * b - c * d
    diff = a * a + b * b - c * c - d * d
    if den == 0 or abs(diff) > 2 * abs(den):
        print("Impossible.")
        return
    num = a * b * (c * c + d * d) - c * d * (a * a + b * b)
    # halves go up, as in the other languages, not to even as round() does
    print("Distance is %d km." % math.floor(KM * math.sqrt(num / den) + HALF))


main()
