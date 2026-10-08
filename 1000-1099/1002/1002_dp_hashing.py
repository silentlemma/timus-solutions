import sys

MAX_WORD_LENGTH = 50
KEYPAD = str.maketrans("abcdefghijklmnopqrstuvwxyz", "22233344115566070778889990")
END_OF_INPUT = "-1"


def solve(phone, words):
    by_digits = {}
    for i, word in enumerate(words):
        by_digits.setdefault(word.translate(KEYPAD), i)
    # best[i]: fewest words for the first i digits; how[i]: last word used
    m = len(phone)
    best = [-1] * (m + 1)
    how = [-1] * (m + 1)
    best[0] = 0
    for i in range(m):
        if best[i] < 0:
            continue
        for end in range(i + 1, min(m, i + MAX_WORD_LENGTH) + 1):
            w = by_digits.get(phone[i:end])
            if w is not None and (best[end] < 0 or best[i] + 1 < best[end]):
                best[end] = best[i] + 1
                how[end] = w
    if best[m] < 0:
        return "No solution."
    used = []
    pos = m
    while pos > 0:
        used.append(words[how[pos]])
        pos -= len(words[how[pos]])
    return " ".join(reversed(used))


def main():
    tokens = sys.stdin.read().split()
    out = []
    pos = 0
    while tokens[pos] != END_OF_INPUT:
        phone, n = tokens[pos], int(tokens[pos + 1])
        words = tokens[pos + 2 : pos + 2 + n]
        pos += 2 + n
        out.append(solve(phone, words))
    sys.stdout.write("\n".join(out) + "\n")


main()
