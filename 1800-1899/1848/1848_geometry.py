import sys
from array import array

LOAD = 300
LIMIT = 10**7
COORD_BITS = (2 * LIMIT).bit_length()
COORD_MASK = (1 << COORD_BITS) - 1
EDGE_FIELDS = 5
DIGIT_ZERO = ord("0")
MINUS = ord("-")


def read_numbers():
    numbers = array("i")
    value = 0
    sign = 1
    digits = False
    for c in sys.stdin.buffer.read() + b" ":
        if c >= DIGIT_ZERO:
            value = value * 10 + c - DIGIT_ZERO
            digits = True
        elif c == MINUS:
            sign = -1
        elif digits:
            numbers.append(sign * value)
            value = 0
            sign = 1
            digits = False
    return numbers


def main():
    data = read_numbers()
    n = data[0]
    flies = [((data[1 + 2 * i] + LIMIT) << COORD_BITS) + data[2 + 2 * i] + LIMIT for i in range(n)]
    flies.sort()
    pos = 1 + 2 * n
    m = data[pos]
    pos += 1
    # A positive owner means that the polygon interior is below the edge.
    lx, ly, dx, dy, owner = (array("i") for _ in range(EDGE_FIELDS))
    left, right = array("q"), array("q")
    for p in range(1, m + 1):
        k = data[pos]
        pos += 1
        ax, ay = data[pos + 2 * k - 2], data[pos + 2 * k - 1]
        a = ((ax + LIMIT) << COORD_BITS) + ay + LIMIT
        for _ in range(k):
            bx, by = data[pos], data[pos + 1]
            pos += 2
            b = ((bx + LIMIT) << COORD_BITS) + by + LIMIT
            if a < b:
                lx.append(ax)
                ly.append(ay)
                dx.append(bx - ax)
                dy.append(by - ay)
                left.append(a)
                right.append(b)
                owner.append(-p)
            else:
                lx.append(bx)
                ly.append(by)
                dx.append(ax - bx)
                dy.append(ay - by)
                left.append(b)
                right.append(a)
                owner.append(p)
            ax, ay, a = bx, by, b
    del data
    edges = len(left)
    starts = sorted(range(edges), key=left.__getitem__)
    ends = sorted(range(edges), key=right.__getitem__)
    count = [0] * m
    si = ei = 0
    buckets = []
    # Handles avoid geometric comparisons when an edge leaves the sweep.
    where = [None] * edges

    def find(edge):
        # Only starting edges are searched. Every active edge already spans
        # this endpoint; a common endpoint is ordered by the two directions.
        x, y, vx, vy = lx[edge], ly[edge], dx[edge], dy[edge]
        lo, hi = 0, len(buckets)
        while lo < hi:
            mid = (lo + hi) // 2
            other = buckets[mid][-1]
            c = dx[other] * (y - ly[other]) - dy[other] * (x - lx[other])
            if c == 0:
                c = dx[other] * vy - dy[other] * vx
            if c > 0:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(buckets):
            return lo, 0
        bucket = buckets[lo]
        low, high = 0, len(bucket)
        while low < high:
            mid = (low + high) // 2
            other = bucket[mid]
            c = dx[other] * (y - ly[other]) - dy[other] * (x - lx[other])
            if c == 0:
                c = dx[other] * vy - dy[other] * vx
            if c > 0:
                low = mid + 1
            else:
                high = mid
        return lo, low

    # Lexicographic endpoints symbolically tilt the sweep past vertical edges.
    # A fly at a vertex is handled by its event, without a separate map.
    last = -1
    boundary = 0
    for point in flies:
        while si < edges or ei < edges:
            start = left[starts[si]] if si < edges else point + 1
            end = right[ends[ei]] if ei < edges else point + 1
            event = min(start, end)
            if event > point:
                break
            last = event
            while ei < edges and right[ends[ei]] == event:
                edge = ends[ei]
                boundary = abs(owner[edge])
                bucket = where[edge]
                del bucket[bucket.index(edge)]
                where[edge] = None
                if not bucket:
                    buckets.remove(bucket)
                ei += 1
            while si < edges and left[starts[si]] == event:
                edge = starts[si]
                boundary = abs(owner[edge])
                b, i = find(edge)
                if b == len(buckets):
                    if not buckets:
                        buckets.append([])
                    b = len(buckets) - 1
                    i = len(buckets[b])
                bucket = buckets[b]
                bucket.insert(i, edge)
                where[edge] = bucket
                if len(bucket) > 2 * LOAD:
                    upper = bucket[LOAD:]
                    del bucket[LOAD:]
                    buckets.insert(b + 1, upper)
                    for moved in upper:
                        where[moved] = upper
                si += 1
        if point == last:
            count[boundary - 1] += 1
            continue
        x = (point >> COORD_BITS) - LIMIT
        y = (point & COORD_MASK) - LIMIT
        lo, hi = 0, len(buckets)
        while lo < hi:
            mid = (lo + hi) // 2
            edge = buckets[mid][-1]
            c = dx[edge] * (y - ly[edge]) - dy[edge] * (x - lx[edge])
            if c > 0:
                lo = mid + 1
            else:
                hi = mid
        if lo == len(buckets):
            continue
        bucket = buckets[lo]
        lo, hi = 0, len(bucket)
        while lo < hi:
            mid = (lo + hi) // 2
            edge = bucket[mid]
            c = dx[edge] * (y - ly[edge]) - dy[edge] * (x - lx[edge])
            if c > 0:
                lo = mid + 1
            else:
                hi = mid
        edge = bucket[lo]
        if owner[edge] > 0 or dx[edge] * (y - ly[edge]) == dy[edge] * (x - lx[edge]):
            count[abs(owner[edge]) - 1] += 1
    sys.stdout.write("\n".join(map(str, count)) + "\n")


main()
