import sys
from math import gcd


def visits(step, start, n):
    """When the walk from start is at each node it reaches: a pair (first
    moment, period), with period 0 for a node passed only once."""
    seen = [-1] * (n + 1)
    order = []
    v = start
    while seen[v] < 0:
        seen[v] = len(order)
        order.append(v)
        v = step[v]
    loop_start, period = seen[v], len(order) - seen[v]
    return {u: (t, period if t >= loop_start else 0) for t, u in enumerate(order)}


def first_common(a, b):
    """The least moment in both sets r + k L (k >= 0), or None."""
    (ra, la), (rb, lb) = a, b
    if la == 0 or lb == 0:
        if la == 0 and lb == 0:
            return ra if ra == rb else None
        if la == 0:
            ra, la, rb, lb = rb, lb, ra, la
        # one moment rb against the moments ra, ra + la, ...
        return rb if rb >= ra and (rb - ra) % la == 0 else None
    g = gcd(la, lb)
    if (rb - ra) % g:
        return None
    m = lb // g
    k = (rb - ra) // g * pow(la // g, -1, m) % m if m > 1 else 0
    t, whole = ra + la * k, la // g * lb
    if t < rb:
        t += (rb - t + whole - 1) // whole * whole
    return t


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    left, right = [0] * (n + 1), [0] * (n + 1)
    pos = 1
    for v in range(1, n + 1):
        left[v] = int(data[pos])
        while data[pos] != b"0":
            pos += 1
        right[v] = int(data[pos - 1])
        pos += 1
    a, b = int(data[pos]), int(data[pos + 1])
    # A always takes the leftmost road and B the rightmost
    seen_a, seen_b = visits(left, a, n), visits(right, b, n)
    best = None
    for v, when in seen_a.items():
        if v in seen_b:
            t = first_common(when, seen_b[v])
            if t is not None and (best is None or t < best):
                best = t
    print(-1 if best is None else best)


main()
