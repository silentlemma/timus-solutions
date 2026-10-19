import sys

SMALL_PRIMES = (2, 3, 5)
MAX_THREE_WEIGHT = 3
FIVE_WEIGHT = 4


def hall(value, groups):
    weights = (1, min(groups - 1, MAX_THREE_WEIGHT), FIVE_WEIGHT)
    color = 0
    for prime, weight in zip(SMALL_PRIMES, weights):
        while value % prime == 0:
            value //= prime
            color += weight
    return color % groups + 1


def assign(values, groups):
    return [hall(value, groups) for value in values]


if __name__ == "__main__":
    words = iter(map(int, sys.stdin.buffer.read().split()))
    size, groups = next(words), next(words)
    answer = assign([next(words) for _ in range(size)], groups)
    sys.stdout.write("Yes\n" + "\n".join(map(str, answer)) + "\n")
