SIDE_FACTOR = 4  # the area is 4a - 1/3


def main():
    a = int(input())
    # 4a - 1/3 = (4a - 1) + 2/3, and 2/3 rounds to 0.6666666667
    print("%d.6666666667" % (SIDE_FACTOR * a - 1))


main()
