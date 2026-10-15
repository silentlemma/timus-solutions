import math


def main():
    data = open(0).read().split()
    n = int(data[0])
    # Sandro's own spot holds no demon: stay there and reach the farthest one
    farthest = max(math.hypot(int(data[1 + 2 * i]), int(data[2 + 2 * i])) for i in range(n))
    print("0 0 %.10f" % farthest)


main()
