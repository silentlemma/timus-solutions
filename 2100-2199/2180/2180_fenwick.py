import sys
from bisect import bisect_left, bisect_right


DIRECT = 0
SUBTREE = 1
LIMITED = 2
QUERY = 3


def main():
    data = iter(sys.stdin.buffer.read().split())
    n = int(next(data))
    parents = [0] * (n + 1)
    children = [[] for _ in range(n + 1)]
    depth = [0] * (n + 1)
    for vertex in range(2, n + 1):
        parent = int(next(data))
        parents[vertex] = parent
        children[parent].append(vertex)
        depth[vertex] = depth[parent] + 1

    deepest = depth.copy()
    size = [1] * (n + 1)
    for vertex in range(n, 1, -1):
        parent = parents[vertex]
        size[parent] += size[vertex]
        if deepest[vertex] > deepest[parent]:
            deepest[parent] = deepest[vertex]

    entry = [0] * (n + 1)
    stack = [1]
    timer = 0
    while stack:
        vertex = stack.pop()
        timer += 1
        entry[vertex] = timer
        stack.extend(children[vertex])
    del children, parents, stack

    operations = []
    queried = set()
    has_limited = False
    q = int(next(data))
    for _ in range(q):
        command = next(data)
        vertex = int(next(data))
        if command == b"?":
            operations.append((QUERY, vertex, 0, 0))
            queried.add(vertex)
            continue
        access = int(next(data))
        value = int(next(data))
        limit = depth[vertex] + access
        if access == 0:
            kind = DIRECT
        elif limit >= deepest[vertex]:
            kind = SUBTREE
        else:
            kind = LIMITED
            has_limited = True
        operations.append((kind, vertex, limit, value))
    del data, deepest

    if not queried:
        return

    # Only vertices that are ever queried need a position in the trees.
    positions = [0] * (n + 1)
    for vertex in queried:
        positions[entry[vertex]] = 1
    for index in range(1, n + 1):
        positions[index] += positions[index - 1]
    count = positions[n]
    coordinates = [[] for _ in range(count + 1)]
    if has_limited:
        for vertex in queried:
            index = positions[entry[vertex]]
            while index:
                coordinates[index].append(depth[vertex])
                index &= index - 1
    del queried

    trees = [[] for _ in range(count + 1)]
    for index in range(1, count + 1):
        if coordinates[index]:
            coordinates[index] = sorted(set(coordinates[index]))
            trees[index] = [0] * (len(coordinates[index]) + 1)

    direct = [0] * (n + 1)
    ordinary = [0] * (count + 1)
    answers = []
    for kind, vertex, limit, value in operations:
        if kind == DIRECT:
            direct[vertex] += value
        elif kind == QUERY:
            position = positions[entry[vertex]]
            answer = direct[vertex]
            level = depth[vertex]
            while position:
                answer += ordinary[position]
                coords = coordinates[position]
                index = bisect_left(coords, level) + 1
                tree = trees[position]
                length = len(tree)
                while index < length:
                    answer += tree[index]
                    index += index & -index
                position &= position - 1
            answers.append(str(answer))
        else:
            # Euler differences confine every addition to its subtree.
            left = positions[entry[vertex] - 1] + 1
            right = positions[entry[vertex] + size[vertex] - 1] + 1
            if left == right:
                continue
            for endpoint, delta in ((left, value), (right, -value)):
                while endpoint <= count:
                    if kind == SUBTREE:
                        ordinary[endpoint] += delta
                    else:
                        coords = coordinates[endpoint]
                        index = bisect_right(coords, limit)
                        tree = trees[endpoint]
                        while index:
                            tree[index] += delta
                            index &= index - 1
                    endpoint += endpoint & -endpoint

    if answers:
        sys.stdout.write("\n".join(answers) + "\n")


if __name__ == "__main__":
    main()
