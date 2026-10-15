import math


def main():
    m, n = map(int, input().split())
    # m * n moves close the tour; m + n + 1 of them are diagonal
    diagonal = m + n + 1
    print("%.12f" % (m * n + diagonal * (math.sqrt(2) - 1)))


main()
