from array import array
import sys

SYMBOL_COUNT = 90
ALPHABET_SIZE = SYMBOL_COUNT**3
LOWEST_SYMBOL = 33
WHITESPACE_MAX = 32
TRIPLET_SIZE = 3


def main():
    pattern = sys.stdin.buffer.readline().split()
    size = len(pattern)
    deficit = array("h", [0]) * ALPHABET_SIZE
    for token in pattern:
        letter = (
            (token[0] - LOWEST_SYMBOL) * SYMBOL_COUNT + token[1] - LOWEST_SYMBOL
        ) * SYMBOL_COUNT
        letter += token[2] - LOWEST_SYMBOL
        deficit[letter] += 1
    del pattern
    ring = array("I", [0]) * size
    missing, position, filled, answer = size, 0, 0, 0
    text = sys.stdin.buffer.read()
    cursor = 0
    while cursor < len(text):
        if text[cursor] <= WHITESPACE_MAX:
            cursor += 1
            continue
        letter = (text[cursor] - LOWEST_SYMBOL) * SYMBOL_COUNT + text[cursor + 1] - LOWEST_SYMBOL
        letter = letter * SYMBOL_COUNT + text[cursor + 2] - LOWEST_SYMBOL
        cursor += TRIPLET_SIZE
        if filled == size:
            old = ring[position]
            if deficit[old] >= 0:
                missing += 1
            deficit[old] += 1
        else:
            filled += 1
        if deficit[letter] > 0:
            missing -= 1
        # Both frequencies are at most size <= 8000, so signed shorts cannot overflow.
        deficit[letter] -= 1
        ring[position] = letter
        position += 1
        if position == size:
            position = 0
        if missing == 0:
            answer += 1
    print(answer)


main()
