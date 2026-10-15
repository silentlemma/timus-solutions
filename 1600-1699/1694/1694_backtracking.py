import sys


def repetition_at_end(word, k):
    """Whether some k-repetition ends at the last letter of word."""
    size = len(word)
    for block in range(1, size // k + 1):
        start = size - k * block
        i = start
        while i < size - block and word[i] == word[i + block]:
            i += 1
        if i == size - block:
            return True
    return False


def proper_repetition(word, k):
    """Whether w^k has a k-repetition other than itself. w has none, and
    w^k repeats with period |w|, so only windows that start in the first
    copy and leave it need a look."""
    size = len(word)
    total = size * k
    text = word * k
    for block in range(1, size + 1):
        span = k * block
        for start in range(min(size, total - span + 1)):
            if start + span <= size or span == total:
                continue
            i, end = start, start + span - block
            while i < end and text[i] == text[i + block]:
                i += 1
            if i == end:
                return True
    return False


def main():
    m, k, n = (int(w) for w in sys.stdin.read().split())
    # a killer word is w repeated k times; whether it works does not depend
    # on which letters w uses, so count the words w with letters numbered in
    # order of first appearance, by their number of different letters
    longest = n // k
    counts = [[0] * (longest + 1) for _ in range(longest + 1)]
    word = []

    def extend(distinct):
        # w^k may fail while a longer w still works, so this only skips counting
        if word and not proper_repetition(word, k):
            counts[len(word)][distinct] += 1
        if len(word) == longest:
            return
        for c in range(distinct + 1):
            word.append(c)
            # a k-repetition inside w is one inside the killer word too
            if not repetition_at_end(word, k):
                extend(max(distinct, c + 1))
            word.pop()

    extend(0)
    total = 0
    for length in range(1, longest + 1):
        ways = 1
        for distinct in range(1, length + 1):
            ways *= max(m - distinct + 1, 0)
            total += counts[length][distinct] * ways
    print(total)


main()
