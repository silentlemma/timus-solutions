import os
import sys


ALPHABET_SIZE = 26
FIRST_LETTER = ord("a")
EMPTY_ROOT = 1
ROOT_COUNT = 2


def distinct_counts(text):
    lengths = [-1, 0]
    links = [0, 0]
    transitions = [{} for _ in range(ALPHABET_SIZE)]
    node_count = 0
    last = EMPTY_ROOT
    answer = []
    for position, letter in enumerate(text):
        code = letter - FIRST_LETTER
        parent = last
        while True:
            left = position - lengths[parent] - 1
            if left >= 0 and text[left] == letter:
                break
            parent = links[parent]
        edges = transitions[code]
        node = edges.get(parent)
        if node is None:
            node = len(lengths)
            lengths.append(lengths[parent] + 2)
            edges[parent] = node
            node_count += 1
            if lengths[node] == 1:
                links.append(EMPTY_ROOT)
            else:
                candidate = links[parent]
                while True:
                    left = position - lengths[candidate] - 1
                    if left >= 0 and text[left] == letter:
                        break
                    candidate = links[candidate]
                links.append(edges[candidate])
        last = node
        answer.append(node_count)
    return answer


def main():
    text = sys.stdin.buffer.readline().strip()
    sys.stdout.write(" ".join(map(str, distinct_counts(text))) + "\n")


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    # Preserve the complete output before avoiding interpreter teardown.
    sys.stdout.flush()
    sys.stderr.flush()
    os._exit(0)
