import sys


def main():
    data = sys.stdin.buffer.read().split()
    f = list(map(int, data[1 : 1 + int(data[0])]))
    # the slope of a chord is the mean of the slopes of the steps under it, so
    # the steepest valid chord joins two neighbours; take the first steepest
    steps = [abs(b - a) for a, b in zip(f, f[1:])]
    a = steps.index(max(steps)) + 1
    print(a, a + 1)


main()
