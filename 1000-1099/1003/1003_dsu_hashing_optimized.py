from array import array
from sys import stdin

END_OF_INPUT = -1


def find(links, node):
    parity = 0
    edge = links[node]
    while edge >> 1 != node:
        parent = edge >> 1
        ancestor = links[parent]
        parity ^= edge & 1
        links[node] = (ancestor & ~1) | ((edge ^ ancestor) & 1)
        node, edge = parent, ancestor
    return node, parity


def solve(tokens, count):
    ids = {}
    links = array("H")
    ranks = bytearray()
    answer = count

    def node(position):
        item = ids.get(position)
        if item is None:
            item = len(links)
            ids[position] = item
            links.append(item << 1)
            ranks.append(0)
        return item

    for i in range(count):
        left, right, word = next(tokens), next(tokens), next(tokens)
        if answer != count:
            continue
        root_a, parity_a = find(links, node(int(left) - 1))
        root_b, parity_b = find(links, node(int(right)))
        required = parity_a ^ parity_b ^ (word == b"odd")
        if root_a == root_b:
            if required:
                answer = i
            continue
        if ranks[root_a] < ranks[root_b]:
            root_a, root_b = root_b, root_a
        links[root_b] = (root_a << 1) | required
        if ranks[root_a] == ranks[root_b]:
            ranks[root_a] += 1
    return answer


def main():
    tokens = (token for line in stdin.buffer for token in line.split())
    for size in tokens:
        if int(size) == END_OF_INPUT:
            break
        print(solve(tokens, int(next(tokens))))


main()
