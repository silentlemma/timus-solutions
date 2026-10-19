"""Distinct palindromes in every prefix, represented by a binary palindromic tree."""

from array import array
import sys

LETTER_A = ord("a")
ONE = ord("1")


def solve(word):
    capacity = len(word) + 2
    lengths = array("i", [0]) * capacity
    links = array("i", [0]) * capacity
    edge_a = array("i", [0]) * capacity
    edge_b = array("i", [0]) * capacity
    lengths[0] = -1
    last, used = 1, 2
    output = bytearray(b"0") * len(word)
    for pos, char in enumerate(word):
        edges = edge_a if char == LETTER_A else edge_b
        parent = last
        while True:
            before = pos - 1 - lengths[parent]
            if before >= 0 and word[before] == char:
                break
            parent = links[parent]
        current = edges[parent]
        if not current:
            current = used
            used += 1
            lengths[current] = lengths[parent] + 2
            edges[parent] = current
            if lengths[current] == 1:
                links[current] = 1
            else:
                candidate = links[parent]
                while True:
                    before = pos - 1 - lengths[candidate]
                    if before >= 0 and word[before] == char:
                        break
                    candidate = links[candidate]
                links[current] = edges[candidate]
            output[pos] = ONE
        last = current
    return output


def main():
    word = sys.stdin.buffer.read().strip()
    sys.stdout.buffer.write(solve(word))
    sys.stdout.buffer.write(b"\n")


if __name__ == "__main__":
    main()
