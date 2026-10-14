import sys

ODD = 3  # the factor of the power of two for odd n
LESS = 4  # every count is that power times 1 or ODD, minus LESS


def main():
    n = int(sys.stdin.read())
    # the counts of polygons grow by 4, 4, 8, 8, 16, 16, ... from zone 3 on
    if n == 1:
        print(1)
    elif n % 2 == 0:
        print((1 << (n // 2 + 2)) - LESS)
    else:
        print(ODD * (1 << (n // 2 + 1)) - LESS)


main()
