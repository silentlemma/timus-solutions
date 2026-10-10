"""Checker: N - 3 distinct diagonals that do not cross split the polygon
into triangles, and each triangle has one vertex of every color. A cut
always exists, so 0 is rejected. In a triangulated convex polygon every
three mutually joined vertices form one of the triangles."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    data = open(inp).read().split()
    n, color = int(data[0]), data[1]
    try:
        nums = [int(t) for t in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if not nums or nums[0] != n - 3 or len(nums) != 1 + 2 * (n - 3):
        fail("expected %d diagonals" % (n - 3))
    cuts = set()
    for k in range(n - 3):
        a, b = sorted((nums[1 + 2 * k] - 1, nums[2 + 2 * k] - 1))
        if not (0 <= a < b < n) or b - a in (1, n - 1):
            fail("%d %d is not a diagonal" % (a + 1, b + 1))
        cuts.add((a, b))
    if len(cuts) != n - 3:
        fail("a diagonal repeats")
    order = sorted(cuts)
    for i, (a, b) in enumerate(order):
        for c, d in order[i + 1 :]:
            if c >= b:
                break
            # c is inside (a, b) here; d outside [a, b] means a crossing
            if a < c < b < d:
                fail("diagonals %d %d and %d %d cross" % (a + 1, b + 1, c + 1, d + 1))
    near = [set() for _ in range(n)]
    for a, b in list(cuts) + [(i, (i + 1) % n) for i in range(n)]:
        near[a].add(b)
        near[b].add(a)
    faces = 0
    for a in range(n):
        for b in near[a]:
            if b > a:
                for c in near[a] & near[b]:
                    if c > b:
                        faces += 1
                        if {color[a], color[b], color[c]} != set("RGB"):
                            fail("triangle %d %d %d lacks a color" % (a + 1, b + 1, c + 1))
    if faces != n - 2:
        fail("the diagonals do not cut the polygon into triangles")


if __name__ == "__main__":
    main()
