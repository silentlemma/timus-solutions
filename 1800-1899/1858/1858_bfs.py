import sys
from math import sqrt

FACES = 6


def main():
    data = sys.stdin.buffer.read().split()
    side, n = int(data[0]), int(data[1])
    count = n * n * n
    # crystals with the same rune touch: the crystals and their contacts
    # form the n x n x n grid, whatever the turns of the crystals
    near = [[] for _ in range(count)]
    first = {}
    for c in range(count):
        for rune in data[2 + FACES * c:2 + FACES * (c + 1)]:
            if rune != b"0":
                if rune in first:
                    near[c].append(first[rune])
                    near[first[rune]].append(c)
                else:
                    first[rune] = c

    def spread(start):
        # grid steps from start to every crystal
        steps = [-1] * count
        steps[start] = 0
        queue = [start]
        for v in queue:
            for w in near[v]:
                if steps[w] < 0:
                    steps[w] = steps[v] + 1
                    queue.append(w)
        return steps

    # a corner touches the fewest crystals; the three corners n - 1 steps
    # away lie along the edges from it, and the steps to a corner and to
    # one of them give the coordinate along that edge
    corner = min(range(count), key=lambda c: len(near[c]))
    origin = spread(corner)
    axes = [spread(c) for c in range(count)
            if origin[c] == n - 1 and len(near[c]) == len(near[corner])]
    place = [[(origin[v] - far[v] + n - 1) // 2 for far in axes] for v in range(count)]
    pos = 2 + FACES * count
    m = int(data[pos])
    out = []
    for k in range(m):
        a, b = int(data[pos + 1 + 2 * k]) - 1, int(data[pos + 2 + 2 * k]) - 1
        out.append("%.7f" % (side * sqrt(sum((x - y) ** 2 for x, y in zip(place[a], place[b])))))
    print("\n".join(out))


main()
