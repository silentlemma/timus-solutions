import sys


def cross(o, a, b):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


def hull_area(points):
    """Area of the convex hull, by the monotone chain and the shoelace."""
    points = sorted(set(points))
    chain = []
    for seq in (points, points[::-1]):
        part = []
        for p in seq:
            while len(part) > 1 and cross(part[-2], part[-1], p) <= 0:
                part.pop()
            part.append(p)
        chain += part[:-1]
    return abs(sum(cross((0, 0), chain[i - 1], chain[i]) for i in range(len(chain)))) / 2


def main():
    words = iter(sys.stdin.read().split())
    n = int(next(words))
    rivers = []
    for _ in range(n):
        k = int(next(words))
        rivers.append([(float(next(words)), float(next(words))) for _ in range(k)])
    # a river is a tributary of the one whose inner vertex is its mouth
    owner = {p: i for i, r in enumerate(rivers) for p in r[1:-1]}
    tributaries = [[] for _ in range(n)]
    for i, r in enumerate(rivers):
        if r[-1] in owner and owner[r[-1]] != i:
            tributaries[owner[r[-1]]].append(i)

    def basin(i):
        points = list(rivers[i])
        for t in tributaries[i]:
            points += basin(t)
        return points

    print("%.2f" % max(hull_area(basin(i)) for i in range(n)))


main()
