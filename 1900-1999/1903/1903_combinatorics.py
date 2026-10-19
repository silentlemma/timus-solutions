import sys

MODULUS = 1_000_000_007


def count_sets(classes, selected, identified, position):
    n = len(classes)
    pivot = classes[identified]
    lower = sum(value < pivot for value in classes)
    greater = sum(value > pivot for value in classes)
    factorial = [1] * n
    for value in range(1, n):
        factorial[value] = factorial[value - 1] * value % MODULUS
    inverse = [1] * n
    inverse[-1] = pow(factorial[-1], MODULUS - 2, MODULUS)
    for value in range(n - 1, 0, -1):
        inverse[value - 1] = inverse[value] * value % MODULUS

    def choose(total, take):
        if take < 0 or take > total:
            return 0
        return (
            factorial[total] * inverse[take] % MODULUS * inverse[total - take] % MODULUS
        )

    others = n - 1
    answer = choose(others, selected - 1)
    for count in range(position, min(lower, selected - 1) + 1):
        answer -= choose(lower, count) * choose(others - lower, selected - 1 - count)
        answer %= MODULUS
    for count in range(selected - position + 1, min(greater, selected - 1) + 1):
        answer -= choose(greater, count) * choose(
            others - greater, selected - 1 - count
        )
        answer %= MODULUS
    return answer


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, selected = next(tokens), next(tokens)
    classes = [next(tokens) for _ in range(n)]
    identified, position = next(tokens) - 1, next(tokens)
    print(count_sets(classes, selected, identified, position))


if __name__ == "__main__":
    main()
