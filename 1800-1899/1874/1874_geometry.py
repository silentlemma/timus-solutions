from math import sqrt


def main():
    a, b = map(int, input().split())
    # the right triangle on the birch and the ground holds at most a quarter
    # of the squared diagonal; with the triangle of the sticks added, the
    # total is largest when the sticks meet at 135 degrees
    x, y = a / 2, b / 2
    print("%.9f" % (x * x + y * y + 2 * sqrt(2) * x * y))


main()
