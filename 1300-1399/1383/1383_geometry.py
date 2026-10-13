import sys
from array import array
from collections import Counter
from math import gcd

COORD_LIMIT = 1000
COORD_BITS = 11
COORD_SPAN = 1 << COORD_BITS
COORD_MASK = COORD_SPAN - 1
FRAME_BITS = 25
FRAME_SPAN = 1 << FRAME_BITS
FRAME_HALF = FRAME_SPAN // 2
FRAME_MASK = FRAME_SPAN - 1


def hull(points):
    """Strict counterclockwise hull of sorted packed points."""
    lower, upper = [], []
    previous = -1
    distinct = 0
    for packed in points:
        if packed == previous:
            continue
        previous = packed
        distinct += 1
        x, y = packed >> COORD_BITS, packed & COORD_MASK
        p = (x, y)
        while len(lower) >= 2:
            ax, ay = lower[-2]
            bx, by = lower[-1]
            if (bx - ax) * (y - ay) > (by - ay) * (x - ax):
                break
            lower.pop()
        lower.append(p)
        while len(upper) >= 2:
            ax, ay = upper[-2]
            bx, by = upper[-1]
            if (bx - ax) * (y - ay) < (by - ay) * (x - ax):
                break
            upper.pop()
        upper.append(p)
    if len(lower) == 1:
        return lower, distinct
    return lower[:-1] + upper[:0:-1], distinct


def edge_tokens(h):
    """Consecutive edge recurrences determine the hull up to an affine map."""
    k = len(h)
    edges = [(h[(i + 1) % k][0] - x, h[(i + 1) % k][1] - y)
             for i, (x, y) in enumerate(h)]
    tokens = []
    for i, (ax, ay) in enumerate(edges):
        bx, by = edges[(i + 1) % k]
        cx, cy = edges[(i + 2) % k]
        a = ax * by - ay * bx
        b = ax * cy - ay * cx
        c = bx * cy - by * cx
        g = gcd(a, b, c)
        tokens.append((a // g, b // g, c // g))
    return tokens


def least_rotation(tokens):
    k = len(tokens)
    doubled = tokens + tokens
    i, j, matched = 0, 1, 0
    while i < k and j < k and matched < k:
        a, b = doubled[i + matched], doubled[j + matched]
        if a == b:
            matched += 1
            continue
        if a > b:
            i += matched + 1
            if i <= j:
                i = j + 1
        else:
            j += matched + 1
            if j <= i:
                j = i + 1
        matched = 0
    return min(i, j)


def rotations(tokens, start):
    k = len(tokens)
    prefix = [0] * k
    for i in range(1, k):
        j = prefix[i - 1]
        while j and tokens[i] != tokens[j]:
            j = prefix[j - 1]
        if tokens[i] == tokens[j]:
            j += 1
        prefix[i] = j
    period = k - prefix[-1]
    if k % period:
        period = k
    return [(start + i) % k for i in range(0, k, period)]


def in_frame(points, o, nxt, prv):
    ox, oy = o
    ax, ay = nxt[0] - ox, nxt[1] - oy
    bx, by = prv[0] - ox, prv[1] - oy
    unit = gcd(ax, ay, bx, by)
    ax, ay, bx, by = ax // unit, ay // unit, bx // unit, by // unit
    d = (ax * by - ay * bx) * unit
    g = d
    for p in points:
        x, y = (p >> COORD_BITS) - ox, (p & COORD_MASK) - oy
        g = gcd(g, x * by - y * bx, ax * y - ay * x)
        if g == 1:
            break
    xc, yc = by * FRAME_SPAN - ay, ax - bx * FRAME_SPAN
    offset = (FRAME_HALF - ox * by + oy * bx) * FRAME_SPAN
    offset += FRAME_HALF - ax * oy + ay * ox
    packed = [(p >> COORD_BITS) * xc + (p & COORD_MASK) * yc + offset for p in points]
    if g != 1:
        packed = [(((v >> FRAME_BITS) - FRAME_HALF) // g + FRAME_HALF) * FRAME_SPAN
                  + ((v & FRAME_MASK) - FRAME_HALF) // g + FRAME_HALF for v in packed]
    packed.sort()
    return d // g, array('q', packed).tobytes()


def canonical(points):
    points.sort()
    h, distinct = hull(points)
    k = len(h)
    if k == 1:
        return (0,)
    if k == 2:
        a, b = h
        if a[0] != b[0]:
            values = [(p >> COORD_BITS) - a[0] for p in points]
            den = b[0] - a[0]
        else:
            values = [(p & COORD_MASK) - a[1] for p in points]
            den = b[1] - a[1]
        g = gcd(den, *values)
        values = [v // g for v in values]
        den //= g
        backward = [den - v for v in reversed(values)]
        return 1, den, array('q', min(values, backward)).tobytes()
    tokens = edge_tokens(h)
    if distinct == k:
        counts = Counter(points) if k != len(points) else None
        tokens = [token + (counts[(x << COORD_BITS) + y] if counts else 1,)
                  for token, (x, y) in zip(tokens, h)]
        start = least_rotation(tokens)
        values = (v for token in tokens[start:] + tokens[:start] for v in token)
        return 2, k, array('q', values).tobytes()
    start = least_rotation(tokens)
    candidates = rotations(tokens, start)
    if len(candidates) > 1:
        sx = sum(p >> COORD_BITS for p in points)
        sy = sum(p & COORD_MASK for p in points)
        m = len(points)
        centers = []
        for i in candidates:
            ox, oy = h[i]
            ax, ay = h[(i + 1) % k][0] - ox, h[(i + 1) % k][1] - oy
            bx, by = h[i - 1][0] - ox, h[i - 1][1] - oy
            d = ax * by - ay * bx
            x, y = sx - m * ox, sy - m * oy
            s, t = x * by - y * bx, ax * y - ay * x
            g = gcd(d, s, t)
            centers.append((d // g, s // g, t // g))
        best = min(centers)
        candidates = [i for i, center in zip(candidates, centers) if center == best]
    if len(candidates) > 1:
        x, y = points[0] >> COORD_BITS, points[0] & COORD_MASK
        gx, gy = 0, 0
        for p in points:
            gx = gcd(gx, (p >> COORD_BITS) - x)
            gy = gcd(gy, (p & COORD_MASK) - y)
            if gx == 1 and gy == 1:
                break
        if gx > 1 or gy > 1:
            gx, gy = max(gx, 1), max(gy, 1)
            points = [((p >> COORD_BITS) // gx) * COORD_SPAN
                      + (p & COORD_MASK) // gy for p in points]
            h = [(x // gx, y // gy) for x, y in h]
    best = None
    for i in candidates:
        key = in_frame(points, h[i], h[(i + 1) % k], h[i - 1])
        if best is None or key < best:
            best = key
    return 2, k, best


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    pos = 1
    buckets = {}
    for project in range(1, n + 1):
        m = data[pos]
        pos += 1
        points = [(data[pos + 2 * j] + COORD_LIMIT) * COORD_SPAN
                  + data[pos + 2 * j + 1] + COORD_LIMIT for j in range(m)]
        pos += 2 * m
        buckets.setdefault(m, []).append((project, points))
    del data
    out = []
    for m in sorted(buckets):
        projects = buckets[m]
        if len(projects) == 1:
            out.append(str(projects[0][0]) + ' 0')
            continue
        classes = {}
        for project, points in projects:
            key = canonical(points)
            classes.setdefault(key, []).append(project)
        for group in classes.values():
            out.append(' '.join(map(str, group)) + ' 0')
    sys.stdout.write(str(len(out)) + '\n' + '\n'.join(out) + '\n')


main()
