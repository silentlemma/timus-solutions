import heapq
import math
import sys

PIPE = 3  # numbers per pipe


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    xs = [int(w) for w in data[1:2 * n + 1:2]]
    ys = [int(w) for w in data[2:2 * n + 2:2]]
    m = int(data[2 * n + 1])
    rest = data[2 * n + 2:]
    ends = [int(w) - 1 for w in rest[0::PIPE]] + [0]
    tips = [int(w) - 1 for w in rest[1::PIPE]] + [n - 1]
    caps = [int(w) for w in rest[2::PIPE]]
    # half-edge 2i runs from ends[i] to tips[i], 2i + 1 back; pipe m is an
    # extra edge from the source, leaving to the left, round the outside to
    # the sink, arriving from the right
    halves = 2 * m + 2
    origin = [0] * halves
    dx = [0] * halves
    dy = [0] * halves
    for i in range(m + 1):
        a, b = ends[i], tips[i]
        origin[2 * i], origin[2 * i + 1] = a, b
        dx[2 * i], dy[2 * i] = xs[b] - xs[a], ys[b] - ys[a]
        dx[2 * i + 1], dy[2 * i + 1] = -dx[2 * i], -dy[2 * i]
    dx[2 * m], dy[2 * m], dx[2 * m + 1], dy[2 * m + 1] = -1, 0, 1, 0
    around = [[] for _ in range(n)]
    for h in range(halves):
        around[origin[h]].append(h)

    def before(g, h):
        """Whether g comes strictly before h counterclockwise from the +x axis."""
        hg = dy[g] < 0 or (dy[g] == 0 and dx[g] < 0)
        hh = dy[h] < 0 or (dy[h] == 0 and dx[h] < 0)
        if hg != hh:
            return hh
        return dx[g] * dy[h] - dy[g] * dx[h] > 0

    angle = [math.atan2(dy[h], dx[h]) % (2 * math.pi) for h in range(halves)]
    pos = [0] * halves
    for out in around:
        out.sort(key=angle.__getitem__)
        # floating angles may swap nearly equal directions; fix them exactly
        for k in range(1, len(out)):
            j = k
            while j > 0 and before(out[j], out[j - 1]):
                out[j], out[j - 1] = out[j - 1], out[j]
                j -= 1
        for k, h in enumerate(out):
            pos[h] = k
    # faces: after arriving at a vertex, leave by the next edge clockwise
    face = [-1] * halves
    faces = 0
    for h in range(halves):
        if face[h] >= 0:
            continue
        g = h
        while face[g] < 0:
            face[g] = faces
            out = around[origin[g ^ 1]]
            g = out[pos[g ^ 1] - 1]
        faces += 1
    # the minimum cut is the shortest path between the two faces next to
    # the extra edge, with pipe capacities as lengths
    links = [[] for _ in range(faces)]
    for i in range(m):
        a, b = face[2 * i], face[2 * i + 1]
        links[a].append((b, caps[i]))
        links[b].append((a, caps[i]))
    far = float("inf")
    dist = [far] * faces
    start = face[2 * m]
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, f = heapq.heappop(heap)
        if d > dist[f]:
            continue
        for g, c in links[f]:
            if d + c < dist[g]:
                dist[g] = d + c
                heapq.heappush(heap, (d + c, g))
    # the flow from ends[i] to tips[i] is the difference of the distances
    # of the faces on its two sides
    flow = [0] * m
    for i in range(m):
        left, right = dist[face[2 * i]], dist[face[2 * i + 1]]
        if left != far and right != far:
            flow[i] = right - left
    total = sum(flow[i] if ends[i] == 0 else -flow[i] for i in range(m) if 0 in (ends[i], tips[i]))
    sign = 1 if total >= 0 else -1
    out = [str(total * sign)]
    for i in range(m):
        f = flow[i] * sign
        if f >= 0:
            out.append("%d %d %d" % (ends[i] + 1, tips[i] + 1, f))
        else:
            out.append("%d %d %d" % (tips[i] + 1, ends[i] + 1, -f))
    sys.stdout.write("\n".join(out) + "\n")


main()
