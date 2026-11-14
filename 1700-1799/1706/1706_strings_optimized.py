import sys


ALPHABET_SIZE = 26
FIRST_LETTER = ord("a")
TEXT_COPIES = 3


def counts(text, width):
    size = len(text)
    if width == 1 or text.count(text[:1]) == size:
        return [width] * size

    sweep_end = size + width - 2
    repeated = (text * TEXT_COPIES)[: sweep_end + width]
    next_equal = [len(repeated)] * len(repeated)
    nearest = [len(repeated)] * ALPHABET_SIZE
    for position in range(len(repeated) - 1, -1, -1):
        letter = repeated[position] - FIRST_LETTER
        next_equal[position] = nearest[letter]
        nearest[letter] = position

    common = [0] * width
    updated = [-2] * width
    covered_until = list(range(len(repeated)))
    answer = [0] * size
    for start in range(sweep_end, -1, -1):
        end = start + width
        position = next_equal[start]
        while position < end:
            distance = position - start
            # A skipped diagonal broke its common prefix at the preceding step.
            length = common[distance] + 1 if updated[distance] == start + 1 else 1
            common[distance] = length
            updated[distance] = start
            duplicate_end = position + length
            if duplicate_end > covered_until[position]:
                covered_until[position] = duplicate_end
            position = next_equal[position]
        if start < size:
            total = 0
            for position in range(start, end):
                fresh = end - covered_until[position]
                if fresh > 0:
                    total += fresh
            answer[start] = total
    return answer


def main():
    width, text = sys.stdin.buffer.read().split()
    print(" ".join(map(str, counts(text, int(width)))))


if __name__ == "__main__":
    main()
