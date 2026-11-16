from bisect import bisect_left, bisect_right
from math import gcd
from sys import stdin


BITS_PER_BYTE = 8
DENSE_SPAN_LIMIT = 24_000
SPAN_PER_VALUE = 16
LONG_RUN = 64


def dense_progression(values, best, first, step):
    origin = values[0]
    span = values[-1] - origin
    packed = bytearray(span // BITS_PER_BYTE + 1)
    for value in values:
        index, bit = divmod(value - origin, BITS_PER_BYTE)
        packed[index] |= 1 << bit
    occupied = int.from_bytes(packed, "little")

    difference = 1
    while difference * best <= span:
        starts = occupied & (occupied >> difference)
        length = 2
        while starts and length <= best:
            extra = min(length, best + 1 - length)
            starts &= starts >> (difference * extra)
            length += extra
        if not starts:
            difference += 1
            continue
        index = (starts & -starts).bit_length() - 1
        mask = 1 << (index + length * difference)
        while mask & occupied:
            length += 1
            mask <<= difference
        best, first, step = length, origin + index, difference
    return best, first, step


def sparse_progression(values, where, best, first, step):
    # The smallest or largest value must form a three-term progression
    # to improve on two terms. Check only isolated extremes.
    while len(values) > 2:
        low, high = values[0], values[-1]
        if 2 * (high - values[-2]) > values[-2] - low:
            start = bisect_left(values, (low + high + 1) // 2)
            if not any(2 * mid - high in where for mid in values[start:-1]):
                values.pop()
                continue
        if 2 * (values[1] - low) > high - values[1]:
            stop = bisect_right(values, (low + high) // 2)
            if not any(2 * mid - low in where for mid in values[1:stop]):
                values.pop(0)
                continue
        break

    maximum = values[-1]
    scaled_length = 0
    for index, start in enumerate(values):
        if len(values) - index <= best:
            break
        if best != scaled_length:
            scaled_length = best
            scaled = [value * best for value in values]
        offset = (scaled_length - 1) * start
        stop = bisect_right(scaled, maximum + offset)
        # With scaled second term k*y, the required endpoint is k*y-(k-1)*x.
        for target in scaled[index + 1 : stop]:
            if target - offset not in where:
                continue
            second = target // scaled_length
            delta = second - start
            if start - delta in where:
                continue
            following = second + delta
            while following in where:
                following += delta
            length = (following - start) // delta
            if length > best:
                best, first, step = length, start, delta
    return best, first, step


def long_progression(values, where, best, first, step):
    grouped_length = 0
    groups = {}
    for index, start in enumerate(values):
        if len(values) - index <= best:
            break
        if best != grouped_length:
            grouped_length = best
            groups = {}
            for value in values[index:]:
                quotient, residue = divmod(value, grouped_length)
                groups.setdefault(residue, []).append(quotient)
        quotient, residue = divmod(start, grouped_length)
        endpoints = groups[residue]
        # The endpoint k steps away must share the start's residue modulo k.
        anchor = start - quotient
        for endpoint in endpoints[bisect_right(endpoints, quotient) :]:
            second = endpoint + anchor
            if second not in where:
                continue
            delta = second - start
            if start - delta in where:
                continue
            following = second + delta
            while following in where:
                following += delta
            length = (following - start) // delta
            if length > best:
                best, first, step = length, start, delta
    return best, first, step


def progression(values, where):
    if len(values) == 1:
        return 1, values[0], 0

    origin = values[0]
    common = values[1] - origin
    for value in values[2:]:
        if common == 1:
            break
        common = gcd(common, value - origin)
    if common > 1:
        # The occupied values lie on a coarser grid. Searching that grid
        # preserves every progression and can make bit intersections cheap.
        values = [(value - origin) // common for value in values]
        best, first, step = progression_on_grid(values, set(values))
        return best, origin + first * common, step * common
    return progression_on_grid(values, where)


def progression_on_grid(values, where):
    best, first, step = 2, values[0], values[1] - values[0]
    run, difference = 1, 0
    for left, right in zip(values, values[1:]):
        gap = right - left
        run = run + 1 if gap == difference else 2
        difference = gap
        if run > best:
            best, first, step = run, right - (run - 1) * gap, gap
    if best == len(values):
        return best, first, step

    span = values[-1] - values[0]
    if span <= min(DENSE_SPAN_LIMIT, SPAN_PER_VALUE * len(values)):
        return dense_progression(values, best, first, step)
    if best >= LONG_RUN:
        return long_progression(values, where, best, first, step)
    return sparse_progression(values, where, best, first, step)


def main():
    _, *data = map(int, stdin.buffer.read().split())
    where = {value: index for index, value in enumerate(data, 1)}
    best, first, step = progression(sorted(where), where)
    print(best)
    print(*(where[first + index * step] for index in range(best)))


if __name__ == "__main__":
    main()
