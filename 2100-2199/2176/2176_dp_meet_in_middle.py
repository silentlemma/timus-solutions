import sys
from bisect import bisect_left

TERNARY_BASE = 3
BYTE_BITS = 8
MAX_DP_SUM = 50_000_000


def beautiful_numbers(limit):
    result = []
    stack = [(1, 1)]
    while stack:
        value, pattern = stack.pop()
        if bin(pattern)[2:] in bin(value):
            result.append(value)
        child = value * TERNARY_BASE
        if child <= limit:
            stack.append((child, pattern * 2))
            if child + 1 <= limit:
                stack.append((child + 1, pattern * 2 + 1))
    result.sort()
    return result


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    queries = data[1:]
    beautiful = beautiful_numbers(max(queries))

    small_total = 0
    split = 0
    while split < len(beautiful) and small_total + beautiful[split] <= MAX_DP_SUM:
        small_total += beautiful[split]
        split += 1

    # Each shift adds the current number once to all earlier subset sums.
    reachable = 1
    for value in beautiful[:split]:
        reachable |= reachable << value
    reachable = reachable.to_bytes(small_total // BYTE_BITS + 1, "little")

    high_sums = [0]
    for value in beautiful[split:]:
        high_sums += [total + value for total in high_sums]
    high_sums.sort()

    answers = []
    for target in queries:
        first = bisect_left(high_sums, target - small_total)
        answer = "NO"
        for index in range(first, len(high_sums)):
            remainder = target - high_sums[index]
            if remainder < 0:
                break
            if (reachable[remainder // BYTE_BITS] >> (remainder % BYTE_BITS)) & 1:
                answer = "YES"
                break
        answers.append(answer)
    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
