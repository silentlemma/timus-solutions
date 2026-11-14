from array import array
import sys


LETTER_BITS = 5
OFFSET_BITS = 7
OFFSET_MASK = (1 << OFFSET_BITS) - 1
POSITION_BITS = 17
POSITION_MASK = (1 << POSITION_BITS) - 1


def shortest_keys(words):
    width = max(map(len, words))
    top = LETTER_BITS * (width - 1)
    first_letter = ord("a") - 1
    suffixes = []
    for owner, word in enumerate(words):
        position = owner << OFFSET_BITS
        suffix = 0
        for offset in range(len(word) - 1, -1, -1):
            suffix = ((word[offset] - first_letter) << top) | (suffix >> LETTER_BITS)
            suffixes.append((suffix << POSITION_BITS) | position | offset)
    suffixes.sort()

    size = len(suffixes)
    positions = array("I", [0]) * size
    adjacent = bytearray(size)
    shared = bytearray(size)
    past = suffixes[0]
    positions[0] = past & POSITION_MASK
    left = 0
    for i in range(1, size):
        current = suffixes[i]
        position = current & POSITION_MASK
        positions[i] = position
        owner, past_owner = position >> OFFSET_BITS, (past & POSITION_MASK) >> OFFSET_BITS
        distinct_bits = ((current ^ past) >> POSITION_BITS).bit_length()
        if distinct_bits:
            common = width - (distinct_bits + LETTER_BITS - 1) // LETTER_BITS
        else:
            common = len(words[owner]) - (position & OFFSET_MASK)
        left = common if owner != past_owner else min(left, common)
        shared[i] = left
        adjacent[i] = common
        past = current
    del suffixes

    best = words.copy()
    right = 0
    following_owner = positions[-1] >> OFFSET_BITS
    for i in range(size - 1, -1, -1):
        position = positions[i]
        owner, start = position >> OFFSET_BITS, position & OFFSET_MASK
        if i + 1 < size:
            common = adjacent[i + 1]
            right = common if owner != following_owner else min(right, common)
        length = 1 + max(shared[i], right)
        if length < len(best[owner]) and start + length <= len(words[owner]):
            best[owner] = words[owner][start : start + length]
        following_owner = owner
    return best


def main():
    _, *words = sys.stdin.buffer.read().split()
    sys.stdout.buffer.write(b"\n".join(shortest_keys(words)) + b"\n")


if __name__ == "__main__":
    main()
