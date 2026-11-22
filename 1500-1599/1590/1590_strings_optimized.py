import sys
from array import array

ALPHABET = 26
FIRST = ord("a")


def main():
    first = sys.stdin.buffer.read().split()[0]
    states = 2 * len(first) + 1
    length = array("H", [0]) * states
    link = array("h", [-1]) * states
    # At most 10000 states fit 16-bit transitions; zero denotes no transition.
    following = array("H", [0]) * (states * ALPHABET)
    size, last = 1, 0
    for letter in first:
        c = letter - FIRST
        current = size
        size += 1
        length[current] = length[last] + 1
        p = last
        while p >= 0 and following[p * ALPHABET + c] == 0:
            following[p * ALPHABET + c] = current
            p = link[p]
        if p < 0:
            link[current] = 0
        else:
            q = following[p * ALPHABET + c]
            if length[p] + 1 == length[q]:
                link[current] = q
            else:
                clone = size
                size += 1
                length[clone] = length[p] + 1
                link[clone] = link[q]
                offset = clone * ALPHABET
                old = q * ALPHABET
                following[offset : offset + ALPHABET] = following[old : old + ALPHABET]
                while p >= 0 and following[p * ALPHABET + c] == q:
                    following[p * ALPHABET + c] = clone
                    p = link[p]
                link[current] = link[q] = clone
        last = current
    print(sum(length[v] - length[link[v]] for v in range(1, size)))


main()
