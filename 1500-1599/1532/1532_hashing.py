import sys

GAP_BITS = 4  # a place in the rest, at most 14
CUT_BITS = 2  # 0, 1 or 2 letters deleted
ID_BITS = 13  # word numbers below 8192
LOW_BITS = ID_BITS + CUT_BITS + 2 * GAP_BITS
GAP_MASK = (1 << GAP_BITS) - 1
CUT_MASK = (1 << CUT_BITS) - 1


def main():
    data = sys.stdin.read().split()
    k = int(data[0])
    words = data[1 : k + 1]
    # two words are at most two edits apart when deleting at most two letters
    # from each leaves the same rest and, gap by gap of the rest, the larger
    # number of deleted letters adds up to at most two
    keys = []
    for wid, w in enumerate(words):
        n = len(w)
        tag = wid << (CUT_BITS + 2 * GAP_BITS)
        keys.append((int.from_bytes(w.encode(), "big") << LOW_BITS) | tag)
        one = tag | (1 << (2 * GAP_BITS))
        two = tag | (2 << (2 * GAP_BITS))
        for i in range(n):
            rest = w[:i] + w[i + 1 :]
            keys.append((int.from_bytes(rest.encode(), "big") << LOW_BITS) | one | i)
            for j in range(i, n - 1):
                # the second letter, w[j + 1], sits in gap j of the rest
                rest2 = rest[:j] + rest[j + 1 :]
                keys.append(
                    (int.from_bytes(rest2.encode(), "big") << LOW_BITS) | two | (i << GAP_BITS) | j
                )
    keys.sort()
    found = [False] * k
    start = 0
    while start < len(keys):
        head = keys[start] >> LOW_BITS
        end = start + 1
        while end < len(keys) and keys[end] >> LOW_BITS == head:
            end += 1
        if end - start > 1:
            mark_group(keys[start:end], found)
        start = end
    chosen = sorted(w for w, f in zip(words, found) if f)
    print(len(chosen))
    if chosen:
        print("\n".join(chosen))


def mark_group(group, found):
    """Marks the words of one rest that have a close word in it."""
    whole = []
    ones = {}  # gap -> words that lost one letter there
    twos = {}  # pair of gaps -> words that lost two letters there
    for x in group:
        wid = (x & ((1 << LOW_BITS) - 1)) >> (CUT_BITS + 2 * GAP_BITS)
        cut = (x >> (2 * GAP_BITS)) & CUT_MASK
        if cut == 0:
            whole.append(wid)
        elif cut == 1:
            ones.setdefault(x & GAP_MASK, set()).add(wid)
        else:
            twos.setdefault((x >> GAP_BITS) & GAP_MASK, {}).setdefault(x & GAP_MASK, set()).add(wid)
    if whole:
        # the rest is a word itself, at most two deletions from every other
        for x in group:
            found[(x & ((1 << LOW_BITS) - 1)) >> (CUT_BITS + 2 * GAP_BITS)] = True
        return
    single = set().union(*ones.values()) if ones else set()
    if len(single) > 1:
        # one deletion from each costs at most two edits
        for wid in single:
            found[wid] = True
    for g1, by_g2 in twos.items():
        for g2, wids in by_g2.items():
            # the same two gaps: two substitutions
            if len(wids) > 1:
                for wid in wids:
                    found[wid] = True
            # one more letter in a gap shared with a single deletion
            near = ones.get(g1, set()) | ones.get(g2, set())
            if near:
                for wid in wids | near:
                    found[wid] = True


main()
