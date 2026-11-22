import sys


BLOCK_SIZE = 16384
WHITESPACE = 32


def tokens(source):
    pending = b""
    while True:
        block = source.read(BLOCK_SIZE)
        if not block:
            break
        fields = (pending + block).split()
        pending = fields.pop() if block[-1] > WHITESPACE else b""
        yield from fields
    if pending:
        yield pending


SYMBOLS = 90
LOWEST_SYMBOL = 33
ALPHABET = SYMBOLS**3


def encode(token):
    return (
        ((token[0] - LOWEST_SYMBOL) * SYMBOLS + token[1] - LOWEST_SYMBOL) * SYMBOLS
        + token[2]
        - LOWEST_SYMBOL
    )


def main():
    source = sys.stdin.buffer
    pattern = source.readline().split()
    size = len(pattern)
    # A list avoids boxing/unboxing a signed-short cell at every window update.
    deficit = [0] * ALPHABET
    for token in pattern:
        deficit[encode(token)] += 1
    del pattern
    ring = [0] * size
    missing, position, filled, answer = size, 0, 0, 0
    for token in tokens(source):
        letter = encode(token)
        if filled == size:
            old = ring[position]
            if deficit[old] >= 0:
                missing += 1
            deficit[old] += 1
        else:
            filled += 1
        if deficit[letter] > 0:
            missing -= 1
        deficit[letter] -= 1
        ring[position] = letter
        position += 1
        if position == size:
            position = 0
        if missing == 0:
            answer += 1
    print(answer)


main()
