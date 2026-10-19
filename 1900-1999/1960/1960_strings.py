import sys


ALPHABET_SIZE = 26
FIRST_LETTER = ord("a")
EMPTY_ROOT = 1
ROOT_COUNT = 2


def distinct_counts(text):
    lengths = [-1, 0]
    links = [0, 0]
    transitions = {}
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
        key = parent * ALPHABET_SIZE + code
        node = transitions.get(key)
        if node is None:
            node = len(lengths)
            lengths.append(lengths[parent] + 2)
            transitions[key] = node
            if lengths[node] == 1:
                links.append(EMPTY_ROOT)
            else:
                candidate = links[parent]
                while True:
                    left = position - lengths[candidate] - 1
                    if left >= 0 and text[left] == letter:
                        break
                    candidate = links[candidate]
                links.append(transitions[candidate * ALPHABET_SIZE + code])
        last = node
        answer.append(len(lengths) - ROOT_COUNT)
    return answer


def main():
    text = sys.stdin.buffer.readline().strip()
    print(*distinct_counts(text))


if __name__ == "__main__":
    main()
