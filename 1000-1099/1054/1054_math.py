import sys

# the disks start on the source rod and go to the target rod
SOURCE = 1
TARGET = 2
SPARE = 3


def main():
    data = list(map(int, sys.stdin.read().split()))
    n, rod = data[0], [0] + data[1:]
    # disks 1..k are being moved from a to b over c; disk k moves once, in the
    # middle: before it the others go to c, after it they go from c to b
    a, b, c = SOURCE, TARGET, SPARE
    steps = 0
    for k in range(n, 0, -1):
        if rod[k] == a:
            b, c = c, b
        elif rod[k] == b:
            steps += 1 << (k - 1)
            a, c = c, a
        else:
            steps = -1
            break
    print(steps)


main()
