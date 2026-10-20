import sys

ABSENT = -1


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    values = [next(data) for _ in range(n)]
    following = [ABSENT] * n
    last = 0
    count = 1
    for position in range(1, n):
        if values[position] > values[last]:
            following[last] = position
            last = position
            count += 1
    following[last] = n

    # Ties select the earliest maximum, which is a staircase element.
    tree = list(range(ABSENT, n))
    for index in range(1, n + 1):
        parent = index + (index & -index)
        if parent <= n:
            left = tree[index]
            right = tree[parent]
            if values[left] > values[right] or (values[left] == values[right] and left < right):
                tree[parent] = left

    answers = []
    for _ in range(next(data)):
        position = next(data) - 1
        increase = next(data)
        if increase == 0:
            answers.append(str(count))
            continue
        values[position] += increase
        value = values[position]
        if following[position] == ABSENT:
            previous = 0
            index = position
            while index:
                candidate = tree[index]
                if values[candidate] > values[previous] or (
                    values[candidate] == values[previous] and candidate < previous
                ):
                    previous = candidate
                index -= index & -index
            if value > values[previous]:
                following[position] = following[previous]
                following[previous] = position
                count += 1

        if following[position] != ABSENT:
            successor = following[position]
            while successor < n and values[successor] <= value:
                removed = successor
                successor = following[removed]
                following[removed] = ABSENT
                count -= 1
            following[position] = successor

        index = position + 1
        while index <= n:
            candidate = tree[index]
            if candidate != position:
                if value > values[candidate] or (
                    value == values[candidate] and position < candidate
                ):
                    tree[index] = position
                else:
                    break
            index += index & -index
        answers.append(str(count))

    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
