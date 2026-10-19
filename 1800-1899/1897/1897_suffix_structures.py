from array import array
import sys

BYTE_VALUES = 256
TURN_BLOCK = 4
JIT_THRESHOLD = 400
JIT_EAGERNESS = 50
WORD_BITS = 60
REPEAT_BITS_PER_CHARACTER = 512
ODD_BASE = 3
ALTERNATING_BITS = ((1 << WORD_BITS) - 1) // ODD_BASE

PYPY = sys.implementation.name == "pypy"

if PYPY:
    import pypyjit

    pypyjit.set_param(
        threshold=JIT_THRESHOLD,
        function_threshold=JIT_THRESHOLD,
        trace_eagerness=JIT_EAGERNESS,
    )


def integers(value, size):
    # PyPy keeps homogeneous integer lists unboxed; CPython needs explicit arrays.
    if PYPY:
        return [value] * size
    return array("i", [value]) * size


def bitset_game(original, k, n, sigma, transitions, used, lengths, links,
                  occurrences, ends, states, mask, children, sibling):
    wins = [0] * used

    def value(v, length):
        if occurrences[v] == 1:
            return min(ends[v] - length + 1, n - ends[v] - 1) & 1
        return (wins[v] >> (lengths[v] - length)) & 1

    for entry in reversed(states):
        v = entry & mask
        if occurrences[v] == 1:
            continue
        upper = lengths[v]
        lower = lengths[links[v]] + 1 if v else 0
        top_win = 0
        child = children[v]
        while child >= 0 and not top_win:
            base = child * sigma
            for c in range(sigma):
                q = transitions[base + c]
                if q and not value(q, upper + 2):
                    top_win = 1
                    break
            child = sibling[child]
        if upper == lower:
            wins[v] = top_win
            continue
        width = upper - lower + 1
        limit = (1 << width) - 1
        combined = limit
        base = v * sigma
        for c in range(sigma):
            q = transitions[base + c]
            if not q:
                continue
            if occurrences[q] == 1:
                end = ends[q]
                right = n - end - 1
                cut = min(width, max(0, upper + 2 - (end - right + 1)))
                low = (1 << cut) - 1
                if width <= WORD_BITS:
                    alternating = ALTERNATING_BITS
                elif width & 1:
                    alternating = (2 * limit + 1) // ODD_BASE
                else:
                    alternating = limit // ODD_BASE
                if not ((end - upper - 1) & 1):
                    alternating <<= 1
                result = alternating & low
                if right & 1:
                    result |= limit ^ low
            else:
                shift = lengths[q] - upper - 2
                result = wins[q] >> shift if shift >= 0 else wins[q] << -shift
            combined &= result
        wins[v] = ((combined ^ limit) & ~1) | top_win
    if wins[0] & 1:
        if k == 1:
            return b"-"
        k -= 1
    v = children[0]
    while v >= 0:
        upper = lengths[v]
        lower = lengths[links[v]] + 1
        if occurrences[v] == 1:
            end = ends[v]
            right = n - end - 1
            boundary = min(upper, end - right + 1)
            first_count = max(0, boundary - lower + 1) if right & 1 else 0
            first = max(lower, boundary + 1)
            first += (first ^ end) & 1
            count = first_count + max(0, (upper - first) // 2 + 1)
            if k <= count:
                length = lower + k - 1 if k <= first_count else first + 2 * (k - first_count - 1)
                start = n - end - 1
                return original[start : start + length]
        else:
            bits = wins[v]
            count = bits.bit_count()
            if k <= count:
                for length in range(lower, upper + 1):
                    k -= (bits >> (upper - length)) & 1
                    if not k:
                        start = n - ends[v] - 1
                        return original[start : start + length]
        k -= count
        if children[v] >= 0:
            v = children[v]
        else:
            while v >= 0 and sibling[v] < 0:
                v = links[v]
            if v >= 0:
                v = sibling[v]
    return b"no solution"


def solve(s, k):
    n = len(s)
    # Each winning string chooses a distinct losing extension with that string as its middle.
    if k > (n * (n + 1) // 2 + 1) // 2:
        return b"no solution"
    if s.count(s[:1]) == n:
        if n % TURN_BLOCK == 2:
            if k == 1:
                return b"-"
            k -= 1
            first = TURN_BLOCK - 1
        else:
            first = (n + 1) % TURN_BLOCK
        length = first + TURN_BLOCK * ((k - 1) // 2) + (k - 1) % 2
        if length > n:
            return b"no solution"
        return s[:length] if length else b"-"
    # Reversed suffix links form the original suffix tree and provide lexicographic order.
    original = s
    s = s[::-1]
    alphabet = sorted(set(s))
    sigma = len(alphabet)
    codes = [0] * BYTE_VALUES
    for i, c in enumerate(alphabet):
        codes[c] = i
    capacity = 2 * n + 1
    transitions = integers(0, capacity * sigma)
    lengths = integers(0, capacity)
    links = integers(-1, capacity)
    occurrences = integers(0, capacity)
    ends = integers(-1, capacity)
    used = 1
    last = 0
    distinct = 1
    for i, c in enumerate(s):
        c = codes[c]
        cur = used
        used += 1
        lengths[cur] = lengths[last] + 1
        occurrences[cur] = 1
        ends[cur] = i
        p = last
        while p >= 0 and not transitions[p * sigma + c]:
            transitions[p * sigma + c] = cur
            p = links[p]
        if p < 0:
            links[cur] = 0
        else:
            q = transitions[p * sigma + c]
            if lengths[p] + 1 == lengths[q]:
                links[cur] = q
            else:
                clone = used
                used += 1
                lengths[clone] = lengths[p] + 1
                links[clone] = links[q]
                ends[clone] = ends[q]
                a = clone * sigma
                b = q * sigma
                transitions[a : a + sigma] = transitions[b : b + sigma]
                links[q] = links[cur] = clone
                while p >= 0 and transitions[p * sigma + c] == q:
                    transitions[p * sigma + c] = clone
                    p = links[p]
        last = cur
        distinct += lengths[cur] - lengths[links[cur]]
    if k > distinct // 2:
        return b"no solution"
    bits = used.bit_length()
    mask = (1 << bits) - 1
    states = sorted((lengths[v] << bits) + v for v in range(used))
    children = integers(-1, used)
    sibling = integers(-1, used)
    buckets = [[] for _ in range(sigma)]
    for v in range(1, used):
        p = links[v]
        buckets[codes[s[ends[v] - lengths[p]]]].append(v)
    for bucket in reversed(buckets):
        for v in bucket:
            p = links[v]
            sibling[v] = children[p]
            children[p] = v
    repeat_volume = 0
    for entry in reversed(states[1:]):
        v = entry & mask
        occurrences[links[v]] += occurrences[v]
        if occurrences[v] > 1:
            repeat_volume += lengths[v] - lengths[links[v]]
    # Bitsets cover only repeated strings; the budget keeps their combined size linear.
    if repeat_volume <= REPEAT_BITS_PER_CHARACTER * n:
        return bitset_game(original, k, n, sigma, transitions, used, lengths, links,
                             occurrences, ends, states, mask, children, sibling)
    # Each parity uses a shared run list, with a skipped prefix and a lazy complement.
    heads = integers(0, 2 * used)
    skips = integers(0, 2 * used)
    flips = bytearray(2 * used)
    run_lengths = integers(n + 1, 1)
    run_values = bytearray([0])
    run_next = integers(0, 1)

    def run(size, value, nex):
        v = len(run_lengths)
        run_lengths.append(size)
        run_values.append(value)
        run_next.append(nex)
        return v

    def value(v, length):
        parity = length & 1
        index = 2 * v + parity
        upper = lengths[v] - ((lengths[v] - parity) & 1)
        offset = (upper - length) // 2 + skips[index]
        node = heads[index]
        while offset >= run_lengths[node]:
            offset -= run_lengths[node]
            node = run_next[node]
        return run_values[node] ^ flips[index]

    for entry in reversed(states):
        v = entry & mask
        upper = lengths[v]
        lower = lengths[links[v]] + 1 if v else 0
        # A unique occurrence can only expand until it reaches the nearer boundary.
        if occurrences[v] == 1:
            end = ends[v]
            right = n - end - 1
            for parity in range(2):
                top = upper - ((upper - parity) & 1)
                bottom = lower + ((lower - parity) & 1)
                if top < bottom:
                    continue
                width = (top - bottom) // 2 + 1
                start = end - top + 1
                first = start & 1
                last = right & 1
                before = min(width, max(0, (right - start + 1) // 2))
                index = 2 * v + parity
                if first == last or not before:
                    flips[index] = last
                elif before == width:
                    flips[index] = first
                else:
                    heads[index] = run(before, 1, 0)
                    flips[index] = last
            continue
        base = v * sigma
        outgoing = []
        for c in range(sigma):
            q = transitions[base + c]
            if q:
                outgoing.append(q)
        if not outgoing:
            continue
        # Only the longest string can have several left contexts: its suffix-link children.
        top_win = 0
        child = children[v]
        while child >= 0 and not top_win:
            b = child * sigma
            for c in range(sigma):
                q = transitions[b + c]
                if q and not value(q, upper + 2):
                    top_win = 1
                    break
            child = sibling[child]
        # Below the longest length, the left letter is forced; right moves shift by two.
        if len(outgoing) == 1:
            q = outgoing[0]
            for parity in range(2):
                index = 2 * v + parity
                qi = 2 * q + parity
                top = upper - ((upper - parity) & 1)
                bottom = lower + ((lower - parity) & 1)
                if top < bottom:
                    continue
                add = parity == (upper & 1)
                next_top = top - 2 * add
                flip = flips[qi] ^ 1
                if next_top >= bottom:
                    child_top = lengths[q] - ((lengths[q] - parity) & 1)
                    offset = (child_top - next_top - 2) // 2 + skips[qi]
                    node = heads[qi]
                    while offset >= run_lengths[node]:
                        offset -= run_lengths[node]
                        node = run_next[node]
                else:
                    node = 0
                    offset = 0
                    flip = top_win
                if add:
                    bit = top_win ^ flip
                    if node == 0 and not bit:
                        offset = 0
                    elif bit == run_values[node]:
                        node = run(run_lengths[node] - offset + 1, bit, run_next[node])
                        offset = 0
                    else:
                        if offset:
                            node = run(run_lengths[node] - offset, run_values[node], run_next[node])
                        node = run(1, bit, node)
                        offset = 0
                heads[index] = node
                skips[index] = offset
                flips[index] = flip
        else:
            # Right-branching strings are explicit suffix-tree nodes; their total is linear.
            for parity in range(2):
                bottom = lower + ((lower - parity) & 1)
                node = 0
                for length in range(bottom, upper + 1, 2):
                    if length == upper:
                        bit = top_win
                    else:
                        bit = 0
                        for q in outgoing:
                            if not value(q, length + 2):
                                bit = 1
                                break
                    if node == 0 and bit == 0:
                        continue
                    if node and run_values[node] == bit:
                        run_lengths[node] += 1
                    else:
                        node = run(1, bit, node)
                heads[2 * v + parity] = node
    if value(0, 0):
        if k == 1:
            return b"-"
        k -= 1
    v = children[0]
    while v >= 0:
        upper = lengths[v]
        lower = lengths[links[v]] + 1
        if upper == lower:
            count = value(v, upper)
        elif occurrences[v] == 1:
            end = ends[v]
            right = n - end - 1
            boundary = min(upper, end - right + 1)
            count = max(0, boundary - lower + 1) if right & 1 else 0
            first = max(lower, boundary + 1)
            first += (first ^ end) & 1
            count += max(0, (upper - first) // 2 + 1)
        else:
            count = 0
            for parity in range(2):
                top = upper - ((upper - parity) & 1)
                bottom = lower + ((lower - parity) & 1)
                if top < bottom:
                    continue
                left = (top - bottom) // 2 + 1
                index = 2 * v + parity
                node = heads[index]
                offset = skips[index]
                flip = flips[index]
                while left:
                    size = min(left, run_lengths[node] - offset)
                    if run_values[node] ^ flip:
                        count += size
                    left -= size
                    node = run_next[node]
                    offset = 0
        if k <= count:
            candidates = []
            for parity in range(2):
                top = upper - ((upper - parity) & 1)
                bottom = lower + ((lower - parity) & 1)
                if top < bottom:
                    continue
                left = (top - bottom) // 2 + 1
                index = 2 * v + parity
                node = heads[index]
                offset = skips[index]
                flip = flips[index]
                while left:
                    size = min(left, run_lengths[node] - offset)
                    if run_values[node] ^ flip:
                        candidates.extend(range(top - 2 * (size - 1), top + 1, 2))
                    top -= 2 * size
                    left -= size
                    node = run_next[node]
                    offset = 0
            candidates.sort()
            start = n - ends[v] - 1
            return original[start : start + candidates[k - 1]]
        k -= count
        if children[v] >= 0:
            v = children[v]
        else:
            while v >= 0 and sibling[v] < 0:
                v = links[v]
            if v >= 0:
                v = sibling[v]
    return b"no solution"


if __name__ == "__main__":
    s, k = sys.stdin.buffer.read().split()
    sys.stdout.buffer.write(solve(s, int(k)) + b"\n")
