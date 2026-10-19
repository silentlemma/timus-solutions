import sys


def solve(values, first, second):
    total = sum(values)
    score = 0
    if first == second:
        left = 0
        for i in range(first):
            left += values[i]
        right = total - left - values[first]
        score = values[first] + max(left, right)
    elif first < second:
        for i in range((first + second) // 2 + 1):
            score += values[i]
    else:
        for i in range((first + second + 1) // 2, len(values)):
            score += values[i]
    return score, total - score


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    first, second = next(tokens) - 1, next(tokens) - 1
    print(*solve(values, first, second))


if __name__ == "__main__":
    main()
