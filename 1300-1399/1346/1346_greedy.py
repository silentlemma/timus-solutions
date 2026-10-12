import sys


def main():
    data = sys.stdin.buffer.read().split()
    a, b = int(data[0]), int(data[1])
    f = [int(x) for x in data[2:][: b - a + 1]]
    pieces, i, n = 0, 0, len(f)
    while i < n:
        # stretch this piece while it stays monotone; its way up or down is
        # fixed by its first step that is not flat
        pieces += 1
        way, j = 0, i
        while j + 1 < n:
            step = (f[j + 1] > f[j]) - (f[j + 1] < f[j])
            if step and way and step != way:
                break
            way = way or step
            j += 1
        i = j + 1
    print(pieces)


main()
