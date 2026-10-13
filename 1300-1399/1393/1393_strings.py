from array import array
import sys

ALPHABET = 256


def suffix_array(text, alphabet):
    n = len(text)
    if n == 1:
        return array("i", [0])
    # Suffix types and all indices use compact buffers, including recursive levels.
    types = bytearray(n)
    types[-1] = 1
    for i in range(n - 2, -1, -1):
        types[i] = text[i] < text[i + 1] or (
            text[i] == text[i + 1] and types[i + 1]
        )
    counts = array("i", [0]) * alphabet
    for c in text:
        counts[c] += 1
    starts = array("i", [0]) * alphabet
    ends = array("i", [0]) * alphabet
    total = 0
    for c in range(alphabet):
        starts[c] = total
        total += counts[c]
        ends[c] = total
    del counts
    sa = array("i", [-1]) * n

    def induce(lms):
        sa[:] = array("i", [-1]) * n
        buckets = ends[:]
        for p in reversed(lms):
            c = text[p]
            buckets[c] -= 1
            sa[buckets[c]] = p
        buckets = starts[:]
        for i in range(n):
            p = sa[i] - 1
            if p >= 0 and not types[p]:
                c = text[p]
                sa[buckets[c]] = p
                buckets[c] += 1
        buckets = ends[:]
        for i in range(n - 1, -1, -1):
            p = sa[i] - 1
            if p >= 0 and types[p]:
                c = text[p]
                buckets[c] -= 1
                sa[buckets[c]] = p

    # LMS positions cannot be adjacent, so their map needs only half as many entries.
    lms = array("i", (i for i in range(1, n) if types[i] and not types[i - 1]))
    m = len(lms)
    induce(lms)
    mapping = array("i", [0]) * (n // 2 + 1)
    for i, p in enumerate(lms):
        mapping[p // 2] = i
    reduced = array("i", [0]) * m
    prev = name = -1
    for p in sa:
        if p <= 0 or not types[p] or types[p - 1]:
            continue
        index = mapping[p // 2]
        different = prev < 0
        if not different:
            old = mapping[prev // 2]
            stop = lms[index + 1] if index + 1 < m else n
            old_stop = lms[old + 1] if old + 1 < m else n
            if stop - p != old_stop - prev:
                different = True
            else:
                a, b = p, prev
                while a < stop and text[a] == text[b]:
                    a += 1
                    b += 1
                different = a != stop or stop == n or text[stop] != text[old_stop]
        if different:
            name += 1
        reduced[index] = name
        prev = p
    del mapping
    # Sorting the smaller string resolves equal LMS substrings before the final induction.
    if name + 1 == m:
        sorted_lms = array("i", [0]) * m
        for i in range(m):
            sorted_lms[reduced[i]] = lms[i]
    else:
        reduced_sa = suffix_array(reduced, name + 1)
        sorted_lms = array("i", (lms[i] for i in reduced_sa))
        del reduced_sa
    del reduced, lms
    induce(sorted_lms)
    return sa


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    text = data[1]
    del data
    # The next occurrence in the doubled string starts at the shortest cyclic period.
    p = (text + text).find(text, 1)
    if p == 1:
        print("%.3f" % n)
        return
    text = text[:p] * 2 + b"\0"
    sa = suffix_array(text, ALPHABET)
    order = array("i", (i for i in sa if i < p))
    del sa
    rank = array("i", [0]) * p
    for r, i in enumerate(order):
        rank[i] = r
    # The primitive period has distinct rotations, so their LCPs end before the sentinel.
    total = h = 0
    for i in range(p):
        r = rank[i]
        if not r:
            h = 0
            continue
        j = order[r - 1]
        while text[i + h] == text[j + h]:
            h += 1
        total += h
        if h:
            h -= 1
    total += p * (n // p - 1) * n
    print("%.3f" % (total / (n - 1)))


if __name__ == "__main__":
    main()
