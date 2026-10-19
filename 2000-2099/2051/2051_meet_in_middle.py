from array import array
from bisect import bisect_left
import sys

OUTPUT_CHUNK = 4096


class Curve:
    __slots__ = ("time", "height")

    def __init__(self):
        self.time = array("I")
        self.height = array("I")

    def add(self, time, height):
        times, heights = self.time, self.height
        if times and times[-1] == time:
            return
        while len(times) >= 2:
            a, b = times[-2], times[-1]
            x, y = heights[-2], heights[-1]
            if (y - x) * (time - b) != (height - y) * (b - a):
                break
            times.pop()
            heights.pop()
        times.append(time)
        heights.append(height)


def contacts_of(upper, lower, duration):
    ht, hy, gt, gy = upper.time, upper.height, lower.time, lower.height
    i = j = time = 0
    contacts = []
    while True:
        while i + 2 < len(ht) and ht[i + 1] <= time:
            i += 1
        while j + 2 < len(gt) and gt[j + 1] <= time:
            j += 1
        hn = hy[i] * (ht[i + 1] - time) + hy[i + 1] * (time - ht[i])
        gn = gy[j] * (gt[j + 1] - time) + gy[j + 1] * (time - gt[j])
        hd, gd = ht[i + 1] - ht[i], gt[j + 1] - gt[j]
        if hn * gd == gn * hd and 0 < time < duration:
            contacts.append((time, hn // hd))
        if time == duration:
            return contacts
        time = min(ht[i + 1], gt[j + 1])


def augment(curve, contacts):
    result = Curve()
    times, heights = curve.time, curve.height
    i = j = 0
    while i < len(times) or j < len(contacts):
        if j == len(contacts) or (i < len(times) and times[i] < contacts[j][0]):
            result.time.append(times[i])
            result.height.append(heights[i])
            i += 1
        elif i == len(times) or contacts[j][0] < times[i]:
            result.time.append(contacts[j][0])
            result.height.append(contacts[j][1])
            j += 1
        else:
            result.time.append(times[i])
            result.height.append(heights[i])
            i += 1
            j += 1
    return result


def areas(curve, boundaries):
    times, heights = curve.time, curve.height
    result = []
    total = 0
    region = 1
    for i in range(len(times) - 1):
        total += (heights[i] + heights[i + 1]) * (times[i + 1] - times[i])
        if times[i + 1] == boundaries[region]:
            result.append(total)
            total = 0
            region += 1
    return result


def choose(weights):
    target = sum(weights) // 2
    left_count = len(weights) // 2
    scale = 1 << left_count
    keys = [0]
    for bit, weight in enumerate(weights[:left_count]):
        step = weight * scale + (1 << bit)
        keys.extend([key + step for key in keys])
    keys.sort()
    previous = right_sum = 0
    for index in range(1 << (len(weights) - left_count)):
        gray = index ^ (index >> 1)
        if index:
            changed = gray ^ previous
            bit = changed.bit_length() - 1
            weight = weights[left_count + bit]
            right_sum += weight if gray & changed else -weight
        previous = gray
        need = target - right_sum
        position = bisect_left(keys, need * scale)
        if position < len(keys) and keys[position] // scale == need:
            return (keys[position] & (scale - 1)) | (gray << left_count)
    return 0


def solve(duration, upper, lower):
    contacts = contacts_of(upper, lower, duration)
    boundaries = [0] + [t for t, _ in contacts] + [duration]
    upper, lower = augment(upper, contacts), augment(lower, contacts)
    upper_areas, lower_areas = areas(upper, boundaries), areas(lower, boundaries)
    mask = choose([h - g for h, g in zip(upper_areas, lower_areas)])
    result = [Curve(), Curve()]
    hi = lo = 0
    for region, end in enumerate(boundaries[1:]):
        destination = 0 if mask & (1 << region) else 1
        while hi < len(upper.time) and upper.time[hi] <= end:
            result[destination].add(upper.time[hi], upper.height[hi])
            hi += 1
        while lo < len(lower.time) and lower.time[lo] <= end:
            result[1 - destination].add(lower.time[lo], lower.height[lo])
            lo += 1
        hi -= 1
        lo -= 1
    return result


def read_curve(fields):
    curve = Curve()
    for _ in range(next(fields)):
        curve.time.append(next(fields))
        curve.height.append(next(fields))
    return curve


def write_curve(curve):
    print(len(curve.time))
    for start in range(0, len(curve.time), OUTPUT_CHUNK):
        end = min(len(curve.time), start + OUTPUT_CHUNK)
        sys.stdout.write("".join(f"{curve.time[i]} {curve.height[i]}\n" for i in range(start, end)))


def main():
    fields = iter(map(int, sys.stdin.buffer.read().split()))
    duration = next(fields)
    upper, lower = read_curve(fields), read_curve(fields)
    del fields
    for curve in solve(duration, upper, lower):
        write_curve(curve)


if __name__ == "__main__":
    main()
