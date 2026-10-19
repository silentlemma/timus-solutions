import sys

TRIO = 3


def main():
    data = list(map(int, sys.stdin.read().split()))
    times = sorted(data[1:1 + data[0]])
    total = 0
    # move the two slowest across each round, in whichever of two ways is
    # cheaper: the fastest escorts each of them, or the two fastest cross,
    # one comes back, the two slowest cross together and the other returns
    while len(times) > TRIO:
        a, b, y, z = times[0], times[1], times[-2], times[-1]
        total += min(2 * a + y + z, a + 2 * b + z)
        times = times[:-2]
    if len(times) == TRIO:
        total += sum(times)
    else:
        total += times[-1]
    print(total)


main()
