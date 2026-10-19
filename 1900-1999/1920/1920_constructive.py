import sys


def ears(size):
    width = size - size % 2
    for column in range(2, width):
        yield column - 1, size + column - 1, column, size + column
    for row in range(2, size):
        for column in range(0, width, 2):
            upper = (row - 1) * size + column
            lower = row * size + column
            yield upper, upper + 1, lower, lower + 1
    if size % 2:
        for row in range(0, size - 1, 2):
            left = row * size + width - 1
            yield left, left + size, left + 1, left + size + 1


def construct_cycle(size, length):
    if length % 2 or length > size * size - size % 2:
        return None
    successor = [-1] * (size * size)
    initial = [0, 1, size + 1, size]
    for first, second in zip(initial, initial[1:] + initial[:1]):
        successor[first] = second
    additions = ears(size)
    for _ in range((length - len(initial)) // 2):
        first, second, outer_first, outer_second = next(additions)
        if successor[first] != second:
            first, second = second, first
            outer_first, outer_second = outer_second, outer_first
        successor[first] = outer_first
        successor[outer_first] = outer_second
        successor[outer_second] = second
    result = []
    current = 0
    for _ in range(length):
        result.append(divmod(current, size))
        current = successor[current]
    return result


def main():
    size, length = map(int, sys.stdin.buffer.read().split())
    cycle = construct_cycle(size, length)
    if cycle is None:
        print("Unsuitable device")
    else:
        print("Overwhelming power of magic")
        print("\n".join(f"{row + 1} {column + 1}" for row, column in cycle))


if __name__ == "__main__":
    main()
