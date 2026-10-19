import sys

WINDOW_SIZE = 3


def maximum_window(values):
    current = sum(values[:WINDOW_SIZE])
    best = current
    position = WINDOW_SIZE // 2 + 1
    for start in range(1, len(values) - WINDOW_SIZE + 1):
        current += values[start + WINDOW_SIZE - 1] - values[start - 1]
        if current > best:
            best = current
            position = start + WINDOW_SIZE // 2 + 1
    return best, position


def main():
    tokens = list(map(int, sys.stdin.buffer.read().split()))
    count = tokens[0]
    print(*maximum_window(tokens[1 : count + 1]))


if __name__ == "__main__":
    main()
