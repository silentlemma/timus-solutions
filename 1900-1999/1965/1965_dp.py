import sys


def fixed_directions(values, first_direction, second_direction):
    size = len(values)
    empty_first = 0 if first_direction == 1 else size + 1
    empty_second = 0 if second_direction == 1 else size + 1
    other_first, other_second = empty_second, empty_first
    parent_first = bytearray(size)
    parent_second = bytearray(size)
    previous = values[0]
    for index in range(1, size):
        value = values[index]
        next_first = next_second = None
        if other_first is not None and first_direction * (value - previous) > 0:
            next_first = other_first
            parent_first[index] = 0
        if other_second is not None and first_direction * (value - other_second) > 0:
            if next_first is None or second_direction * (previous - next_first) < 0:
                next_first = previous
                parent_first[index] = 1
        if other_second is not None and second_direction * (value - previous) > 0:
            next_second = other_second
            parent_second[index] = 1
        if other_first is not None and second_direction * (value - other_first) > 0:
            if next_second is None or first_direction * (previous - next_second) < 0:
                next_second = previous
                parent_second[index] = 0
        if next_first is None and next_second is None:
            return None
        other_first, other_second = next_first, next_second
        previous = value
    owner = 0 if other_first is not None else 1
    groups = [[], []]
    for index in range(size - 1, -1, -1):
        groups[owner].append(values[index])
        owner = parent_first[index] if owner == 0 else parent_second[index]
    groups[0].reverse()
    groups[1].reverse()
    if not groups[0]:
        groups[0].append(groups[1].pop())
    if not groups[1]:
        groups[1].append(groups[0].pop())
    return groups


def partition(values):
    for first, second in ((1, 1), (-1, -1), (1, -1), (-1, 1)):
        result = fixed_directions(values, first, second)
        if result is not None:
            return result
    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    size = data[0]
    groups = partition(data[1 : size + 1])
    if groups is None:
        print('Fail')
    else:
        print(len(groups[0]), len(groups[1]))
        print(*groups[0])
        print(*groups[1])


if __name__ == '__main__':
    main()
