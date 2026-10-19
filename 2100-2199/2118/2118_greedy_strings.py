import collections
import sys

ALPHABET = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BYTE_VALUES = 256
ZERO = ord("0")


def solve(data):
    tokens = data.split()
    size = int(tokens[0])
    message = tokens[1]
    codes = tokens[2:]
    single = [code for code in codes if len(code) == 1]
    weights = bytearray(BYTE_VALUES)
    if not single:
        for letter, code in zip(ALPHABET, codes):
            weights[letter] = len(code)
        return sum(message.translate(weights))
    if len(single) == 2:
        return -1

    bad = 1 - (single[0][0] - ZERO)
    index = bytearray(BYTE_VALUES)
    counts = []
    words = []
    for number, code in enumerate(codes):
        index[ALPHABET[number]] = number
        count = code.count(bytes([ZERO + bad]))
        counts.append(count)
        weights[ALPHABET[number]] = count
        words.append([bit - ZERO for bit in reversed(code)])
    total = sum(message.translate(weights))
    if total == 0:
        return -1

    next_state = [[0, 0]]
    terminal = [False]
    failure = [0]
    for word in words:
        state = 0
        for bit in word:
            child = next_state[state][bit]
            if child == 0:
                child = len(next_state)
                next_state[state][bit] = child
                next_state.append([0, 0])
                terminal.append(False)
                failure.append(0)
            state = child
        terminal[state] = True

    queue = collections.deque(child for child in next_state[0] if child)
    while queue:
        state = queue.popleft()
        fallback = failure[state]
        terminal[state] |= terminal[fallback]
        for bit in range(2):
            child = next_state[state][bit]
            if child:
                failure[child] = next_state[fallback][bit]
                queue.append(child)
            else:
                next_state[state][bit] = next_state[fallback][bit]

    # Cache a whole reversed codeword, avoiding expansion of the ciphertext.
    cache = [[0] * size for _ in next_state]
    state = 0
    tail = 0
    for letter in reversed(message.translate(index)):
        edge = cache[state][letter]
        if edge == 0:
            current = state
            consumed = 0
            for bit in words[letter]:
                consumed += bit == bad
                current = next_state[current][bit]
                if not terminal[current]:
                    edge = -consumed
                    break
            else:
                edge = current + 1
            cache[state][letter] = edge
        if edge < 0:
            # Every earlier bad bit can end a separate undecodable part.
            return total - tail + edge + 1
        state = edge - 1
        tail += counts[letter]
    return -1


def main():
    print(solve(sys.stdin.buffer.read()))


if __name__ == "__main__":
    main()
