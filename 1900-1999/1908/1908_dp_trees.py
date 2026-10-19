from array import array
import sys


def minimum_clicks(words):
    first_child = array("i", [0])
    next_sibling = array("i", [0])
    labels = bytearray([0])
    for word in words:
        node = 0
        for letter in word:
            child = first_child[node]
            while child and labels[child] != letter:
                child = next_sibling[child]
            if not child:
                child = len(first_child)
                first_child.append(0)
                next_sibling.append(first_child[node])
                labels.append(letter)
                first_child[node] = child
            node = child
    size = len(first_child)
    leaves = array("i", [0]) * size
    normal = array("i", [0]) * size
    supplied_skip = array("i", [0]) * size
    for node in range(size - 1, -1, -1):
        child = first_child[node]
        if not child:
            leaves[node] = 1
            continue
        total = 0
        best_normal = 0
        best_supplied = 0
        while child:
            count = leaves[child]
            leaves[node] += count
            total += normal[child] + count
            saving = normal[child] - supplied_skip[child]
            best_normal = max(best_normal, saving)
            best_supplied = max(best_supplied, count + saving)
            child = next_sibling[child]
        normal[node] = total - best_normal
        supplied_skip[node] = total - best_supplied
    return normal[0]


def main():
    tokens = sys.stdin.buffer.read().split()
    count = int(tokens[0])
    print(minimum_clicks(tokens[1 : count + 1]))


if __name__ == "__main__":
    main()
