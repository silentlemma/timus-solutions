import sys


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    where = {}  # a value and the number of one element holding it
    for i in range(n):
        where.setdefault(int(data[1 + i]), i + 1)
    a = sorted(where)
    best = (1, a[0], 1)  # length, first value, difference
    for i, x in enumerate(a):
        for y in a[i + 1 :]:
            d = y - x
            # walk each progression only from its first member, so every
            # pair of neighbours in it is visited once
            if x - d in where:
                continue
            length, last = 2, y
            while last + d in where:
                last += d
                length += 1
            if length > best[0]:
                best = (length, x, d)
    length, first, d = best
    print(length)
    print(" ".join(str(where[first + k * d]) for k in range(length)))


main()
