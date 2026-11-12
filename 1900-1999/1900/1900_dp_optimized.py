from array import array
import sys

INFINITY = 1_000_000_000
INPUT_SIZE = 16384
DIGIT_ZERO = ord("0")
DIGIT_NINE = ord("9")
DECIMAL_BASE = 10


def integers():
    read = sys.stdin.buffer.read
    value = 0
    active = False
    while True:
        data = read(INPUT_SIZE)
        if not data:
            break
        for c in data:
            if DIGIT_ZERO <= c <= DIGIT_NINE:
                value = value * DECIMAL_BASE + c - DIGIT_ZERO
                active = True
            elif active:
                yield value
                value = 0
                active = False
    if active:
        yield value


def main():
    values = integers()
    n, k = next(values), next(values)
    offset = [right * (right + 1) // 2 for right in range(n)]
    cost = array("I", [0]) * (n * (n + 1) // 2)
    for left in range(n - 1):
        for right in range(left + 1, n):
            cost[offset[right] + left] = next(values)
    for left in range(n - 2, -1, -1):
        prefix = 0
        for right in range(left + 1, n):
            index = offset[right] + left
            prefix += cost[index]
            cost[index] = cost[index + 1] + prefix
    span = n - k
    previous = [cost[offset[index]] for index in range(span)]
    current = [0] * span
    parents = array("H", [0]) * (k * span)
    for group in range(2, k + 2):
        parent_base = (group - 2) * span

        def fill(left, right, first, last):
            if left > right:
                return
            middle = (left + right) // 2
            column = offset[group + middle - 1] + group - 1
            best, split = INFINITY, first
            for cut in range(first, min(last, middle) + 1):
                value = previous[cut] + cost[column + cut]
                if value < best:
                    best, split = value, cut
            current[middle] = best
            parents[parent_base + middle] = group - 1 + split
            fill(left, middle - 1, first, split)
            fill(middle + 1, right, split, last)

        fill(0, span - 1, 0, span - 1)
        previous, current = current, previous
    cuts = [0] * k
    end = n
    for group in range(k + 1, 1, -1):
        end = parents[(group - 2) * span + end - group]
        cuts[group - 2] = end
    print(cost[offset[n - 1]] - previous[span - 1])
    print(*cuts)


if __name__ == "__main__":
    main()
