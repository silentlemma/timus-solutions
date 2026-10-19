"""Generate seed mode: dense, dense_lower, mitm, dense_mitm; fixed exact area certificates."""

import sys


def append_point(curve, point):
    if curve and curve[-1] == point:
        return
    while len(curve) >= 2:
        (a, x), (b, y) = curve[-2:]
        c, z = point
        if (y - x) * (c - b) != (z - y) * (b - a):
            break
        curve.pop()
    curve.append(point)


def encode(duration, upper, lower):
    return (
        str(duration)
        + "\n"
        + "".join(
            (
                str(len(curve)) + "\n" + "".join((f"{t} {y}\n" for t, y in curve))
                for curve in (upper, lower)
            )
        )
    ).encode()


def maximal(mode):
    if mode in ("dense", "dense_lower"):
        duration = 1000000
        upper, lower = ([], [])
        times = [10 * i for i in range(99999)] + [duration]
        for index, time in enumerate(times):
            baseline = 500000 + (3 if index % 2 and index < 99999 else 0)
            gap = abs(time - duration // 2)
            if mode == "dense":
                upper.append((time, baseline + gap))
                lower.append((time, baseline))
            else:
                upper.append((time, baseline))
                lower.append((time, baseline - gap))
        return (duration, upper, lower)
    weights = [1 << power for power in range(1, 31)]
    weights.insert(29, sum(weights))
    gap = []
    time = 0
    for index, weight in enumerate(weights):
        if index == 29:
            width, height = (99962, 21483)
        else:
            power = weight.bit_length() - 1
            width = 1 if index == 0 else 1 << max(1, power // 2)
            height = weight // width
        assert width * height == weight
        append_point(gap, (time, height if index == 0 else 0))
        if 0 < index < len(weights) - 1:
            append_point(gap, (time + width // 2, height))
        time += width
        append_point(gap, (time, height if index == len(weights) - 1 else 0))
    duration = time
    if mode == "mitm":
        return (duration, [(t, 100000 + y) for t, y in gap], [(0, 100000), (duration, 100000)])
    assert mode == "dense_mitm"
    times = {t for t, _ in gap}
    pointer = added = 0
    for t in range(duration + 1):
        while pointer + 2 < len(gap) and gap[pointer + 1][0] <= t:
            pointer += 1
        a, x = gap[pointer]
        b, y = gap[pointer + 1]
        if (y - x) * (t - a) % (b - a) == 0:
            times.add(t)
            added += 1
            if added == 98000:
                break
    upper, lower = ([], [])
    pointer = 0
    for t in sorted(times):
        while pointer + 2 < len(gap) and gap[pointer + 1][0] <= t:
            pointer += 1
        a, x = gap[pointer]
        b, y = gap[pointer + 1]
        numerator = x * (b - t) + y * (t - a)
        assert numerator % (b - a) == 0
        baseline = 300000 + 10 * (t & 1)
        append_point(upper, (t, baseline + numerator // (b - a)))
        append_point(lower, (t, baseline))
    assert len(upper) <= 100000 and len(lower) <= 100000
    return (duration, upper, lower)


if __name__ == "__main__":
    seed, mode = sys.argv[1:]
    assert int(seed) >= 0
    sys.stdout.buffer.write(encode(*maximal(mode)))
