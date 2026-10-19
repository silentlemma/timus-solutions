import sys
from array import array

# character classes, ordered: the end, other characters, dot, at, letters
OTHER = 1
DOT = 2
AT = 3
LETTER = 4
LETTERS = 26
ALPHABET = LETTER + LETTERS
BYTES = 256


def suffix_array(code):
    # cyclic prefix doubling with counting sort; code ends with a 0
    n = len(code)
    count = array("i", [0]) * max(n, ALPHABET)
    for c in code:
        count[c] += 1
    for i in range(1, ALPHABET):
        count[i] += count[i - 1]
    order = array("i", [0]) * n
    for i in range(n - 1, -1, -1):
        count[code[i]] -= 1
        order[count[code[i]]] = i
    cls = array("i", [0]) * n
    classes = 1
    for i in range(1, n):
        if code[order[i]] != code[order[i - 1]]:
            classes += 1
        cls[order[i]] = classes - 1
    shifted = array("i", [0]) * n
    fresh = array("i", [0]) * n
    shift = 1
    while shift < n and classes < n:
        for i in range(n):
            p = order[i] - shift
            shifted[i] = p + n if p < 0 else p
        for i in range(classes):
            count[i] = 0
        for i in range(n):
            count[cls[shifted[i]]] += 1
        for i in range(1, classes):
            count[i] += count[i - 1]
        for i in range(n - 1, -1, -1):
            p = shifted[i]
            c = cls[p]
            count[c] -= 1
            order[count[c]] = p
        fresh[order[0]] = 0
        classes = 1
        prev = order[0]
        prev_next = prev + shift
        if prev_next >= n:
            prev_next -= n
        for i in range(1, n):
            cur = order[i]
            cur_next = cur + shift
            if cur_next >= n:
                cur_next -= n
            if cls[cur] != cls[prev] or cls[cur_next] != cls[prev_next]:
                classes += 1
            fresh[cur] = classes - 1
            prev, prev_next = cur, cur_next
        cls, fresh = fresh, cls
        shift *= 2
    return order, cls


def main():
    text = sys.stdin.buffer.read()
    n = len(text)
    table = bytearray([OTHER]) * BYTES
    for ch in range(LETTERS):
        table[ord("a") + ch] = LETTER + ch
    table[ord(".")] = DOT
    table[ord("@")] = AT
    code = bytearray(text.translate(table)) + b"\0"
    letters = array("i", [0]) * (n + 1)
    for i in range(n):
        letters[i + 1] = letters[i] + (code[i] >= LETTER)
    # around an at sign, users start no earlier than just past the last other
    # character, at or double dot, and domains end no later than just before
    # the next of them
    first_start = {}
    last_end = {}
    barrier = double = -1
    for i in range(n):
        c = code[i]
        if c == AT:
            first_start[i] = max(barrier, double) + 1
        elif c == DOT and i and code[i - 1] == DOT:
            double = i
        if c == OTHER or c == AT:
            barrier = i
    barrier = double = n
    next_at = array("i", [-1]) * n
    upcoming = -1
    for i in range(n - 1, -1, -1):
        c = code[i]
        if c == OTHER:
            upcoming = -1
        next_at[i] = upcoming
        if c == AT:
            last_end[i] = min(barrier, double) - 1
            upcoming = i
        elif c == DOT and code[i + 1] == DOT:
            double = i + 1
        if c == OTHER or c == AT:
            barrier = i
    order, rank = suffix_array(code)
    # being an address is a property of the string alone, so every address
    # is counted once, at the first suffix in sorted order that starts with
    # it: only prefixes longer than the common part with the suffix before
    total = 0
    common = 0
    for start in range(n):
        r = rank[start]
        other = order[r - 1]
        while code[start + common] == code[other + common] and code[start + common]:
            common += 1
        lcp = common
        if common:
            common -= 1
        if code[start] < LETTER:
            continue
        at = next_at[start]
        if at < 0 or start < first_start[at] or code[at - 1] < LETTER:
            continue
        end = last_end[at]
        if at + 1 > end or code[at + 1] < LETTER:
            continue
        lo = max(start + lcp, at + 1)
        if lo <= end:
            total += letters[end + 1] - letters[lo]
    print(total)


main()
