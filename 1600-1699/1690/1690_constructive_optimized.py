import sys
from array import array

PARITY_CLASSES = 4
ODD_BIT = 1


def select(lines, count):
    groups = [array("H") for _ in range(PARITY_CLASSES)]
    for index, line in enumerate(lines, 1):
        x, y = map(int, line.split())
        group = groups[2 * (x & ODD_BIT) + (y & ODD_BIT)]
        group.append(index)
        if len(group) == count:
            return group


def main():
    stream = sys.stdin.buffer
    count = int(stream.readline())
    selected = select(stream, count)
    print("OK")
    print(" ".join(map(str, selected)))


if __name__ == "__main__":
    main()
