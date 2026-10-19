import sys

DECIMAL_BASE = 10
MAX_DIGIT = DECIMAL_BASE - 1


def build_tables(digits):
    maximum = MAX_DIGIT * digits
    ways = [1] + [0] * maximum
    prefix = []
    for length in range(digits):
        running = 0
        row = []
        for count in ways:
            running += count
            row.append(running)
        prefix.append(row)
        if length + 1 == digits:
            break
        next_ways = []
        window = 0
        for total in range(maximum + 1):
            window += ways[total]
            if total >= DECIMAL_BASE:
                window -= ways[total - DECIMAL_BASE]
            next_ways.append(window)
        ways = next_ways
    return prefix


def count_leq(value, target, prefix):
    digits = str(value)
    maximum = len(prefix[0]) - 1
    remaining, result = target, 0
    for position, word in enumerate(digits):
        digit = ord(word) - ord("0")
        row = prefix[len(digits) - position - 1]
        if digit and remaining >= 0:
            result += row[min(maximum, remaining)]
            if remaining >= digit:
                result -= row[min(maximum, remaining - digit)]
        remaining -= digit
        if remaining < 0:
            return result
    return result + (remaining == 0)


def digit_sum(value):
    total = 0
    while value:
        total += value % DECIMAL_BASE
        value //= DECIMAL_BASE
    return total


def solve(number):
    digits = len(str(number))
    prefix = build_tables(digits)
    lower = answer = 0
    for target in range(1, MAX_DIGIT * digits + 1):
        count = count_leq(number, target, prefix)
        if not count:
            continue
        start, end = lower + 1, lower + count
        left, right = start, end
        while left <= right:
            middle = (left + right) // 2
            if middle - count_leq(middle, target, prefix) <= lower:
                left = middle + 1
            else:
                right = middle - 1
        if right >= start and digit_sum(right) == target:
            if right - count_leq(right, target, prefix) == lower:
                answer += 1
        lower += count
    return answer


def main():
    print(solve(int(sys.stdin.buffer.read())))


if __name__ == "__main__":
    main()
