import sys

TIME = 30000


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # the latest start among the talks that end at each minute
    latest = [0] * (TIME + 1)
    for s, e in zip(map(int, data[1 : 2 * n + 1 : 2]), map(int, data[2 : 2 * n + 2 : 2])):
        if s > latest[e]:
            latest[e] = s
    # take the talk that ends first among those starting after the last one
    count, last = 0, 0
    for e in range(1, TIME + 1):
        if latest[e] > last:
            count += 1
            last = e
    print(count)


main()
