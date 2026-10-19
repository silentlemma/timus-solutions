import sys

ALPHABET = 26
FIRST = ord("a")


def solve(source, modifiers):
    data = source.encode("ascii")
    size = len(data)
    positions = [[] for _ in range(ALPHABET)]
    for at, ch in enumerate(data):
        positions[ch - FIRST].append(at)
    frequency = list(map(len, positions))
    for row in positions:
        row.append(size)
    counts = [0] * ALPHABET
    for ch in modifiers.encode("ascii"):
        counts[ch - FIRST] += 1
    head = [0] * ALPHABET
    cut = counts.copy()
    next_position = [row[0] for row in positions]
    next_cut = [positions[c][cut[c]] if cut[c] < frequency[c] else size for c in range(ALPHABET)]
    delta = [counts[c] - frequency[c] for c in range(ALPHABET)]
    bad = 0
    available = 0
    present = 0
    for c in range(ALPHABET):
        if delta[c] < 0 or delta[c] & 1:
            bad |= 1 << c
        if counts[c]:
            available |= 1 << c
        if frequency[c]:
            present |= 1 << c
    at = 0
    answer = bytearray()
    dirty = True
    original = ALPHABET
    while bad:
        if dirty:
            if at == size:
                original = ALPHABET
            elif counts[data[at] - FIRST] == 0:
                original = data[at] - FIRST
            else:
                limit = min(next_cut)
                candidates = present
                while candidates:
                    bit = candidates & -candidates
                    c = bit.bit_length() - 1
                    if next_position[c] <= limit:
                        original = c
                        break
                    candidates ^= bit
                else:
                    raise AssertionError("missing accessible original")
            dirty = False
        modifier = (available & -available).bit_length() - 1 if available else ALPHABET
        if original <= modifier:
            c = original
            assert c < ALPHABET
            to = next_position[c]
            while at < to:
                removed = data[at] - FIRST
                counts[removed] -= 1
                head[removed] += 1
                next_position[removed] = positions[removed][head[removed]]
                if counts[removed] == 0:
                    available &= ~(1 << removed)
                if head[removed] == frequency[removed]:
                    present &= ~(1 << removed)
                at += 1
            head[c] += 1
            next_position[c] = positions[c][head[c]]
            at += 1
            if head[c] == frequency[c]:
                present &= ~(1 << c)
            cut[c] += 1
            delta[c] += 1
            dirty = True
        else:
            c = modifier
            assert c < ALPHABET
            counts[c] -= 1
            if counts[c] == 0:
                available &= ~(1 << c)
            cut[c] -= 1
            delta[c] -= 1
        next_cut[c] = positions[c][cut[c]] if cut[c] < frequency[c] else size
        if delta[c] < 0 or delta[c] & 1:
            bad |= 1 << c
        else:
            bad &= ~(1 << c)
        answer.append(c + FIRST)
    return answer.decode("ascii")


if __name__ == "__main__":
    source, modifiers = sys.stdin.buffer.read().decode("ascii").split()
    print(solve(source, modifiers))
