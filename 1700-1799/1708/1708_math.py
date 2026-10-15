import sys
from array import array
from bisect import bisect_left

# This bound covers the obstructions and the fixed parts for bases up to 36.
LONGEST = 15
MAX_FIXED = LONGEST - 1
SHIFT = 6
DIGIT_MASK = (1 << SHIFT) - 1
DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def solve(base):
    m = base - 1
    width = LONGEST * m * m + 1
    offsets = []
    total = 0
    # For each sum, convexity bounds the square sum. Equal parities let us
    # store only half of that interval, with no hash table or empty rectangle.
    for s in range(LONGEST * m + 1):
        a, r = divmod(s, LONGEST)
        lo = LONGEST * a * a + r * (2 * a + 1)
        a, r = divmod(s, m)
        hi = a * m * m + r * r
        offsets.append(total - lo // 2)
        total += (hi - lo) // 2 + 1
    where = array("i", [-1]) * total
    where[0] = 0
    # Each word is a parent index and its last digit; runs skips equal digits.
    words = array("I", [0])
    keys = array("I", [0])
    runs = array("I", [0])
    allowed = array("Q", [(1 << base) - 2])
    begin = 0
    end = 1
    forbidden = array("I")
    fkeys = array("I")
    # Breadth first and lexicographic order make the first word of a pair least.
    # Intersecting the extension masks of its deletions skips nonminimal failures.
    for length in range(LONGEST):
        for r in range(begin, end):
            s, q = divmod(keys[r], width)
            word = words[r]
            last = word & DIGIT_MASK
            if r:
                mask = allowed[word >> SHIFT] & ~((1 << last) - 1)
                rem = runs[r]
                while rem and mask:
                    drop = words[rem] & DIGIT_MASK
                    parent = where[offsets[s - drop] + (q - drop * drop) // 2]
                    mask &= allowed[parent]
                    rem = runs[rem]
            else:
                mask = allowed[0]
            kept = mask
            while mask:
                bit = mask & -mask
                d = bit.bit_length() - 1
                mask -= bit
                ns = s + d
                nq = q + d * d
                at = offsets[ns] + nq // 2
                if where[at] < 0:
                    # The last layer only detects collisions; fixed parts are
                    # shorter, so its successful words need no records.
                    where[at] = 0
                    if length < MAX_FIXED:
                        where[at] = len(words)
                        words.append((r << SHIFT) | d)
                        keys.append(ns * width + nq)
                        runs.append(runs[r] if d == last else r)
                        allowed.append(0)
                else:
                    kept -= bit
                    forbidden.append((r << SHIFT) | d)
                    fkeys.append(ns * width + nq)
            allowed[r] = kept
        begin, end = end, len(words)
    del allowed
    rays = array("Q", [0]) * len(words)
    pairs = array("Q", [0]) * len(words)
    # Deleting all occurrences of a starred digit projects each obstruction
    # onto a finite word that blocks that star. Do the same for adjacent pairs.
    for i, code in enumerate(forbidden):
        s, q = divmod(fkeys[i], width)
        counts = bytearray(base)
        digit = code & DIGIT_MASK
        counts[digit] = 1
        support = 1 << digit
        r = code >> SHIFT
        while r:
            digit = words[r] & DIGIT_MASK
            counts[digit] += 1
            support |= 1 << digit
            r = words[r] >> SHIFT
        touched = 0
        while support:
            bit = support & -support
            d = bit.bit_length() - 1
            support -= bit
            c = counts[d]
            at = where[offsets[s - d * c] + (q - d * d * c) // 2]
            rays[at] |= 1 << d
            touched |= (1 << d) | (1 << (d - 1))
        touched &= (1 << m) - 2
        while touched:
            bit = touched & -touched
            d = bit.bit_length() - 1
            touched -= bit
            a = counts[d]
            b = counts[d + 1]
            at = where[
                offsets[s - d * a - (d + 1) * b] + (q - d * d * a - (d + 1) * (d + 1) * b) // 2
            ]
            pairs[at] |= bit
    del forbidden, fkeys
    allrays = (1 << base) - 2
    allpairs = (1 << m) - 2
    lines = []
    # Blocked stars propagate from immediate subwords. Two free digits must
    # be adjacent, so these two masks describe every possible free set.
    for r, word in enumerate(words):
        badr = rays[r]
        badp = pairs[r]
        support = 0
        if r:
            drop = word & DIGIT_MASK
            support = 1 << drop
            parent = word >> SHIFT
            badr |= rays[parent]
            badp |= pairs[parent]
            rem = runs[r]
            if rem:
                s, q = divmod(keys[r], width)
                while rem:
                    drop = words[rem] & DIGIT_MASK
                    support |= 1 << drop
                    parent = where[offsets[s - drop] + (q - drop * drop) // 2]
                    badr |= rays[parent]
                    badp |= pairs[parent]
                    rem = runs[rem]
        rays[r] = badr
        pairs[r] = badp
        validr = allrays & ~badr
        validp = allpairs & ~badp
        # A larger free set covers the single-star or finite case, including
        # cases where a newly freed digit had a positive fixed count.
        singles = validr & ~support & ~(validp | (validp << 1))
        doubles = validp & ~(support | (support >> 1))
        if not validr or singles or doubles:
            digits = []
            rem = r
            while rem:
                digits.append(DIGITS[words[rem] & DIGIT_MASK])
                rem = words[rem] >> SHIFT
            fixed = "".join(reversed(digits))
            if not validr:
                lines.append(fixed)
            while singles:
                bit = singles & -singles
                singles -= bit
                d = bit.bit_length() - 1
                digit = DIGITS[d]
                at = bisect_left(fixed, digit)
                lines.append(fixed[:at] + digit + "*" + fixed[at:])
            while doubles:
                bit = doubles & -doubles
                doubles -= bit
                d = bit.bit_length() - 1
                digit = DIGITS[d]
                at = bisect_left(fixed, digit)
                lines.append(fixed[:at] + digit + "*" + DIGITS[d + 1] + "*" + fixed[at:])

    lines.sort()
    sys.stdout.write("\n".join(lines) + "\n")


solve(int(sys.stdin.buffer.read()))
