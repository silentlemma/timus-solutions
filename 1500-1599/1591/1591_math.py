from math import comb

FOUR = 4  # one corner inside: 4 points, one triangle on each side
FIVE = 5  # two corners inside: 5 points, one triangle per apex
SIX = 6  # three corners inside: 6 points, the three long diagonals


def main():
    n = int(input())
    # a triangle is fixed by the set of chord ends it uses, and a set of
    # k points on the circle gives a fixed number of triangles
    print(comb(n, SIX) + FIVE * comb(n, FIVE) + FOUR * comb(n, FOUR))


main()
