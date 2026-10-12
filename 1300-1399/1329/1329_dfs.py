import sys

IDS = 40001


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    children = [[] for _ in range(IDS)]
    root = -1
    for i in range(n):
        node, parent = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if parent < 0:
            root = node
        else:
            children[parent].append(node)
    # enter[v] and leave[v] bound the times of the whole subtree of v
    enter, leave = [-1] * IDS, [-1] * IDS
    clock, stack = 0, [root]
    while stack:
        node = stack.pop()
        if node >= 0:
            enter[node] = clock
            clock += 1
            stack.append(~node)
            stack.extend(children[node])
        else:
            leave[~node] = clock
    pos = 1 + 2 * n
    out = []
    for i in range(int(data[pos])):
        a, b = int(data[pos + 1 + 2 * i]), int(data[pos + 2 + 2 * i])
        if enter[a] >= 0 and enter[a] <= enter[b] < leave[a]:
            out.append("1")
        elif enter[b] >= 0 and enter[b] <= enter[a] < leave[b]:
            out.append("2")
        else:
            out.append("0")
    print("\n".join(out))


main()
