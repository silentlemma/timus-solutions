import math

KM = 1000  # input distances are in thousands of kilometres


def main():
    # a = AD, b = AC, c = BD, d = BC; A and B see the chord CD at the same
    # inscribed angle t, so CD^2 = a^2 + b^2 - 2ab cos t = c^2 + d^2 - 2cd cos t
    a, b, c, d = map(int, input().split())
    den = a * b - c * d
    diff = a * a + b * b - c * c - d * d
    if den == 0 or abs(diff) >= 2 * abs(den) or b * c <= a * d:
        print("Impossible.")
        return
    num = a * b * (c * c + d * d) - c * d * (a * a + b * b)
    if den < 0:
        num = -num
        den = -den
    km = int(KM * math.sqrt(num / den))
    # Compare the half-kilometre boundary exactly, dividing before scaling.
    scale = 4 * KM * KM
    bound = scale * (num // den) + scale * (num % den) // den
    if (2 * km + 1) * (2 * km + 1) <= bound:
        km += 1
    print("Distance is %d km." % km)


main()
