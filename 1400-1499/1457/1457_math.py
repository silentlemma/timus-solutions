import sys


def main():
    data = sys.stdin.read().split()
    p = [int(x) for x in data[1 : 1 + int(data[0])]]
    # the mean of squared distances is smallest at the arithmetic mean
    print("%.6f" % (sum(p) / len(p)))


main()
