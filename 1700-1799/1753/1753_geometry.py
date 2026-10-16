import math


def main():
    rim, book, _ = (int(v) for v in input().split())
    # with the foot at distance x from the rim and r = hypot(x, rim), the book
    # leans on the rim top and its middle lies x * (book / 2r - 1) to the left,
    # which is largest where r cubed is book * rim * rim / 2
    r = math.cbrt(book * rim * rim / 2)
    shift = 0.0
    if r > rim:
        x = math.sqrt(r * r - rim * rim)
        shift = x * (book / (2 * r) - 1)
    print("%.6f" % shift)


main()
