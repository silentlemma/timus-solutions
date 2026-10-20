"""Print a deterministic input, including adversarial maximum-size cases."""

import bisect
import heapq
import random
import sys

MAX_SIZE = 30000
VALUE_LIMIT = 10**9
SMALL_SIZE = 40
SMALL_QUERIES = 120
OLD_BLOCK_SIZE = 173
LATE_WIDTH = 32
WIDE_WIDTH = 512
CROSS_MAGNITUDE_MIN = 10000
CROSS_CORE_MIN = 40


def unique(values, left, right):
    ordered = sorted(values[left:right])
    low, high = 0, len(ordered) - 1
    best = 2 * VALUE_LIMIT + 1
    count = 0
    while low < high:
        total = ordered[low] + ordered[high]
        score = abs(total)
        if score < best:
            best, count = score, 1
        elif score == best:
            count += 1
        if total < 0:
            low += 1
        elif total > 0:
            high -= 1
        else:
            low += 1
            high -= 1
    return count == 1


def unique_prefixes(values):
    active = []
    counts = {}
    heap = []
    result = []

    def edge(first, second, delta):
        score = abs(values[first] + values[second])
        counts[score] = counts.get(score, 0) + delta
        if delta > 0:
            heapq.heappush(heap, score)

    for day, value in enumerate(values):
        item = (abs(value), day)
        position = bisect.bisect_left(active, item)
        if position and position < len(active):
            edge(active[position - 1][1], active[position][1], -1)
        if position:
            edge(active[position - 1][1], day, 1)
        if position < len(active):
            edge(day, active[position][1], 1)
        active.insert(position, item)
        while heap and counts[heap[0]] == 0:
            heapq.heappop(heap)
        if heap and counts[heap[0]] == 1:
            result.append(day + 1)
    return result


def generate(mode, seed):
    rng = random.Random(seed)
    if mode in ("late", "late_wide", "cross"):
        head = MAX_SIZE // 2 - 1
        minimum = CROSS_MAGNITUDE_MIN if mode == "cross" else 1
        magnitudes = rng.sample(range(minimum, MAX_SIZE), head)
        if mode == "cross":
            values = [
                value * MAX_SIZE * (-1 if day // OLD_BLOCK_SIZE % 2 == 0 else 1)
                for day, value in enumerate(magnitudes)
            ]
            starts = list(range(0, head - 2 * OLD_BLOCK_SIZE, 2 * OLD_BLOCK_SIZE))
        else:
            values = [value * MAX_SIZE * (1 if rng.randrange(2) else -1) for value in magnitudes]
            starts = list(range(0, head, OLD_BLOCK_SIZE))
        values += [1 - value for value in values]
        values += [-VALUE_LIMIT, VALUE_LIMIT]
        queries = [(start + 1, MAX_SIZE - 2) for start in starts]
        while len(queries) < MAX_SIZE:
            if mode == "cross":
                start = rng.choice(starts)
                left = start + rng.randrange(10)
                right = start + OLD_BLOCK_SIZE + rng.randrange(CROSS_CORE_MIN, OLD_BLOCK_SIZE + 1)
            else:
                width = LATE_WIDTH if mode == "late" else WIDE_WIDTH
                left = rng.randrange(head - width)
                right = min(head, left + OLD_BLOCK_SIZE + rng.randrange(1, width + 1))
            queries.append((left + 1, right))
        return values, queries
    if mode == "small":
        n = rng.randint(2, SMALL_SIZE)
        values = rng.sample(range(-VALUE_LIMIT, VALUE_LIMIT + 1), n)
        queries = []
        for _ in range(SMALL_QUERIES):
            while True:
                left = rng.randrange(n - 1)
                right = rng.randrange(left + 2, n + 1)
                if unique(values, left, right):
                    queries.append((left + 1, right))
                    break
        return values, queries
    if mode == "repeat":
        return [-VALUE_LIMIT, VALUE_LIMIT], [(1, 2)] * MAX_SIZE
    if mode in ("mixed", "ordered", "clustered", "hidden", "dense"):
        n = MAX_SIZE
        if mode in ("hidden", "dense"):
            head = n // (2 if mode == "hidden" else 10)
            tail = rng.sample(range(1, VALUE_LIMIT // n), head)
            tail = [value * n * (1 if rng.randrange(2) else -1) for value in tail]
            values = [1 - value for value in tail] + tail * ((n - head) // head)
        elif mode == "mixed":
            values = rng.sample(range(-VALUE_LIMIT, VALUE_LIMIT), n)
        elif mode == "ordered":
            values = list(range(-n, -n // 2)) + list(range(1, n // 2 + 1))
        elif mode == "clustered":
            values = rng.sample(range(VALUE_LIMIT // 2, VALUE_LIMIT), n)
            values = [value if rng.randrange(2) else -value for value in values]
        width = n // 10
        queries = []
        for _ in range(MAX_SIZE):
            left = rng.randrange(head if mode in ("hidden", "dense") else 0, n - 1)
            right = rng.randrange(min(n, left + width), n + 1)
            queries.append((left + 1, right))
        return values, queries
    n = MAX_SIZE
    magnitudes = rng.sample(range(1, VALUE_LIMIT), n)
    if mode == "positive":
        values = magnitudes
    elif mode == "negative":
        values = [-value for value in magnitudes]
    elif mode in ("cancel", "prefix", "pairs"):
        values = [value if rng.randrange(2) else -value for value in magnitudes]
    else:
        raise ValueError("unknown mode: " + mode)
    queries = []
    if mode == "cancel":
        middle = n // 2
        values[middle - 1] = -VALUE_LIMIT
        values[middle] = VALUE_LIMIT
        for _ in range(MAX_SIZE):
            queries.append((rng.randint(1, middle), rng.randint(middle + 1, n)))
    elif mode == "prefix":
        ends = unique_prefixes(values)
        queries = [(1, rng.choice(ends)) for _ in range(MAX_SIZE)]
    elif mode == "pairs":
        for _ in range(MAX_SIZE):
            left = rng.randint(1, n - 1)
            queries.append((left, left + 1))
    else:
        for _ in range(MAX_SIZE):
            left = rng.randint(1, n - 1)
            queries.append((left, rng.randint(left + 1, n)))
    return values, queries


def main():
    mode, seed = sys.argv[1:]
    values, queries = generate(mode, int(seed))
    print(len(values), len(queries))
    print(*values)
    for left, right in queries:
        print(left, right)


if __name__ == "__main__":
    main()
