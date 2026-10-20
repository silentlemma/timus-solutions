import sys


def main():
    data = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(data)
    heights = [next(data) for _ in range(n)]
    values = set(heights)
    operations = []
    for _ in range(next(data)):
        kind = next(data)
        index = next(data) if kind == 1 else 0
        value = next(data)
        values.add(value)
        operations.append((index, value))

    ranks = {value: index for index, value in enumerate(sorted(values), 1)}
    size = len(ranks)
    heights = [0] + [ranks[value] for value in heights] + [0]
    tree = [0] * (size + 1)
    previous = 0
    # Each active building contributes one, and each active adjacent pair subtracts one.
    for height in heights[1:-1]:
        tree[height] += 1
        if previous:
            tree[min(previous, height)] -= 1
        previous = height
    for index in range(1, size + 1):
        parent = index + (index & -index)
        if parent <= size:
            tree[parent] += tree[index]

    def add(index, delta):
        while index <= size:
            tree[index] += delta
            index += index & -index

    answers = []
    for index, value in operations:
        new = ranks[value]
        if index == 0:
            position = new - 1
            answer = 1
            while position:
                answer -= tree[position]
                position &= position - 1
            answers.append(str(answer))
            continue

        old = heights[index]
        if old == new:
            continue
        add(old, -1)
        add(new, 1)
        for neighbor in (heights[index - 1], heights[index + 1]):
            if neighbor:
                old_min = old if old < neighbor else neighbor
                new_min = new if new < neighbor else neighbor
                if old_min != new_min:
                    add(old_min, 1)
                    add(new_min, -1)
        heights[index] = new

    sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
