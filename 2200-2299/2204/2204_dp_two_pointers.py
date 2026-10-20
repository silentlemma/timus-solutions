import sys

OPTIONS = 2
EXAM_FIELDS = 2 * OPTIONS


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, m = data[:2]
    trip_start = 2 + EXAM_FIELDS * n
    trip_left = data[trip_start::2]
    trip_right = data[trip_start + 1 :: 2]
    cost = (0, 0)
    last = (-1, -1)
    first = end = 0

    for exam in range(2, trip_start, EXAM_FIELDS):
        next_cost = []
        next_last = []
        for offset in range(0, EXAM_FIELDS, 2):
            left, right = data[exam + offset : exam + offset + 2]
            while first < m and trip_right[first] < left:
                first += 1
            while end < m and trip_left[end] <= right:
                end += 1
            count = end - first
            # A shared boundary trip must be counted only once.
            take_first = cost[0] - (count > 0 and last[0] == first)
            take_second = cost[1] - (count > 0 and last[1] == first)
            next_cost.append(count + min(take_first, take_second))
            next_last.append(end - 1 if count else -1)
        cost = next_cost
        last = next_last

    print(m - min(cost))


if __name__ == "__main__":
    main()
