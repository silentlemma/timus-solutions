import sys

PERCENT_SCALE = 100


def construct(size, kept, percentage):
    weights = [1] * size
    for position in range(size - kept, size):
        rank = (percentage * position - 1) // PERCENT_SCALE
        weights[position] = weights[rank] + 1
    return weights


def main():
    size, kept, percentage = map(int, sys.stdin.buffer.read().split())
    weights = construct(size, kept, percentage)
    print(sum(weights))
    print(" ".join(map(str, weights)))


if __name__ == "__main__":
    main()
