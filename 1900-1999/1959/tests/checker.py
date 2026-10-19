import heapq
import sys


SIZE_LIMIT = 100000
SYMBOL_LIMIT = 100000


def check(input_text, output_text):
    data = list(map(int, input_text.split()))
    if not data or not 1 <= data[0] <= SIZE_LIMIT:
        return False, "invalid text size"
    n = data[0]
    if len(data) < n + 2:
        return False, "truncated input"
    m = data[n + 1]
    if not 1 <= m < n or len(data) != n + m + 2:
        return False, "invalid pattern size"
    text, pattern = data[1 : n + 1], data[n + 2 :]
    if any(not 0 <= v <= SYMBOL_LIMIT for v in text + pattern):
        return False, "invalid input symbol"
    text_holes, pattern_holes = 0 in text, 0 in pattern
    if text_holes and pattern_holes:
        return False, "both strings are damaged"
    restored = list(map(int, output_text.split()))
    if len(restored) != n + m:
        return False, "wrong output length"
    if any(not 1 <= v <= SYMBOL_LIMIT for v in restored):
        return False, "output symbol outside range"
    if any(v != 0 and v != r for v, r in zip(text + pattern, restored)):
        return False, "known symbol changed"
    gap = n - m
    if text_holes:
        known = pattern
        queries = [
            (max(0, i - gap), min(m - 1, i), restored[i])
            for i, value in enumerate(text)
            if value == 0
        ]
    else:
        known = text
        queries = [
            (j, j + gap, restored[n + j])
            for j, value in enumerate(pattern)
            if value == 0
        ]
    frequencies = {}
    heap = []
    left, right = 0, -1

    def update(value, delta):
        count = frequencies.get(value, 0) + delta
        frequencies[value] = count
        if count:
            heapq.heappush(heap, (-count, value))

    for begin, end, chosen in queries:
        while right < end:
            right += 1
            update(known[right], 1)
        while left < begin:
            update(known[left], -1)
            left += 1
        while heap and -heap[0][0] != frequencies[heap[0][1]]:
            heapq.heappop(heap)
        if not heap or frequencies.get(chosen, 0) != -heap[0][0]:
            return False, "a restored symbol is not optimal"
    return True, "valid optimal restoration"


def main():
    try:
        with open(sys.argv[1], encoding="utf-8") as stream:
            input_text = stream.read()
        with open(sys.argv[3], encoding="utf-8") as stream:
            output_text = stream.read()
        okay, message = check(input_text, output_text)
    except (OSError, ValueError, IndexError) as error:
        okay, message = False, str(error)
    print(message)
    return 0 if okay else 1


if __name__ == "__main__":
    sys.exit(main())
