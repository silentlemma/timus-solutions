import sys
from array import array
from bisect import bisect_left

LONGEST = 15  # no minimal forbidden multiset is longer for bases up to 36
SHIFT = 6  # bits per digit in a word code
DIGIT_MASK = (1 << SHIFT) - 1
LOW_DIGITS = 10  # a word keeps its last digits apart, to stay in machine words
LOW_BITS = LOW_DIGITS * SHIFT
LOW_MASK = (1 << LOW_BITS) - 1
LENGTH_AT = 32  # the length sits above the first digits of the word
HIGH_MASK = (1 << LENGTH_AT) - 1
STAR = LONGEST  # a pattern count meaning "any number of this digit"
FIELD = 4  # bits per count in a pattern node
COUNT_MASK = (1 << FIELD) - 1
SLOT = FIELD + 1  # a count with a guard bit above it, in a packed vector
SLOT_MASK = (1 << SLOT) - 1
PER_WORD = 12  # slots per machine word
WORDS = 3
GUARD = sum(1 << (SLOT * i + FIELD) for i in range(PER_WORD))
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def least_words(base):
    # the least number of every pair (sum of digits, sum of squares) with at
    # most LONGEST digits, as (high, low) with the length on top of high:
    # digits come in increasing order, and adding digits keeps words' order
    width = LONGEST * (base - 1) ** 2 + 1
    where = {0: 0}
    find = where.get
    keys, highs, lows = [0], [0], [0]
    for d in range(1, base):
        step = d * width + d * d
        for i in range(len(keys)):
            key, length = keys[i], highs[i] >> LENGTH_AT
            high, low = highs[i] & HIGH_MASK, lows[i]
            for grown in range(length + 1, LONGEST + 1):
                key += step
                high = (high << SHIFT) | (low >> (LOW_BITS - SHIFT))
                low = ((low << SHIFT) & LOW_MASK) | d
                top = (grown << LENGTH_AT) | high
                at = find(key)
                if at is None:
                    where[key] = len(keys)
                    keys.append(key)
                    highs.append(top)
                    lows.append(low)
                elif top < highs[at] or (top == highs[at] and low < lows[at]):
                    highs[at] = top
                    lows[at] = low
    return where, keys, highs, lows, width


def is_least(least, key, length, digits):
    where, _, highs, lows, _ = least
    at = where[key]
    high, low = 0, 0
    for d in digits:
        high = (high << SHIFT) | (low >> (LOW_BITS - SHIFT))
        low = ((low << SHIFT) & LOW_MASK) | d
    return highs[at] == (length << LENGTH_AT) | high and lows[at] == low


def forbidden(base, least):
    # a minimal forbidden multiset is not the least of its pair, while every
    # multiset with one digit fewer is; without its largest digit it is one
    # of the least words, so each least word is grown by one digit at its end
    _, keys, highs, lows, width = least
    found = []
    for r in range(len(keys)):
        length = highs[r] >> LENGTH_AT
        if length == 0 or length >= LONGEST:
            continue
        high, low = highs[r] & HIGH_MASK, lows[r]
        digits = []
        for _ in range(length):
            digits.append(low & DIGIT_MASK)
            low = (low >> SHIFT) | ((high & DIGIT_MASK) << (LOW_BITS - SHIFT))
            high >>= SHIFT
        digits.reverse()
        for add in range(digits[-1], base):
            grown_key = keys[r] + add * width + add * add
            if is_least(least, grown_key, length + 1, digits + [add]):
                continue
            minimal = True
            for i, drop in enumerate(digits):
                if drop == add or (i > 0 and digits[i - 1] == drop):
                    continue
                rest = digits[:i] + digits[i + 1:] + [add]
                if not is_least(least, grown_key - drop * width - drop * drop, length, rest):
                    minimal = False
                    break
            if minimal:
                counts = [0] * (base - 1)
                for d in digits:
                    counts[d - 1] += 1
                counts[add - 1] += 1
                found.append(pack(counts))
    return found


def pack(counts):
    # a vector of counts as three words of PER_WORD slots and the set of its
    # nonzero counts
    words = [0] * WORDS
    mask = 0
    for i, c in enumerate(counts):
        if c:
            words[i // PER_WORD] |= c << (SLOT * (i % PER_WORD))
            mask |= 1 << i
    return words[0], words[1], words[2], mask


def count_at(v, i):
    return (v[i // PER_WORD] >> (SLOT * (i % PER_WORD))) & SLOT_MASK


def without(v, i):
    words = list(v[:WORDS])
    words[i // PER_WORD] &= ~(SLOT_MASK << (SLOT * (i % PER_WORD)))
    return words[0], words[1], words[2], v[WORDS] & ~(1 << i)


def below(g, f):
    # every count of g at most that of f: a slot's guard bit survives the
    # subtraction exactly then, and no borrow crosses into the next slot
    return (((f[0] | GUARD) - g[0]) & GUARD == GUARD
            and ((f[1] | GUARD) - g[1]) & GUARD == GUARD
            and ((f[2] | GUARD) - g[2]) & GUARD == GUARD)


class Index:
    """Vectors grouped by their sets of nonzero counts, to find quickly
    whether one of them lies below a given vector."""

    def __init__(self, items):
        self.items = items
        groups = {}
        for g in items:
            groups.setdefault(g[WORDS], []).append(g)
        self.supports = sorted(groups)
        self.groups = [groups[s] for s in self.supports]

    def covers(self, f):
        # by the subsets of the support of f or by a scan of the supports,
        # whichever is shorter
        supports = self.supports
        mask = f[WORDS]
        if (1 << bin(mask).count("1")) < len(supports):
            sub = mask
            while True:
                s = bisect_left(supports, sub)
                if s < len(supports) and supports[s] == sub and self.in_group(s, f):
                    return True
                if sub == 0:
                    return False
                sub = (sub - 1) & mask
        for s, sup in enumerate(supports):
            if not sup & ~mask and self.in_group(s, f):
                return True
        return False

    def in_group(self, s, f):
        for g in self.groups[s]:
            if below(g, f):
                return True
        return False


def minimal(vectors, digits):
    # one vector that lies below another has a smaller total, so the vectors
    # are taken by total, and those of one total are checked against the
    # smaller ones only
    by_total = {}
    for v in set(vectors):
        by_total.setdefault(sum(count_at(v, i) for i in range(digits)), []).append(v)
    kept = []
    smaller = Index([])
    for total in sorted(by_total):
        fresh = [v for v in by_total[total] if not smaller.covers(v)]
        if fresh:
            kept += fresh
            smaller = Index(kept)
    return kept


class Patterns:
    """Patterns over the first n digits, stored as a trie of (parent, count)
    nodes; node 0 is the empty pattern, and the patterns of one solved set
    are a few runs of consecutive nodes."""

    def __init__(self, digits):
        self.nodes = array("i", [0])
        self.memo = {}
        self.stars = [0]
        for _ in range(digits):
            self.stars.append(self.extend(self.stars[-1], STAR))

    def extend(self, parent, count):
        self.nodes.append((parent << FIELD) | count)
        return len(self.nodes) - 1

    def decode(self, node, n):
        counts = [0] * n
        nodes = self.nodes
        for i in range(n - 1, -1, -1):
            x = nodes[node]
            counts[i] = x & COUNT_MASK
            node = x >> FIELD
        return counts

    def solve(self, gens, n):
        # the runs of patterns whose union is the set of count vectors over
        # the first n digits above none of gens, a set of minimal vectors; the
        # last digit takes each fixed count below the largest one, then any
        key = (n, hash(frozenset(gens)))
        if key in self.memo:
            return self.memo[key]
        runs = []
        if not gens:
            runs.append((self.stars[n], 1))
        elif gens[0][WORDS]:
            last = n - 1
            by_count = {}
            for g in gens:
                by_count.setdefault(count_at(g, last), []).append(without(g, last))
            top = max(by_count)
            # levels[k]: the minimal gens that apply with k copies of the last
            # digit; as gens are minimal, a newcomer with k copies never lies
            # above an earlier one, and the last level serves any count
            levels = []
            for k in range(top + 1):
                fresh = by_count.get(k, [])
                level = []
                if levels:
                    newcomers = Index(fresh)
                    level = [f for f in levels[-1] if not newcomers.covers(f)]
                levels.append(level + fresh)
            open_index = Index(levels[top])
            for k in range(top + 1):
                sub = self.solve(levels[k], last)
                start = len(self.nodes)
                for node in self.members(sub):
                    # a prefix allowed with any count is already covered below
                    if k == top or open_index.covers(pack(self.decode(node, last))):
                        self.extend(node, STAR if k == top else k)
                runs.append((start, len(self.nodes) - start))
        self.memo[key] = runs
        return runs

    @staticmethod
    def members(runs):
        for start, count in runs:
            yield from range(start, start + count)


def main():
    base = int(sys.stdin.read().split()[0])
    m = base - 1
    least = least_words(base)
    gens = minimal(forbidden(base, least), m)
    del least
    patterns = Patterns(m)
    lines = []
    for node in patterns.members(patterns.solve(gens, m)):
        parts = []
        for i, c in enumerate(patterns.decode(node, m)):
            ch = DIGITS[i + 1]
            parts.append(ch + "*" if c == STAR else ch * c)
        lines.append("".join(parts))
    lines.sort()
    print("\n".join(lines))


main()
