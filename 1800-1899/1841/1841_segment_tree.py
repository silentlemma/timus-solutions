import sys
from array import array


DIGIT_ZERO = ord("0")
MINUS = ord("-")


def main():
    raw = sys.stdin.buffer.read()
    data = array('i')
    value = 0
    sign = 1
    in_number = False
    for byte in raw:
        if byte >= DIGIT_ZERO:
            value = value * 10 + byte - DIGIT_ZERO
            in_number = True
        elif byte == MINUS:
            sign = -1
        elif in_number:
            data.append(value * sign)
            value = 0
            sign = 1
            in_number = False
    if in_number:
        data.append(value * sign)
    del raw
    n = data[0]
    xs = data[1:n + 2]
    pos = n + 2
    speed = array('i', [0]) * n
    walk = array('q', [0]) * (n + 1)
    ends = array('i', [0]) * n
    starts = array('i')
    start_cost = array('q')
    arrival = array('q')
    count = 0
    for seg in range(n):
        rate, m = data[pos], data[pos + 1]
        pos += 2
        speed[seg] = rate
        origin = xs[seg]
        base = walk[seg]
        walk[seg + 1] = base + rate * abs(xs[seg + 1] - origin)
        for _ in range(m):
            x = data[pos]
            cost = base + rate * abs(x - origin)
            starts.append(x)
            start_cost.append(cost)
            arrival.append(cost + data[pos + 1])
            pos += 2
            count += 1
            # A shared vertex belongs to the preceding segment.
            if seg and x == origin:
                ends[seg - 1] += 1
        ends[seg] = count
    del data
    if not count:
        print(walk[n])
        return

    offset = min(xs)
    size = 1 << (max(xs) - offset).bit_length()
    paint = array('i', [n]) * (2 * size)
    land_cost = array('q', [0]) * count
    # Reverse painting finds the first later segment crossing each cable.
    # Each segment includes its last vertex and excludes its first one.
    for seg in range(n - 1, -1, -1):
        first = ends[seg - 1] if seg else 0
        for k in range(first, ends[seg]):
            x = starts[k]
            land = n
            i = x - offset + size
            while i:
                if paint[i] < land:
                    land = paint[i]
                i >>= 1
            land_cost[k] = walk[land] + speed[land] * abs(x - xs[land])
        a, b = xs[seg], xs[seg + 1]
        if a < b:
            lo, hi = a + 1, b + 1
        else:
            lo, hi = b, a
        lo += size - offset
        hi += size - offset
        while lo < hi:
            if lo & 1:
                paint[lo] = seg
                lo += 1
            if hi & 1:
                hi -= 1
                paint[hi] = seg
            lo >>= 1
            hi >>= 1
    del paint, starts, ends, speed, xs

    # Starts are already ordered along the trail; only landings need sorting.
    # At a shared point, apply every landing before starting the next cable.
    landings = sorted(range(count), key=land_cost.__getitem__)
    gain = 0
    k = 0
    for cable in landings:
        at = land_cost[cable]
        while k < count and start_cost[k] < at:
            arrival[k] += gain
            k += 1
        candidate = arrival[cable] - at
        if candidate < gain:
            gain = candidate
    print(walk[n] + gain)


main()
