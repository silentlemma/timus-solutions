import sys

SEATS = 36


def main():
    stream = sys.stdin.buffer
    n = int(stream.readline())
    east = [0] * (n - 1)
    west = [0] * (n - 1)
    for i in range(n):
        for j, people in enumerate(map(int, stream.readline().split())):
            if people:
                load = east if i < j else west
                for leg in range(min(i, j), max(i, j)):
                    load[leg] += people
    peak = max(max(east), max(west))
    print((peak + SEATS - 1) // SEATS)


main()
