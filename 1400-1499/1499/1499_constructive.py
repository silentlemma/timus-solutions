import sys


def main():
    data = sys.stdin.buffer.read().split()
    n, k = int(data[0]), int(data[1])
    ending = [[] for _ in range(n + 1)]  # the cuts u-v with u < v, kept at v
    given = data[2:]
    for i in range(k):
        a, b = sorted((int(given[2 * i]), int(given[2 * i + 1])))
        ending[b].append(a)

    cuts = []

    def fan(face):
        # a convex face is cut into triangles by diagonals from its first
        # vertex; the first and the last of its sides already exist
        for w in face[2:-1]:
            cuts.append((face[0], w))

    # walk the vertices in order: a cut u-v closes the face formed by u,
    # the vertices still stacked above it, and v; nearer u first
    stack = []
    for v in range(1, n + 1):
        stack.append(v)
        for u in sorted(ending[v], reverse=True):
            stack.pop()
            inner = []
            while stack[-1] != u:
                inner.append(stack.pop())
            fan([u] + inner[::-1] + [v])
            stack.append(v)
    fan(stack)  # the last face, closed by the side n-1
    out = [str(len(cuts))] + ["%d %d" % c for c in cuts]
    sys.stdout.write("\n".join(out) + "\n")


main()
