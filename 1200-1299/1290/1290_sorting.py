import sys

LARGEST = 25000


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    # counting each value is a sort in descending order, and printing the
    # conjugate partition twice gives back the sorted array
    count = [0] * (LARGEST + 1)
    for token in data[1 : n + 1]:
        count[int(token)] += 1
    out = []
    for value in range(LARGEST, 0, -1):
        out.extend([value] * count[value])
    sys.stdout.write("".join("%d\n" % x for x in out))


main()
