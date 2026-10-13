import sys
from bisect import bisect_left, bisect_right


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    where = {}  # a value and the number of one element holding it
    for i in range(n):
        where.setdefault(int(data[1 + i]), i + 1)
    a = sorted(where)
    length, first, step = 1, a[0], 1
    if len(a) > 1:
        length, step = 2, a[1] - a[0]
    # An isolated extreme with no three-term progression cannot occur in a longer answer.
    while len(a) > 2:
        low, high = a[0], a[-1]
        if 2 * (high - a[-2]) > a[-2] - low:
            start = bisect_left(a, (low + high + 1) // 2)
            if not any(2 * y - high in where for y in a[start:-1]):
                a.pop()
                continue
        if 2 * (a[1] - low) > high - a[1]:
            stop = bisect_right(a, (low + high) // 2)
            if not any(2 * y - low in where for y in a[1:stop]):
                a.pop(0)
                continue
        break
    hint = run = 1
    previous = 0
    for left, right in zip(a, a[1:]):
        difference = right - left
        run = run + 1 if difference == previous else 2
        previous = difference
        if run > hint:
            hint = run
    maximum = a[-1]
    scaled_length = 0
    for i, x in enumerate(a):
        if len(a) - i <= length:
            break
        bound = max(length, hint - 1)
        if scaled_length != bound:
            scaled_length = bound
            scaled = [v * bound for v in a]
        offset = (scaled_length - 1) * x
        stop = bisect_right(scaled, maximum + offset)
        # Test the required endpoint before walking the progression's prefix.
        for target in scaled[i + 1 : stop]:
            if target - offset not in where:
                continue
            y = target // scaled_length
            d = y - x
            if x - d in where:
                continue
            count, last = 2, y
            while last + d in where:
                last += d
                count += 1
            if count > length:
                length, first, step = count, x, d
    answer = " ".join(str(where[first + k * step]) for k in range(length))
    sys.stdout.write(str(length) + "\n" + answer + "\n")


main()
