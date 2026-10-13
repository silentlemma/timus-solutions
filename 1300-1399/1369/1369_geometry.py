import math
import sys
from array import array
from bisect import bisect_left

LEAF = 32
SLACK = 1e-6
RELATIVE_SLACK = 1e-14
RING_WIDTH = 1.001
COORD_LIMIT = 10000
RING_FRACTION = 0.9
CORRELATION = 0.5
CENTERED_FRACTION = 0.98
SAMPLES = 1024
OUTLIER_RADIUS = 16
DIRECT_ANGLE = 0.1
ANGLE_SLACK = 1e-7
SCALE = 30
UNIT = 10**SCALE
EPS_BITS = 24
EPS = UNIT * UNIT >> EPS_BITS
POW10 = [10**i for i in range(SCALE + 1)]


def exact(s):
    if b'e' not in s and b'E' not in s:
        dot = s.find(b'.')
        if dot < 0:
            return int(s) * UNIT
        frac = s[dot + 1:dot + 1 + SCALE]
        return int(s[:dot] + frac or b'0') * POW10[SCALE - len(frac)]
    mantissa, _, exponent = s.decode().lower().partition('e')
    negative = mantissa.startswith('-')
    whole, _, frac = mantissa.lstrip('+-').partition('.')
    digits = whole + frac
    shift = SCALE - len(frac) + int(exponent or '0')
    if shift >= 0:
        value = int(digits or '0') * 10**shift
    else:
        value = int(digits[:max(0, len(digits) + shift)] or '0')
    return -value if negative else value


def is_ring(radii):
    sample = sorted(radii[::max(1, len(radii) // 10)])
    middle = sample[len(sample) // 2]
    if middle == 0:
        return False
    low, high = middle / RING_WIDTH, middle * RING_WIDTH
    return sum(low <= r <= high for r in radii) >= RING_FRACTION * len(radii)


def main():
    tokens = sys.stdin.buffer.read().split()
    m = int(tokens[0])
    qpos = 2 * m + 1
    n = int(tokens[qpos])
    if n == 0:
        return
    xs = array('d', (float(tokens[2 * i + 1]) for i in range(m)))
    ys = array('d', (float(tokens[2 * i + 2]) for i in range(m)))
    ox = (min(xs) + max(xs)) / 2
    oy = (min(ys) + max(ys)) / 2
    radii = array('d', ((xs[i] - ox)**2 + (ys[i] - oy)**2 for i in range(m)))
    ring = is_ring(radii)
    if m > 2:
        a, b, c = 0, m // 2, m - 1
        ax, ay = xs[a], ys[a]
        dx, dy = xs[b] - ax, ys[b] - ay
        cx, cy = xs[c] - ax, ys[c] - ay
        det = 2 * (dx * cy - dy * cx)
        if det:
            length = dx * dx + dy * dy
            other = cx * cx + cy * cy
            nx = ax + (cy * length - dy * other) / det
            ny = ay + (dx * other - cx * length) / det
            if abs(nx) <= COORD_LIMIT and abs(ny) <= COORD_LIMIT:
                fitted = array('d', ((xs[i] - nx)**2 + (ys[i] - ny)**2 for i in range(m)))
                if is_ring(fitted):
                    ox, oy, radii, ring = nx, ny, fitted, True
    if not ring and m > 2:
        a = min(range(m), key=xs.__getitem__)
        b = max(range(m), key=xs.__getitem__)
        ax, ay = xs[a], ys[a]
        dx, dy = xs[b] - ax, ys[b] - ay
        cross = 0.0
        third = a
        for i in range(m):
            area = abs(dx * (ys[i] - ay) - dy * (xs[i] - ax))
            if area > cross:
                cross, third = area, i
        cx, cy = xs[third] - ax, ys[third] - ay
        det = 2 * (dx * cy - dy * cx)
        if det:
            length = dx * dx + dy * dy
            other = cx * cx + cy * cy
            nx = ax + (cy * length - dy * other) / det
            ny = ay + (dx * other - cx * length) / det
            if abs(nx) <= COORD_LIMIT and abs(ny) <= COORD_LIMIT:
                ox, oy = nx, ny
                radii = array('d', ((xs[i] - ox)**2 + (ys[i] - oy)**2 for i in range(m)))
                ring = is_ring(radii)
    mx, my = sum(xs) / m, sum(ys) / m
    sample = sorted(radii[::max(1, m // 10)])
    middle = sample[len(sample) // 2]
    if (mx - ox)**2 + (my - oy)**2 > middle * CENTERED_FRACTION:
        ring = False
    bx, by = xs, ys
    cosine, sine = 1.0, 0.0
    # Align elongated clouds with the boxes to keep distant queries cheap.
    if not ring:
        sample = range(0, m, max(1, m // SAMPLES))
        sx = sorted(xs[i] for i in sample)
        sy = sorted(ys[i] for i in sample)
        cx, cy = sx[len(sx) // 2], sy[len(sy) // 2]
        spread = sorted((xs[i] - cx)**2 + (ys[i] - cy)**2 for i in sample)
        radius = OUTLIER_RADIUS * spread[len(spread) // 2]
        sample = [i for i in sample if (xs[i] - cx)**2 + (ys[i] - cy)**2 <= radius]
        cx = sum(xs[i] for i in sample) / len(sample)
        cy = sum(ys[i] for i in sample) / len(sample)
        xx = yy = xy = 0.0
        for i in sample:
            dx, dy = xs[i] - cx, ys[i] - cy
            xx += dx * dx
            yy += dy * dy
            xy += dx * dy
        if abs(xy) > CORRELATION * math.sqrt(xx * yy):
            angle = math.atan2(2 * xy, xx - yy) / 2
            cosine, sine = math.cos(angle), math.sin(angle)
            bx = array('d', (cosine * xs[i] + sine * ys[i] for i in range(m)))
            by = array('d', (cosine * ys[i] - sine * xs[i] for i in range(m)))
    order = list(range(m))
    # Angular intervals and radial minima give tight bounds across empty circles.
    if ring:
        angles = array('d', (math.atan2(ys[i] - oy, xs[i] - ox) for i in range(m)))
        order.sort(key=angles.__getitem__)
        polar_angles = array('d', (angles[i] for i in order))
        ux = array('d', ((xs[i] - ox) / math.sqrt(radii[i]) if radii[i]
                         else math.cos(angles[i]) for i in range(m)))
        uy = array('d', ((ys[i] - oy) / math.sqrt(radii[i]) if radii[i]
                         else math.sin(angles[i]) for i in range(m)))
    size = 2
    while size * LEAF < 2 * m:
        size *= 2
    lo = array('i', [0]) * size
    hi = array('i', [0]) * size
    xmin = array('d', [0]) * size
    xmax = array('d', [0]) * size
    ymin = array('d', [0]) * size
    ymax = array('d', [0]) * size
    rmin = array('d', [0]) * size

    # Only leaves contain points; all bounds and leaf ranges are flat arrays.
    def build(v, a, b, axis):
        lo[v], hi[v] = a, b
        if b - a <= LEAF:
            i = order[a]
            lx = hx = bx[i]
            ly = hy = by[i]
            radius = radii[i]
            for j in range(a + 1, b):
                i = order[j]
                x, y = bx[i], by[i]
                if x < lx:
                    lx = x
                if x > hx:
                    hx = x
                if y < ly:
                    ly = y
                if y > hy:
                    hy = y
                if radii[i] < radius:
                    radius = radii[i]
            xmin[v], xmax[v], ymin[v], ymax[v] = lx, hx, ly, hy
            rmin[v] = radius
            return
        if not ring:
            order[a:b] = sorted(order[a:b], key=(by if axis else bx).__getitem__)
        mid = (a + b) // 2
        left, right = 2 * v, 2 * v + 1
        build(left, a, mid, 1 - axis)
        build(right, mid, b, 1 - axis)
        xmin[v] = min(xmin[left], xmin[right])
        xmax[v] = max(xmax[left], xmax[right])
        ymin[v] = min(ymin[left], ymin[right])
        ymax[v] = max(ymax[left], ymax[right])
        rmin[v] = min(rmin[left], rmin[right])

    build(1, 0, m, 0)
    order = array('i', order)
    min_radius, max_radius = math.sqrt(min(radii)), math.sqrt(max(radii))
    out = []
    previous = 0
    for qi in range(n):
        pos = qpos + 1 + 2 * qi
        x, y = float(tokens[pos]), float(tokens[pos + 1])
        tx, ty = cosine * x + sine * y, cosine * y - sine * x
        old_previous = previous
        if ring:
            qx, qy = x - ox, y - oy
            qr = qx * qx + qy * qy
            qa, qlen = math.atan2(qy, qx), math.sqrt(qr)
            at = bisect_left(polar_angles, qa)
            previous = order[at % m]
        dx, dy = xs[previous] - x, ys[previous] - y
        best = dx * dx + dy * dy
        candidates = [previous]
        if ring:
            for i in (old_previous, order[(at - 1) % m]):
                dx, dy = xs[i] - x, ys[i] - y
                d = dx * dx + dy * dy
                if d < best:
                    best, previous = d, i
                    candidates.append(i)
        stack = [1]
        bounds = [0.0]
        limit = best + SLACK + RELATIVE_SLACK * best
        if ring and qlen and min_radius:
            radius = min(max_radius, max(min_radius, math.sqrt(max(0, qr - limit))))
            cosine_bound = (qr + radius * radius - limit) / (2 * qlen * radius)
            window = math.acos(max(-1, min(1, cosine_bound))) + ANGLE_SLACK
            # A thin angular cap can be scanned directly without descending the tree.
            if window <= DIRECT_ANGLE or window >= math.pi:
                if window >= math.pi:
                    ranges = [(0, m)]
                else:
                    low, high = qa - window, qa + window
                    if low < -math.pi:
                        ranges = [(0, bisect_left(polar_angles, high)),
                                  (bisect_left(polar_angles, low + math.tau), m)]
                    elif high > math.pi:
                        ranges = [(bisect_left(polar_angles, low), m),
                                  (0, bisect_left(polar_angles, high - math.tau))]
                    else:
                        ranges = [(bisect_left(polar_angles, low),
                                   bisect_left(polar_angles, high))]
                for a, b in ranges:
                    for j in range(a, b):
                        i = order[j]
                        dx, dy = xs[i] - x, ys[i] - y
                        d = dx * dx + dy * dy
                        if d <= limit:
                            if d < best:
                                best, previous = d, i
                                limit = best + SLACK + RELATIVE_SLACK * best
                            candidates.append(i)
                stack.clear()
        while stack:
            v = stack.pop()
            lower = bounds.pop()
            if lower > limit:
                continue
            if hi[v] - lo[v] <= LEAF:
                for j in range(lo[v], hi[v]):
                    i = order[j]
                    dx, dy = xs[i] - x, ys[i] - y
                    d = dx * dx + dy * dy
                    if d <= limit:
                        if d < best:
                            best, previous = d, i
                            limit = best + SLACK + RELATIVE_SLACK * best
                        candidates.append(i)
            else:
                child_bounds = []
                for child in (2 * v, 2 * v + 1):
                    dx = xmin[child] - tx if tx < xmin[child] else tx - xmax[child]
                    dy = ymin[child] - ty if ty < ymin[child] else ty - ymax[child]
                    if dx < 0:
                        dx = 0
                    if dy < 0:
                        dy = 0
                    lower = dx * dx + dy * dy
                    if ring:
                        a, b = order[lo[child]], order[hi[child] - 1]
                        if angles[a] <= qa <= angles[b]:
                            projection = qlen
                        else:
                            projection = max(qx * ux[a] + qy * uy[a],
                                             qx * ux[b] + qy * uy[b])
                        radius = math.sqrt(rmin[child])
                        # Minimize the distance over the node's angular and radial ranges.
                        radial = (qr + rmin[child] - 2 * radius * projection
                                  if projection <= radius else qr - projection * projection)
                        if radial > lower:
                            lower = radial
                    child_bounds.append(lower)
                left, right = 2 * v, 2 * v + 1
                dl, dr = child_bounds
                if dl < dr:
                    if dr <= limit:
                        stack.append(right)
                        bounds.append(dr)
                    if dl <= limit:
                        stack.append(left)
                        bounds.append(dl)
                else:
                    if dl <= limit:
                        stack.append(left)
                        bounds.append(dl)
                    if dr <= limit:
                        stack.append(right)
                        bounds.append(dr)
        candidates = set(i for i in candidates
                         if (xs[i] - x)**2 + (ys[i] - y)**2 <= limit)
        if len(candidates) == 1:
            out.append(str(previous + 1))
            continue
        # Floating bounds retain every possible tie; only these candidates need decimals.
        qx, qy = exact(tokens[pos]), exact(tokens[pos + 1])
        distances = []
        ids = []
        for i in candidates:
            dx = exact(tokens[2 * i + 1]) - qx
            dy = exact(tokens[2 * i + 2]) - qy
            distances.append(dx * dx + dy * dy)
            ids.append(i + 1)
        bound = min(distances) + EPS
        answer = sorted(i for i, d in zip(ids, distances) if d < bound)
        out.append(' '.join(map(str, answer)))
    sys.stdout.write('\n'.join(out) + '\n')


main()
