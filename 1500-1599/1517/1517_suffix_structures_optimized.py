import sys
from array import array

ALPHABET = 26
FIRST = ord("A")


def main():
    data = sys.stdin.buffer.read().split()
    first, second = data[1], data[2]
    states = 2 * len(first) + 1
    length = array("i", [0]) * states
    link = array("i", [-1]) * states
    # Dense 32-bit transitions fit without Python integer objects or linked scans.
    following = array("i", [-1]) * (states * ALPHABET)
    size, last = 1, 0
    for letter in first:
        c = letter - FIRST
        current = size
        size += 1
        length[current] = length[last] + 1
        p = last
        while p >= 0 and following[p * ALPHABET + c] < 0:
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
    state = run = best = end = 0
    for index, letter in enumerate(second):
        c = letter - FIRST
        target = following[state * ALPHABET + c]
        while state and target < 0:
            state = link[state]
            run = length[state]
            target = following[state * ALPHABET + c]
        if target >= 0:
            state = target
            run += 1
        else:
            run = 0
        if run > best:
            best, end = run, index + 1
    sys.stdout.buffer.write(second[end - best : end] + b"\n")


main()
