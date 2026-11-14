import sys


def rank_permutation(permutation):
    size = len(permutation)
    positions = [0] * (size + 1)
    for position, value in enumerate(permutation, 1):
        positions[value] = position
    tree = [0] * (size + 1)
    rank = 0
    for value in range(1, size + 1):
        position = positions[value]
        left = 0
        index = position - 1
        while index:
            left += tree[index]
            index &= index - 1
        index = position
        while index <= size:
            tree[index] += 1
            index += index & -index
        offset = left if rank & 1 else value - 1 - left
        rank = rank * value + offset
    return rank + 1


def main():
    fields = iter(map(int, sys.stdin.buffer.read().split()))
    size = next(fields)
    print(rank_permutation([next(fields) for _ in range(size)]))


if __name__ == "__main__":
    main()
