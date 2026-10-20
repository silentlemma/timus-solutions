import sys


# A score is at least one half; eighteen mismatches cannot improve it.
SCORE_BITS = 18
SCORE_SCALE = 1 << SCORE_BITS
BYTE_BITS = 8
BYTE_VALUES = 1 << BYTE_BITS
HALF_BASE = 10 // 2
FIVE_POWER = HALF_BASE**SCORE_BITS
MISMATCH_TABLE = bytes([0] + [1] * (BYTE_VALUES - 1))
MISMATCH = b"\x01"


def format_score(score):
    whole, fraction = divmod(score, SCORE_SCALE)
    if not fraction:
        return str(whole)
    tail = f"{fraction * FIVE_POWER:0{SCORE_BITS}d}".rstrip("0")
    return str(whole) + "." + tail


def main():
    tokens = sys.stdin.buffer.read().split()
    word_count = int(tokens[0])
    query_count = int(tokens[1])
    numbers = []
    lengths = []
    for word in tokens[2 : word_count + 2]:
        numbers.append(int.from_bytes(word, "big"))
        lengths.append(len(word))

    groups = {}
    answers = [0] * query_count
    offset = word_count + 2
    for index in range(query_count):
        first = int(tokens[offset]) - 1
        second = int(tokens[offset + 1]) - 1
        cut = int(tokens[offset + 2])
        offset += 1 + 2
        if first == second:
            answers[index] = (lengths[first] - cut) * SCORE_SCALE
        else:
            if first > second:
                first, second = second, first
            groups.setdefault((first, second), []).append((cut, index))
    del tokens

    for (first, second), queries in groups.items():
        if lengths[first] > lengths[second]:
            first, second = second, first
        length = lengths[first]
        longer = numbers[second]
        if lengths[second] != length:
            longer &= (1 << (BYTE_BITS * length)) - 1
        difference = numbers[first] ^ longer
        if not difference:
            for cut, index in queries:
                answers[index] = (length - cut) * SCORE_SCALE
            continue

        # Least significant bytes compare letters starting at the word ends.
        different = difference.to_bytes(length, "little").translate(MISMATCH_TABLE)
        find = different.find
        for cut, index in queries:
            position = cut
            mismatches = 0
            best = 0
            upper = (length - cut) * SCORE_SCALE
            while upper >> mismatches > best:
                next_position = find(MISMATCH, position)
                if next_position < 0:
                    next_position = length
                candidate = (next_position - cut) << (SCORE_BITS - mismatches)
                if candidate > best:
                    best = candidate
                if next_position == length:
                    break
                position = next_position + 1
                mismatches += 1
            answers[index] = best

    sys.stdout.write("\n".join(map(format_score, answers)) + "\n")


if __name__ == "__main__":
    main()
