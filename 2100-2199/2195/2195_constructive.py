import sys


def preorder(parent):
    children = [[] for _ in parent]
    for vertex in range(1, len(parent)):
        children[parent[vertex]].append(vertex)
    order = []
    stack = [0]
    while stack:
        vertex = stack.pop()
        order.append(vertex)
        stack.extend(reversed(children[vertex]))
    return order


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    n = data[0]
    source = [0] + data[1:n]
    target = [0] + data[n:]
    first = preorder(source)
    second = preorder(target)
    mapping = [0] * n
    for left, right in zip(first, second):
        mapping[right] = left

    moves = []
    # Join consecutive preorder subtrees into one path.
    for i in range(1, n):
        if source[first[i]] != first[i - 1]:
            moves.append((first[i], first[i - 1]))
    # Undo the target's path construction using the source labels.
    for i in range(n - 1, 0, -1):
        if target[second[i]] != second[i - 1]:
            moves.append((mapping[second[i]], mapping[target[second[i]]]))
    lines = [str(len(moves))]
    lines.extend(f"{vertex} {parent}" for vertex, parent in moves)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
