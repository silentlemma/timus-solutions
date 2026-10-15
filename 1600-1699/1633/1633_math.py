import math


def main():
    a1, b1, a2, b2 = map(int, open(0).read().split())
    # the largest singular value of [[a1, b1], [a2, b2]] without cancellation:
    # both sums of squares are exact integers
    p = (a1 + b2) ** 2 + (b1 - a2) ** 2
    q = (a1 - b2) ** 2 + (b1 + a2) ** 2
    print("%.10f" % ((math.sqrt(p) + math.sqrt(q)) / 2))


main()
