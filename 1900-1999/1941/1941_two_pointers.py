from array import array
import sys

LOWEST_SYMBOL = 33
SYMBOL_COUNT = 90
ALPHABET_SIZE = SYMBOL_COUNT * SYMBOL_COUNT * SYMBOL_COUNT


def encode(token):
    return (
        ((token[0] - LOWEST_SYMBOL) * SYMBOL_COUNT + token[1] - LOWEST_SYMBOL)
        * (SYMBOL_COUNT)
        + token[2]
        - LOWEST_SYMBOL
    )


def count_windows(pattern, text):
    size = len(pattern)
    deficit = array("i", [0]) * ALPHABET_SIZE
    for token in pattern:
        deficit[encode(token)] += 1
    ring = array("i", [0]) * size
    missing = size
    position = 0
    used = 0
    answer = 0
    for token in text:
        if used == size:
            old = ring[position]
            if deficit[old] >= 0:
                missing += 1
            deficit[old] += 1
        else:
            used += 1
        code = encode(token)
        if deficit[code] > 0:
            missing -= 1
        deficit[code] -= 1
        ring[position] = code
        position += 1
        if position == size:
            position = 0
        if missing == 0:
            answer += 1
    return answer


if __name__ == "__main__":
    pattern = sys.stdin.buffer.readline().split()
    text = sys.stdin.buffer.read().split()
    print(count_windows(pattern, text))
